# 前端开发入口

React + TypeScript + Vite。建议使用 Node.js 24 LTS（最低 22.12）。在本目录运行：

```powershell
npm ci
Copy-Item .env.example .env
npm run dev
```

访问 http://127.0.0.1:5173 。另行启动后端 8000 端口，首页会调用真实 /health；未启动时显示未连接提示。

- `src/app`：应用入口与路由。
- `src/pages`：市场、应用详情、版本列表、版本详情、社区、工作台、登录和管理页面。
- `src/components`：公共布局和组件。
- `src/api`：唯一 HTTP 入口；统一错误、204、取消请求，不自动重试写请求。
- `src/hooks`：可复用状态逻辑。
- `src/types`：接口类型，业务类型按 `../contracts/openapi.json` 补齐。
- `src/styles`：全局样式。`public`：公开静态资源。

`npm run typecheck` 检查类型，`npm run build` 检查类型并打包，`npm run preview` 预览产物。
业务页面当前为明确标注的占位页面，不提供虚假登录、上传或管理成功结果。页面路由不是后端 API 路径。上线需配置单页应用回退到 index.html。

VITE_ 配置会公开给浏览器，只放 API 地址等公开信息。认证方案尚未接入，不在本框架保存令牌。只请求 /health，/ready 的 503 表示数据库或迁移未就绪。
