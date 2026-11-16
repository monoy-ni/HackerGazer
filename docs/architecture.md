# 架构

前端调用FastAPI，后端通过受限服务端身份连接Supabase PostgreSQL。业务写入在服务层的单一数据库事务中完成；不把多个HTTP请求当事务。文件存储及扫描通过独立适配接入，尚未实现。前端不持有数据库连接或服务端密钥。若开启Supabase Data API，必须单独配置schema、grants及RLS，不能依赖高权限身份自动受保护。
