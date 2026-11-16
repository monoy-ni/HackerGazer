// 当前为手工维护的基础服务类型；业务类型须以 contracts/openapi.json 为准。
export interface Health { status: string; service: string; version: string }
export interface Ready { status: string; checks: Record<string, string> }
export interface ErrorEnvelope { code: string; message: string; field_errors: unknown; request_id: string }
