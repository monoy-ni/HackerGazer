import { useHealth } from '../../hooks/useHealth';
export default function Marketplace() {
  const status = useHealth();
  return <section><span className="badge">框架已就绪</span><h1>发现应用，见证迭代</h1><p>应用市场将在此展示搜索、筛选与应用列表。</p><p role="status">{status}</p></section>;
}
