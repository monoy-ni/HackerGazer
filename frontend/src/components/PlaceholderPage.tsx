export function PlaceholderPage({ title, description }: { title: string; description: string }) {
  return <section><span className="badge">待实现</span><h1>{title}</h1><p>{description}</p><p>页面路由已建立，业务接口接入后再完成交互。</p></section>;
}
