---
layout: post
title: "mcp 配置 结合大模型，AI操控 浏览器，文件系统 ，结合官方文档"
date: 2025-05-09 09:00:00
summary: "\"mcpServers\": {"
categories: AI
---


{  
"mcpServers": {  
"context7-mcp": {  
"isActive": true,  
"command": "cmd",  
"args": [  
"/c",  
"npx",  
"-y",  
"@smithery/cli@latest",  
"run",  
"@upstash/context7-mcp",  
"--key",  
"ecdff2bd-17e8-4d9d-81d1-fc2e388d8e3b"  
],  
"name": "context7-mcp"  
},  
"playwright": {  
"isActive": true,  
"command": "cmd",  
"args": [  
"/c",  
"npx",  
"-y",  
"@executeautomation/playwright-mcp-server"  
],  
"shell": true,  
"name": "playwright"  
},  
"filesystem": {  
"isActive": true,  
"command": "cmd",  
"args": [  
"/c",  
"npx",  
"-y",  
"@modelcontextprotocol/server-filesystem",  
"E:\Projcet\otherproject\mromroforwardgit\mroforward\mroforward"  
],  
"shell": true,  
"name": "filesystem"  
},  
"server-sequential-thinking": {  
"isActive": true,  
"command": "cmd",  
"args": [  
"/c",  
"npx",  
"-y",  
"@smithery/cli@latest",  
"run",  
"@smithery-ai/server-sequential-thinking",  
"--key",  
"ecdff2bd-17e8-4d9d-81d1-fc2e388d8e3b"  
],  
"shell": true,  
"name": "server-sequential-thinking"  
}  
}  
}

npm install -g @executeautomation/playwright-mcp-server

npx -y @smithery/cli install @executeautomation/playwright-mcp-server --client cursor
