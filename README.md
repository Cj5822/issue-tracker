# Issue Tracker (learning project)

A full-stack learning project for understanding how a React frontend, a FastAPI backend,
and Supabase (PostgreSQL + Auth) fit together.

> Status: project skeleton only. No database, authentication, or issue-tracker features yet.

## Tech stack

| Layer    | Tech                          |
| -------- | ----------------------------- |
| Frontend | React + TypeScript (Vite)     |
| Backend  | FastAPI + Python, managed by uv |
| Database | Supabase PostgreSQL (later)   |
| Auth     | Supabase Auth (later)         |

## Project structure

```
personal-project/
├── frontend/   React + TypeScript app (Vite)
└── backend/    FastAPI app (uv)
```

## Prerequisites

- Node.js 20.19+ or 22.12+ (includes npm)
- [uv](https://docs.astral.sh/uv/) (installs the right Python version for you)

## Running the backend

```bash
cd backend
uv sync                                   # create .venv and install locked dependencies
uv run uvicorn app.main:app --reload      # start the dev server
```

- API: http://127.0.0.1:8000/health
- Interactive docs: http://127.0.0.1:8000/docs

## Running the frontend

```bash
cd frontend
npm install       # install dependencies from package-lock.json
npm run dev       # start the Vite dev server
```

- App: http://localhost:5173
