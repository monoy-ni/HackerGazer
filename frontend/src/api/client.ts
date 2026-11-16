import type { ErrorEnvelope } from '../types/api';
const baseUrl = (import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000').replace(/\/$/, '');
export class ApiError extends Error {
  constructor(public status: number, public detail: ErrorEnvelope) { super(detail.message); }
}
// 不自动重试写请求；调用者可通过 signal 取消请求。认证方式确认后在此统一接入。
export async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const response = await fetch(`${baseUrl}${path}`, { ...options, cache: 'no-store' });
  if (!response.ok) {
    let detail: Partial<ErrorEnvelope> = {};
    try { detail = await response.json(); } catch { /* 非 JSON 错误使用统一提示 */ }
    throw new ApiError(response.status, {
      code: detail.code || 'HTTP_ERROR', message: detail.message || `请求失败（${response.status}）`,
      field_errors: detail.field_errors ?? {}, request_id: detail.request_id || response.headers.get('X-Request-ID') || '',
    });
  }
  if (response.status === 204) return undefined as T;
  return response.json() as Promise<T>;
}
