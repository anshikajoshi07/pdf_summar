Render deployment guide

1) Create a Render account and link your GitHub repo `anshikajoshi07/pdf_summari`.

2) Add a Managed PostgreSQL service named `pdf-summar-db` (or use `render.yaml` to create it automatically).
   - Save the `DATABASE_URL` value that Render provides for the DB.

3) Create a Web Service (or let Render create it from `render.yaml`) with:
   - Build command: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   - Start command: gunicorn pdf_summari.wsgi:application

4) Set environment variables on the Render Web Service:
   - SECRET_KEY (set a strong secret)
   - DEBUG = False
   - ALLOWED_HOSTS = yourdomain.com (or leave blank to set via Render)
   - DATABASE_URL (Render-managed Postgres will set this automatically)

5) Enable auto-deploy from the GitHub repository. Pushes to `main` will trigger a build.

6) (Optional) If you want the GitHub Actions workflow in this repo to trigger a deploy, add secrets:
   - RENDER_API_KEY
   - RENDER_SERVICE_ID

Notes:
- The repo includes `requirements.txt`, `Procfile`, and `render.yaml`.
- The app uses `dj-database-url` to parse `DATABASE_URL` in `settings.py`.
- Ensure static files are served using Whitenoise; `STATIC_ROOT` and `STATICFILES_STORAGE` are configured.
