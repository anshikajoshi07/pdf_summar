# pdf_summari

A simple Django app for PDF summarization.

## Local setup

1. Create and activate a Python virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` from `.env.example` and set `SECRET_KEY` and other env vars as needed.

4. Run migrations and start the dev server:

```bash
python manage.py migrate
python manage.py runserver
```

## Deploy
See `DEPLOY_TO_RENDER.md` for a sample Render deployment guide and instructions.
