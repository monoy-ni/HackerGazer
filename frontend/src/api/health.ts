import { request } from './client';
import type { Health } from '../types/api';
export const getHealth = (signal?: AbortSignal) => request<Health>('/health', { signal });
