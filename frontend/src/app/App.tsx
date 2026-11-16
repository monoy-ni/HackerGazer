import { Route, Routes } from 'react-router-dom';
import { Layout } from '../components/Layout';
import Marketplace from '../pages/marketplace';
import AppDetail from '../pages/app-detail';
import VersionHistory from '../pages/version-history';
import VersionDetail from '../pages/version-detail';
import Community from '../pages/community';
import Workspace from '../pages/workspace';
import Login from '../pages/login';
import Admin from '../pages/admin';
import { PlaceholderPage } from '../components/PlaceholderPage';
export function App() {
  return <Routes><Route element={<Layout />}>
    <Route index element={<Marketplace />} />
    <Route path="apps/:appId" element={<AppDetail />} />
    <Route path="apps/:appId/releases" element={<VersionHistory />} />
    <Route path="apps/:appId/releases/:releaseId" element={<VersionDetail />} />
    <Route path="apps/:appId/community" element={<Community />} />
    <Route path="workspace/*" element={<Workspace />} />
    <Route path="login" element={<Login />} />
    <Route path="admin/*" element={<Admin />} />
    <Route path="*" element={<PlaceholderPage title="页面不存在" description="请通过顶部导航返回。" />} />
  </Route></Routes>;
}
