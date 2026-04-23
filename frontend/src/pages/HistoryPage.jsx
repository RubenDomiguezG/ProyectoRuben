import { useEffect, useState } from "react";

import { api } from "../services/api";

export default function HistoryPage() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    api.listDailyLogs().then(setLogs).catch(() => setLogs([]));
  }, []);

  return (
    <section>
      <h2>Historial</h2>
      <ul className="history-list">
        {logs.map((log) => (
          <li key={log.id}>
            <strong>{log.log_date}</strong> — Score: {log.daily_score ?? "N/A"} — Mood: {log.mood ?? "N/A"}
          </li>
        ))}
      </ul>
    </section>
  );
}
