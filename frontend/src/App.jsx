import { Link, Route, Routes } from "react-router-dom";

import DashboardPage from "./pages/DashboardPage";
import DailyLogPage from "./pages/DailyLogPage";
import HistoryPage from "./pages/HistoryPage";

export default function App() {
  return (
    <div className="layout">
      <nav>
        <h1>Performance Tracker</h1>
        <div className="nav-links">
          <Link to="/">Dashboard</Link>
          <Link to="/daily-log">Registro diario</Link>
          <Link to="/history">Historial</Link>
        </div>
      </nav>
      <main>
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/daily-log" element={<DailyLogPage />} />
          <Route path="/history" element={<HistoryPage />} />
        </Routes>
      </main>
    </div>
  );
}
