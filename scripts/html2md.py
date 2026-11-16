# -*- coding: utf-8 -*-
"""把 Gridea 生成的 HTML 文章反解为 Jekyll Markdown。

用法:
    python scripts/html2md.py <源myblogs目录> <输出_posts目录> [--limit N]

处理要点:
1. 定位 <div class="post-content" v-pre> 区段，只取正文。
2. 42 张 base64 内嵌图抽成实体文件，写入 images/posts/<slug>/。
3. 剥离 hljs 高亮 span，保留 <pre><code> 纯文本，并补回 language-xxx 标识。
4. 用 markdownify 转 Markdown，再修正 GFM 表格与代码围栏。
5. 生成 Jekyll front matter：title/date/categories/summary。
"""
import base64
import io
import os
import re
import sys

from bs4 import BeautifulSoup
from markdownify import markdownify

POST_CONTENT_RE = re.compile(
    r'<div class="post-content" v-pre>(.*?)\n\s{12}</div>', re.S
)
TITLE_RE = re.compile(r'<h2 class="post-title">(.*?)</h2>', re.S)
DATE_RE = re.compile(r'<div class="post-date">(.*?)</div>', re.S)
TAG_RE = re.compile(r'<title>(.*?) \|[^<]*</title>', re.S)


def extract(path):
    html = io.open(path, encoding='utf-8', errors='replace').read()
    body = POST_CONTENT_RE.search(html)
    if not body:
        return None
    title = TITLE_RE.search(html)
    date = DATE_RE.search(html)
    doc_title = TAG_RE.search(html)
    return {
        'body': body.group(1),
        'title': (title.group(1) if title else
                  (doc_title.group(1) if doc_title else '') ).strip(),
        'date': (date.group(1) if date else '').strip(),
    }


def dump_images(soup, slug, image_root):
    """把 base64 img 落盘，返回替换后的文件名前缀。"""
    n = 0
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if not src.startswith('data:image'):
            continue
        m = re.match(r'data:image/(\w+);base64,(.*)', src, re.S)
        if not m:
            continue
        ext = 'png' if m.group(1) == 'png' else m.group(1).replace('jpeg', 'jpg')
        n += 1
        outdir = os.path.join(image_root, slug)
        os.makedirs(outdir, exist_ok=True)
        name = f'img-{n:02d}.{ext}'
        with open(os.path.join(outdir, name), 'wb') as fh:
            fh.write(base64.b64decode(m.group(2)))
        img['src'] = f'/images/posts/{slug}/{name}'
    return n


def strip_hljs(soup):
    """把 <pre><code class="language-x hljs"> 里的高亮 span 还原成纯文本。"""
    langs = []
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code is None:
            continue
        cls = ' '.join(code.get('class') or [])
        m = re.search(r'language-([\w+-]+)', cls)
        lang = m.group(1) if m else ''
        if lang == 'csharp':
            lang = 'csharp'
        text = code.get_text()
        # markdownify 会保留 pre/code，这里用占位符暂时替换，避免 span 被转义
        placeholder = f'@@CODEBLOCK{len(langs)}@@'
        langs.append((placeholder, lang, text))
        pre.replace_with(placeholder)


def to_markdown(fragment, slug, image_root):
    soup = BeautifulSoup(fragment, 'html.parser')
    dump_images(soup, slug, image_root)
    strip_hljs(soup)
    md = markdownify(str(soup), heading_style='ATX', bullets='-',
                     strip=['figure'], escape_underscores=False)
    # 占位符还原为围栏代码块
    for placeholder, lang, text in re.findall(
            r'(@@CODEBLOCK(\d+)@@)', md):
        pass
    for idx, (placeholder, lang, text) in enumerate(_saved_blocks):
        fence = f'\n```{lang}\n{text.rstrip()}\n```\n'
        md = md.replace(placeholder, fence)
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = md.strip()
    return md


def clean_inline(md):
    """修正 markdownify 常见的多余转义与空链接。"""
    md = md.replace('\\_', '_')
    md = re.sub(r'!\[\]\(([^)]+)\)', r'![](\1)', md)
    # 原 HTML 的 alt 常是浏览器抓图产生的路径垃圾，统一清成空 alt
    md = re.sub(r'!\[[^\]]*\\?\.png[^\]]*\]\(', '![](', md)
    md = re.sub(r'!\[[^\]]{60,}\]\(', '![](', md)
    md = re.sub(r'!\[[^\]]*_files[^\]]*\]\(', '![](', md)
    return md


def strip_leading_frontmatter(md):
    """只有当正文开头确实是 YAML front matter（首行 ---，且第二行是 key: value）时
    才剥掉，避免把 `---`（原文的 <hr>）误当成 front matter 边界。"""
    lines = md.split('\n')
    if len(lines) < 3 or lines[0].strip() != '---':
        return md
    if not re.match(r'^[A-Za-z_][\w-]*\s*:', lines[1]):
        return md
    for i in range(1, min(len(lines), 40)):
        if lines[i].strip() == '---':
            return '\n'.join(lines[i + 1:]).lstrip('\n')
    return md


def drop_hugo_header_block(md):
    """Gridea 常把 Hugo 的 YAML 头当成普通文本渲染成一个标题块，
    例如 `## tags: ["AI"] title: "..." weight: 1 description: >`。
    这类以 YAML 键开头、且含两个以上 `key:` 的标题行整行删掉。"""
    out = []
    for line in md.split('\n'):
        stripped = line.lstrip('#').strip()
        if line.lstrip().startswith('#') and len(
                re.findall(r'\b(tags|title|linkTitle|weight|description|'
                           r'draft|categories|slug|summary)\s*:', stripped)) >= 2:
            continue
        out.append(line)
    return '\n'.join(out)


def yaml_safe(value):
    """标题/摘要里常含冒号、井号、方括号，直接裸写会让 YAML 解析失败。
    统一用双引号包起来并转义内部双引号与反斜杠。"""
    text = (value or '').replace('\\', '\\\\').replace('"', '\\"')
    text = re.sub(r'\s+', ' ', text).strip()
    return f'"{text}"'


def pick_summary(md):
    """从正文里挑第一段真正的文字当摘要，跳过标题、引用与代码围栏。"""
    for raw in md.split('\n'):
        line = raw.strip()
        if not line or line.startswith(('#', '>', '```', '|', '!', '-', '*')):
            continue
        text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', line)
        text = re.sub(r'[*`_~]', '', text).strip()
        if len(text) >= 12:
            return text[:100]
    return ''


_saved_blocks = []


def convert_one(src_dir, slug, out_dir, image_root):
    global _saved_blocks
    _saved_blocks = []
    path = os.path.join(src_dir, slug, 'index.html')
    data = extract(path)
    if not data:
        return None, 'no post-content'

    # 重新解析一次，把代码块真正保存到全局
    soup = BeautifulSoup(data['body'], 'html.parser')
    n_img = dump_images(soup, slug, image_root)
    blocks = []
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code is None:
            continue
        cls = ' '.join(code.get('class') or [])
        m = re.search(r'language-([\w+-]+)', cls)
        lang = m.group(1) if m else ''
        blocks.append((f'@@CODEBLOCK{len(blocks)}@@', lang, code.get_text()))
        pre.replace_with(blocks[-1][0])
    _saved_blocks = blocks

    md = markdownify(str(soup), heading_style='ATX', bullets='-',
                     strip=['figure'], escape_underscores=False)
    for placeholder, lang, text in blocks:
        md = md.replace(placeholder, f'\n```{lang}\n{text.rstrip()}\n```\n')
    md = clean_inline(md)
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    md = strip_leading_frontmatter(md)
    md = drop_hugo_header_block(md)
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    title = data['title']
    date = data['date'] or '2020-01-01'
    summary = pick_summary(md)
    # 原文里顺手带过来的 tags 行不该留在正文
    md = re.sub(r'^\s*tags:\s*\[?[^\]\n]*\]?\s*$', '', md, flags=re.M)
    md = re.sub(r'\n{3,}', '\n\n', md).strip()

    fm = ['---', 'layout: post', f'title: {yaml_safe(title)}',
          f'date: {date} 09:00:00',
          f'summary: {yaml_safe(summary)}', 'categories: Notes', '---', '', md, '']
    out = os.path.join(out_dir, f'{date}-{slug}.md')
    io.open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(fm))
    return out, f'{len(md)} chars, {n_img} imgs, {len(blocks)} code'


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    src, dst = sys.argv[1], sys.argv[2]
    limit = None
    if '--limit' in sys.argv:
        limit = int(sys.argv[sys.argv.index('--limit') + 1])
    image_root = os.path.join(os.path.dirname(dst.rstrip('/\\')), 'images', 'posts')
    os.makedirs(dst, exist_ok=True)
    slugs = sorted(d for d in os.listdir(src)
                   if os.path.isdir(os.path.join(src, d)))
    if limit:
        slugs = slugs[:limit]
    ok = fail = 0
    for slug in slugs:
        try:
            out, info = convert_one(src, slug, dst, image_root)
        except Exception as exc:  # noqa: BLE001
            print(f'FAIL {slug}: {exc}')
            fail += 1
            continue
        if out:
            print(f'OK   {slug} -> {os.path.basename(out)} ({info})')
            ok += 1
        else:
            print(f'SKIP {slug}: {info}')
            fail += 1
    print(f'\n完成: {ok} 成功, {fail} 跳过/失败')
    return 0


if __name__ == '__main__':
    sys.exit(main())
