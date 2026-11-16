import { useEffect, useState } from 'react';
import { getHealth } from '../api/health';
export function useHealth() {
  const [status, setStatus] = useState('正在检查后端连接…');
  useEffect(() => {
    const controller = new AbortController();
    getHealth(controller.signal).then(data => setStatus(`${data.service} 服务在线 · ${data.version}`))
      .catch(() => { if (!controller.signal.aborted) setStatus('后端暂未连接，请先启动后端服务。'); });
    return () => controller.abort();
  }, []);
  return status;
}
