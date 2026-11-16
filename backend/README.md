# 后端基础骨架

使用 Python 3.12，在 backend 目录运行：

```powershell
python -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.lock.txt
Copy-Item .env.example .env
./.venv/Scripts/python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --no-access-log
```

打开 /health、/ready、/docs。健康检查无需数据库；就绪检查需有效配置及迁移。配置文件只有模板，没有任何真实密码。

填写本机 Supabase 连接参数后才执行 `.venv/Scripts/python.exe -m alembic upgrade head`。选择独立开发项目，不将本初始化迁移用于已有业务库；当前迁移仅建立框架版本记录，无业务表。连接SSL默认verify-full，使用匹配主机名与受信CA；必要时配置CA路径。连接方式按部署网络与Supabase项目提供的Connect参数选择。

测试：`.venv/Scripts/python.exe -m pytest -q`。基础测试不连接真实数据库，不需要远程凭据。

日志：收集hackergazer.requests，级别INFO；生产代理不能记录查询串或认证头。尚未选择认证和文件存储服务，相关业务接口未实现。
