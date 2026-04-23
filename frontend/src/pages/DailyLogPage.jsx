import { useState } from "react";

import { api } from "../services/api";

const TODAY = new Date().toISOString().slice(0, 10);

export default function DailyLogPage() {
  const [message, setMessage] = useState("");
  const [formData, setFormData] = useState({
    user_id: "",
    log_date: TODAY,
    mood: 3,
    energy: 3,
    stress: 3,
    mental_clarity: 3,
    notes: "",
    daily_score: 50,
  });

  const onChange = (event) => {
    const { name, value } = event.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const onSubmit = async (event) => {
    event.preventDefault();
    setMessage("");

    try {
      await api.createDailyLog({
        ...formData,
        mood: Number(formData.mood),
        energy: Number(formData.energy),
        stress: Number(formData.stress),
        mental_clarity: Number(formData.mental_clarity),
        daily_score: Number(formData.daily_score),
      });
      setMessage("Registro guardado correctamente.");
    } catch {
      setMessage("No se pudo guardar. Verifica user_id y backend activo.");
    }
  };

  return (
    <section>
      <h2>Registro diario</h2>
      <form className="log-form" onSubmit={onSubmit}>
        <label>
          User ID
          <input name="user_id" value={formData.user_id} onChange={onChange} required />
        </label>
        <label>
          Fecha
          <input type="date" name="log_date" value={formData.log_date} onChange={onChange} required />
        </label>
        <label>
          Mood (1-5)
          <input type="number" name="mood" min="1" max="5" value={formData.mood} onChange={onChange} />
        </label>
        <label>
          Energía (1-5)
          <input type="number" name="energy" min="1" max="5" value={formData.energy} onChange={onChange} />
        </label>
        <label>
          Stress (1-5)
          <input type="number" name="stress" min="1" max="5" value={formData.stress} onChange={onChange} />
        </label>
        <label>
          Claridad mental (1-5)
          <input
            type="number"
            name="mental_clarity"
            min="1"
            max="5"
            value={formData.mental_clarity}
            onChange={onChange}
          />
        </label>
        <label>
          Score diario
          <input type="number" name="daily_score" min="0" max="100" value={formData.daily_score} onChange={onChange} />
        </label>
        <label>
          Notas
          <textarea name="notes" value={formData.notes} onChange={onChange} />
        </label>
        <button type="submit">Guardar</button>
      </form>
      {message ? <p>{message}</p> : null}
    </section>
  );
}
