# 接口契约

openapi.json只列当前可运行的健康检查。生成方式：在backend运行 Python，导入app.main.app并将app.openapi()以JSON写入../contracts/openapi.json。业务目标先评审再新增，不把设计文档当作已上线接口。
