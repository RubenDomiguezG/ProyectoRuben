const API_BASE_URL = "http://localhost:8000/api/v1";

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || `Error ${response.status}`);
  }

  if (response.status === 204) return null;
  return response.json();
}

export const api = {
  listDailyLogs: () => request("/daily-logs/"),
  createDailyLog: (payload) => request("/daily-logs/", { method: "POST", body: JSON.stringify(payload) }),
  listSleepLogs: () => request("/sleep-logs/"),
  listStudySessions: () => request("/study-sessions/"),
  listWorkouts: () => request("/workouts/"),
  listDistractions: () => request("/distractions/"),
};
