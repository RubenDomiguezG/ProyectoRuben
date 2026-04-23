# ProyectoRuben - MVP monitoreo de rendimiento y hábitos

## 1) Estructura de carpetas recomendada

```text
backend/
  app/
    api/
    core/
    crud/
    db/
    models/
    schemas/
    main.py
  sql/
    schema.sql
  requirements.txt
  .env.example
frontend/
  src/
    components/
    pages/
    services/
    App.jsx
    main.jsx
    styles.css
  package.json
```

## 2) Plan breve de implementación
1. **Backend base (FastAPI):** app principal, configuración por variables de entorno, sesión DB.
2. **PostgreSQL:** conexión y schema SQL equivalente al diseño base.
3. **Modelos y esquemas:** SQLAlchemy + Pydantic para validaciones.
4. **CRUD mínimos:** endpoints para users, daily_logs, sleep_logs, study_sessions, workouts y distractions.
5. **Frontend base:** páginas Dashboard, Registro diario e Historial.
6. **Conexión frontend-backend:** servicio API y consumo real de endpoints.

## 3) Archivos iniciales creados (MVP)
- Backend: `main.py`, `core/config.py`, `db/session.py`, modelos ORM, schemas Pydantic, CRUD y routers REST.
- Frontend: `App.jsx`, `services/api.js`, páginas y componente KPI para dashboard.
- SQL: `backend/sql/schema.sql`.

---

## Requisitos
- Python 3.10+
- Node 18+
- PostgreSQL 14+

## Ejecutar local

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```


## Flujo principal recomendado en frontend
- **Principal**: `POST /api/v1/daily-logs/full` para registrar un día completo en una sola operación.
- **Consulta agregada**: `GET /api/v1/daily-logs/full/{log_id}` y `GET /api/v1/daily-logs/full/by-date/{log_date}`.
- **CRUD individuales** se mantienen para mantenimiento/edición puntual por recurso.

## Endpoints CRUD disponibles (v1)
- `/api/v1/users`
- `/api/v1/daily-logs`
- `/api/v1/sleep-logs`
- `/api/v1/study-sessions`
- `/api/v1/workouts`
- `/api/v1/distractions`

## Notas MVP
- Sin autenticación avanzada.
- Sin IA/recomendaciones automáticas.
- Arquitectura simple para crecer luego hacia analítica/predicción.
