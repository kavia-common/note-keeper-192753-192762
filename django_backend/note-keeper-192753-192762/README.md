# note-keeper-192753-192762

Backend: Django REST API for Notes

- Endpoints:
  - GET /api/health/ — health check
  - GET /api/notes/ — list notes
  - POST /api/notes/ — create note
  - GET /api/notes/{id}/ — retrieve note
  - PUT/PATCH /api/notes/{id}/ — update note
  - DELETE /api/notes/{id}/ — delete note

## Getting started (django_backend)

1) Prepare environment
- cd django_backend
- cp .env.example .env
- Set database variables in .env to point to your PostgreSQL instance. If not set, the app falls back to SQLite for local development.

2) Install dependencies
- python -m venv .venv && source .venv/bin/activate
- pip install -r requirements.txt

3) Apply migrations
- python manage.py migrate

4) Seed example notes (optional)
- python manage.py seed_notes

5) Run server
- python manage.py runserver 0.0.0.0:3010

6) Explore docs
- Swagger UI: /docs
- Redoc: /redoc

Notes:
- The app automatically uses PostgreSQL if either DATABASE_URL is set or POSTGRES_* env vars are provided.
- Default allowed hosts include localhost/testserver for development.
