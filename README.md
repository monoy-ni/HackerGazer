# HackerGazer

前后端协作主仓基础骨架。当前仅提供服务健康检查；业务接口尚未实现。

- frontend：React + TypeScript + Vite 前端工程，含页面路由与统一接口层。
- backend：Python 3.12 / FastAPI，数据库使用 Supabase PostgreSQL。
- contracts：当前可运行接口的 OpenAPI。
- docs：架构、开发、决策和验收说明。

启动与测试见 backend/README.md。无需数据库即可启动 /health；/ready 需有效数据库配置及迁移。不要提交真实凭据。本仓独立于原 HackerGazer，未配置远程地址。

前端启动见 frontend/README.md；前端业务页面目前仅建立路由和占位说明。

项目背景与产品介绍见 [项目概述](docs/project-overview.md)。
