# Deploying pdf_summari

## Push to GitHub

Option A — Using GitHub CLI (recommended):

1. Create the repo and push:

```bash
# from project root
gh repo create <your-username>/pdf_summari --public --source=. --remote=origin --push
```

Option B — Manually via GitHub website:

1. Create an empty repo on GitHub.
2. Add remote and push:

```bash
git remote add origin git@github.com:<your-username>/pdf_summari.git
git branch -M main
git push -u origin main
```

## CI (GitHub Actions)
A basic workflow is included at `.github/workflows/python-app.yml` that runs tests on push and pull requests to `main`.

## Deploy to Render (recommended)
1. Create a new Web Service on Render and connect your GitHub repo.
2. Build command (Render uses `pip` automatically):
   - `pip install -r requirements.txt`
3. Start command:
   - `gunicorn pdf_summari.wsgi --log-file -`
4. Environment variables to set in Render:
   - `SECRET_KEY`
   - `DEBUG=false`
   - `ALLOWED_HOSTS=<your-domain.com>` (comma-separated)
   - `DATABASE_URL` (set if using Postgres)
5. After deploy, run one-off commands on Render to apply migrations and collect static:
   - `python manage.py migrate --noinput`
   - `python manage.py collectstatic --noinput`

## Deploy to Railway
1. Connect your GitHub repo in Railway, set the environment variables listed above, and set the start command to `gunicorn pdf_summari.wsgi --log-file -`.

## Notes
- Keep `SECRET_KEY` out of the repo; store it only in host environment variables.
- For production database use Postgres and set `DATABASE_URL` accordingly.
- The project uses WhiteNoise to serve static files in production.
