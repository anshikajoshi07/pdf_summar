# Deploying to Render (example)

This file shows a minimal set of steps to deploy the `pdf_summari` Django app to Render.com as a Web Service.

1. Connect your GitHub repo to Render and create a **Web Service**.

2. Use the following build and start commands (these are also included in `render.yaml` and `Procfile` in the repo):

   - Build command: `pip install -r requirements.txt`
   - Start command: `python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn pdf_summari.wsgi:application --bind 0.0.0.0:$PORT`

3. Set environment variables in Render (Environment -> Environment Variables):
   - `SECRET_KEY` — set to a secure random secret. Do NOT commit it.
   - `DEBUG` — set to `False` in production.
   - `ALLOWED_HOSTS` — set to your domain(s) (comma-separated), e.g. `example.com,www.example.com`.

4. Make sure `requirements.txt` contains `gunicorn` (it does) and `whitenoise` is installed (already in `settings.py` middleware). Render will run the start command after building.

5. After deployment: check Render logs for any errors; if static files do not appear, verify `collectstatic` ran successfully.

Notes
- If you prefer not to use `render.yaml`, you can set the start/build commands in the Render dashboard manually.
- If you previously used GitHub Pages for this repo, remove GitHub Pages publishing (Settings → Pages) to prevent the repo from showing the README as a static site.

If you'd like, I can also add a minimal `Dockerfile` or prepare a Heroku-ready `Procfile` variant; tell me which one you prefer next.