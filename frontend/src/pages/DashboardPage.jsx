import { useEffect, useMemo, useState } from "react";
import { CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

import KpiCard from "../components/KpiCard";
import { api } from "../services/api";

export default function DashboardPage() {
  const [dailyLogs, setDailyLogs] = useState([]);
  const [sleepLogs, setSleepLogs] = useState([]);
  const [studySessions, setStudySessions] = useState([]);
  const [distractions, setDistractions] = useState([]);

  useEffect(() => {
    Promise.all([api.listDailyLogs(), api.listSleepLogs(), api.listStudySessions(), api.listDistractions()])
      .then(([daily, sleep, study, distraction]) => {
        setDailyLogs(daily);
        setSleepLogs(sleep);
        setStudySessions(study);
        setDistractions(distraction);
      })
      .catch(() => {
        setDailyLogs([]);
      });
  }, []);

  const chartData = useMemo(() => {
    return [...dailyLogs]
      .sort((a, b) => new Date(a.log_date) - new Date(b.log_date))
      .slice(-7)
      .map((log) => {
        const sleep = sleepLogs.find((item) => item.daily_log_id === log.id);
        const studyMinutes = studySessions
          .filter((item) => item.daily_log_id === log.id)
          .reduce((acc, item) => acc + (item.real_minutes || 0), 0);
        const distractionMinutes = distractions
          .filter((item) => item.daily_log_id === log.id)
          .reduce((acc, item) => acc + (item.duration_minutes || 0), 0);

        return {
          date: log.log_date,
          score: Number(log.daily_score || 0),
          sleep_hours: Number(sleep?.sleep_hours || 0),
          study_minutes: studyMinutes,
          distraction_minutes: distractionMinutes,
        };
      });
  }, [dailyLogs, sleepLogs, studySessions, distractions]);

  const today = dailyLogs.find((item) => item.log_date === new Date().toISOString().slice(0, 10));

  return (
    <section>
      <h2>Dashboard</h2>
      <p>Score de hoy, tendencia semanal y relación simple entre variables.</p>

      <div className="kpi-grid">
        <KpiCard label="Score hoy" value={today?.daily_score ?? "N/A"} />
        <KpiCard label="Registros" value={dailyLogs.length} />
        <KpiCard
          label="Distracción media (7d)"
          value={
            chartData.length
              ? `${Math.round(chartData.reduce((acc, d) => acc + d.distraction_minutes, 0) / chartData.length)} min`
              : "N/A"
          }
        />
      </div>

      <div className="chart-card">
        <h3>Tendencia semanal</h3>
        <ResponsiveContainer width="100%" height={280}>
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="score" stroke="#2563eb" name="Score" />
            <Line type="monotone" dataKey="sleep_hours" stroke="#059669" name="Sueño (h)" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </section>
  );
}
