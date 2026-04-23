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
    sleep_hours: 7,
    sleep_quality: 3,
    study_topic: "",
    study_real_minutes: 0,
    workout_type: "",
    workout_duration_minutes: 0,
    distraction_type: "",
    distraction_duration_minutes: 0,
  });

  const onChange = (event) => {
    const { name, value } = event.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const onSubmit = async (event) => {
    event.preventDefault();
    setMessage("");

    const payload = {
      user_id: formData.user_id,
      log_date: formData.log_date,
      mood: Number(formData.mood),
      energy: Number(formData.energy),
      stress: Number(formData.stress),
      mental_clarity: Number(formData.mental_clarity),
      notes: formData.notes,
      daily_score: Number(formData.daily_score),
      sleep_log: {
        sleep_hours: Number(formData.sleep_hours),
        sleep_quality: Number(formData.sleep_quality),
      },
      study_sessions: formData.study_topic
        ? [
            {
              topic: formData.study_topic,
              real_minutes: Number(formData.study_real_minutes),
            },
          ]
        : [],
      workouts: formData.workout_type
        ? [
            {
              done: true,
              workout_type: formData.workout_type,
              duration_minutes: Number(formData.workout_duration_minutes),
            },
          ]
        : [],
      distractions: formData.distraction_type
        ? [
            {
              type: formData.distraction_type,
              duration_minutes: Number(formData.distraction_duration_minutes),
            },
          ]
        : [],
    };

    try {
      await api.createDailyLogFull(payload);
      setMessage("Registro completo guardado correctamente.");
    } catch {
      setMessage("No se pudo guardar. Verifica user_id y backend activo.");
    }
  };

  return (
    <section>
      <h2>Registro diario (flujo unificado)</h2>
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
          <input type="number" name="mental_clarity" min="1" max="5" value={formData.mental_clarity} onChange={onChange} />
        </label>
        <label>
          Score diario
          <input type="number" name="daily_score" min="0" max="100" value={formData.daily_score} onChange={onChange} />
        </label>

        <label>
          Sueño (horas)
          <input type="number" name="sleep_hours" min="0" max="24" step="0.5" value={formData.sleep_hours} onChange={onChange} />
        </label>
        <label>
          Calidad de sueño (1-5)
          <input type="number" name="sleep_quality" min="1" max="5" value={formData.sleep_quality} onChange={onChange} />
        </label>

        <label>
          Tema de estudio
          <input name="study_topic" value={formData.study_topic} onChange={onChange} />
        </label>
        <label>
          Minutos de estudio
          <input type="number" name="study_real_minutes" min="0" value={formData.study_real_minutes} onChange={onChange} />
        </label>

        <label>
          Tipo de workout
          <input name="workout_type" value={formData.workout_type} onChange={onChange} />
        </label>
        <label>
          Minutos workout
          <input
            type="number"
            name="workout_duration_minutes"
            min="0"
            value={formData.workout_duration_minutes}
            onChange={onChange}
          />
        </label>

        <label>
          Tipo distracción
          <input name="distraction_type" value={formData.distraction_type} onChange={onChange} />
        </label>
        <label>
          Minutos distracción
          <input
            type="number"
            name="distraction_duration_minutes"
            min="0"
            value={formData.distraction_duration_minutes}
            onChange={onChange}
          />
        </label>

        <label>
          Notas
          <textarea name="notes" value={formData.notes} onChange={onChange} />
        </label>
        <button type="submit">Guardar día completo</button>
      </form>
      {message ? <p>{message}</p> : null}
    </section>
  );
}
