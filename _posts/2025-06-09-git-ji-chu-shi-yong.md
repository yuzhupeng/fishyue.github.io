---
layout: post
title: git基础使用
date: 2025-06-09 09:00:00
summary: git是一个免费的开源的分布式版本控制系统,可以快速高效的处理从小型到大型项目的所有事务
categories: Note
---

**1.git简介**

git是一个免费的开源的分布式版本控制系统,可以快速高效的处理从小型到大型项目的所有事务

在实际工作中可以保留项目的所有版本,可以快速的实现版本的回滚和修改

git整体可以分为4个区域的划分

- 工作区：程序员直接修改代码文件
- 暂存区：暂存修改的文件
- 版本库：提交到本地一个版本
- 远程仓：远程存放代码，便于共享

![](/images/posts/git-ji-chu-shi-yong/img-01.png)

**2.git的安装**

<https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git>

产看版本信息

git --version

![](/images/posts/git-ji-chu-shi-yong/img-02.png)

**3.git初始化**

**3.1 目录初始化**

我们安装git之后,接下来就是创建一个目录，用做初始化，也就是让git管理该目录

初始化目录

git **init**

![](/images/posts/git-ji-chu-shi-yong/img-03.png)

**3.2 用户配置**

对于刚下载的git，我们通常要配置用户名和邮箱，为了以后提交代码使用，只需要配置一次即可

查看当前git配置

git config *--list*

![](/images/posts/git-ji-chu-shi-yong/img-04.png)

# 配置用户名和邮箱

git **config** --**global** user.name "用户名"

git **config** --**global** user.email "邮箱"

![](/images/posts/git-ji-chu-shi-yong/img-05.png)

**4.git本地常用操作**

**4.1查看git文件状态**

我们在做任何操作的时候，都会确定当前文件状态

git status

**4.2 加入暂存区**

将所有的已修改或者新建的文件加入缓存

git **add** .

​

将指定的文件加入缓存

git **add** 文件名字

![](/images/posts/git-ji-chu-shi-yong/img-06.png)

**4.3 加入版本管理**

git **commit** -m "提交备注"

![](/images/posts/git-ji-chu-shi-yong/img-07.png)

**4.4 查看提交记录**

简单查看

git log

​

一行显示

git log *--oneline*

​

可以显示分支关系

git log –-pretty=oneline *--graph*

​

查看原始log

git reflog

![](/images/posts/git-ji-chu-shi-yong/img-08.png)

**4.5 查看某次提交做的修改**

git **show** commitID

![](/images/posts/git-ji-chu-shi-yong/img-09.png)

**4.6 查看当前修改的内容**

查看工作区和版本区的不同

git **diff**

​

查看暂存区和版本区的不同

git __diff __--**cached**

​

查看两次提交记录之间的不同

git __diff __commitID1 commitID2

![](/images/posts/git-ji-chu-shi-yong/img-10.png)

**4.7 清除未被git管理的文件**

我们在编译项目的时候，如C语言，会产生大量的中间文件，这些是不需要提交的文件

将git未被管理的文件或者文件夹清除，注意，对于新加的文件也会清除，需要先加入缓存

git clean -df

**4.8 撤销操作**

![](/images/posts/git-ji-chu-shi-yong/img-11.png)

**4.8.1 撤销工作区修改**

git checkout 文件名称

![](/images/posts/git-ji-chu-shi-yong/img-12.png)

**4.8.2 撤销暂存区的修改**

以下两个命令都可以

git reset HEAD

git restore --staged 文件名

![](/images/posts/git-ji-chu-shi-yong/img-13.png)

**4.8.3 撤销版本区到暂存区**

git reset --soft commitID

![](/images/posts/git-ji-chu-shi-yong/img-14.png)

**4.8.4 撤销版本区到工作区的已修改**

git reset --mix commitID

![](/images/posts/git-ji-chu-shi-yong/img-15.png)

**4.8.5 撤销版本区到工作区，工作区内容完全清除**

慎用！！

git reset --hard commitID

![](/images/posts/git-ji-chu-shi-yong/img-16.png)

**5.HEAD**

HEAD是指向__当前所在分支__的__当前提交记录__的引用标识符

HEAD^ : 当前提交记录的上一次提交记录

**HEAD^^: 当前提交记录的上上次提交记录**

​

如：git show HEAD^ 显示上上次的提交记录

**6.分支**

分支本质上就是只想提交对象的可变指针,git中的分支才是我们有可能完成多人协同开发，使用分支的场景

- 多人协同开发，最后合并代码
- 一个人针对不同的开发，在不同分支上开发，避免影响主分支

**6.1 查看分支**

查看所有的本地分支

git __branch __

​

查看多有分支，包括远端分支

git __branch __-a

​

查看分支的详细信息，包括跟踪分支

git __branch __-vv

**6.2 创建分支**

git __branch __分支名字

![](/images/posts/git-ji-chu-shi-yong/img-17.png)

**6.3 切换分支**

git checkout 分支名

![](/images/posts/git-ji-chu-shi-yong/img-18.png)

**6.4 创建并切换分支**

git checkout -**b** 分支名

![](/images/posts/git-ji-chu-shi-yong/img-19.png)

**6.5 删除分支**

删除分支的时候必须切换到其他分支才能删除指定分支

删除分支

git __branch __-d 分支名

​

强制删除分支

git __branch __-D 分支名

![](/images/posts/git-ji-chu-shi-yong/img-20.png)

**6.6 合并分支**

合并分支的时候，如果希望A分支合并到B分支，那么首先要切换到B分支上

git **merge** 要合并的分支

![](/images/posts/git-ji-chu-shi-yong/img-21.png)
![](/images/posts/git-ji-chu-shi-yong/img-22.png)

**6.7 变基合并**

变基可以保持代码提交的整洁

git rebase 分支名

![](/images/posts/git-ji-chu-shi-yong/img-23.png)

通过merge合并分支，查看log记录，饿哦们可以很清晰的看出两个分支在什么位置合并的，各个分支的节点，但如果分支很多，合并很复杂，也是感觉很乱的，如果我们希望log记录是一条直线，可以考虑变基合并，如下两张图

![](/images/posts/git-ji-chu-shi-yong/img-24.png)
![](/images/posts/git-ji-chu-shi-yong/img-25.png)

**6.8 cherry-pick**

如果我们不希望合并整个分支，只希望获取其他分支的一个或者几个提交，那么就可以使用如下

git cherry-pick commitID

![](/images/posts/git-ji-chu-shi-yong/img-26.png)
![](/images/posts/git-ji-chu-shi-yong/img-27.png)

**6.9 stash操作**

我们在一个分支上工作的时候，如果需要切换到另一个分支，但又不希望提交当前的修改，我们可以隐藏当前分支的修改

显示所有的隐藏记录

git stash list

​

将当前分支的所有修改隐藏

git stash

​

弹出隐藏记录

git stash **pop**

![](/images/posts/git-ji-chu-shi-yong/img-28.png)

**7.冲突**

冲突产生的原因就是两个要合并分支(或者节点)对同一个文件的的同一行文件做了修改，关于合并的操作都可能产生冲突

git **merge**

git rebase

git cherry-pick

git pull

git **fetch**

..

解决冲突的办法(git merge)

1. 找到产生冲突的文件，寻找产生冲突的代码
2. 决定保留那一个分支上的代码
3. 重新提交
4. git **add**

git **commit**

![](/images/posts/git-ji-chu-shi-yong/img-29.png)
![](/images/posts/git-ji-chu-shi-yong/img-30.png)
![](/images/posts/git-ji-chu-shi-yong/img-31.png)

**8.远程操作**

远程仓库，顾名思义就是在远端有一个仓库，存储这我们的代码，我们要做的就是实现本地仓库和远程仓库的交互

我们常用的就是github，可以自己上去申请一个账号<https://github.com/>

![](/images/posts/git-ji-chu-shi-yong/img-32.png)

**8.1 代码仓克隆**

克隆之后的本地仓库，会默认生成远程分支跟踪远程仓库的所有分支

![](/images/posts/git-ji-chu-shi-yong/img-33.png)

git clone 远程仓地址

![](/images/posts/git-ji-chu-shi-yong/img-34.png)
![](/images/posts/git-ji-chu-shi-yong/img-35.png)

**8.2 远程仓管理**

显示远程仓名字，默认为origin

git remote

​

在指定的远程仓中添加分支

git **push** origin 分支名字

​

在指定的远程仓库中删除一个分支

git **push** origin --**delete** 分支名字

![](/images/posts/git-ji-chu-shi-yong/img-36.png)
![](/images/posts/git-ji-chu-shi-yong/img-37.png)

**8.3 推送代码**

git **push** origin 本地分支:远端分支

远端分支不存在自动则创建

![](/images/posts/git-ji-chu-shi-yong/img-38.png)

**8.4 拉取代码-fetch**

将本地远程分支更新到远程分支的最新状态,但是本地分支不发生改变

拉取特定的一个分支

git **fetch** origin 远端分支

​

拉去仓库的所有分支

git **fetch**

![](/images/posts/git-ji-chu-shi-yong/img-39.png)

**8.5拉取代码-pull**

将本地远程分支更新到远程仓库最新状态，然后合并本地分支

使用该命令的前提是本地分支跟踪远端分支

git branch -u 本地远端分支名字

​

​

分支跟踪之后，以后推送代码和拉取代码就很简单了

git **push**

git pull

![](/images/posts/git-ji-chu-shi-yong/img-40.png)

git pull = git **fetch** + git **merge**

拉取指定的分支

git pull __origin __远程分支

​

拉去所有追踪的分支

git pull

![](/images/posts/git-ji-chu-shi-yong/img-41.png)

**9.其他**

**9.1 ssh**

我们可以使用ssh的url进行克隆,但是需要生成ssh key

1. 在本地电脑执行命令 ssh-keyge -t rsa -C “email”

2. vim ~/.ssh.id\*_rsa.pub\*

*3. 在github中添加公钥*

**9.2 git blame**

该命令可以显示该文件每一行代码的修改人，日期等，以便追查责任人

git __blame __filename

![](/images/posts/git-ji-chu-shi-yong/img-42.png)
