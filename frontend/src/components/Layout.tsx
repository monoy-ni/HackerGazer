import { NavLink, Outlet } from 'react-router-dom';
export function Layout() {
  return <><header><strong>HackerGazer</strong><nav><NavLink to="/">应用市场</NavLink><NavLink to="/workspace">开发者工作台</NavLink><NavLink to="/admin">管理后台</NavLink><NavLink to="/login">登录</NavLink></nav></header><main><Outlet /></main><footer>项目基础框架 · 业务功能正在建设中</footer></>;
}
