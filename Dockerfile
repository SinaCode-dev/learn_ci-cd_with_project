FROM python:3.12-slim
RUN adduser --system --group --quiet --no-create-home app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
RUN chown app:app /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
RUN mkdir -p /app/media && chown -R app:app /app/media
USER app
CMD ["sh", "-c", "if [ \"$ENV_MODE\" = \"prod\" ]; then gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3; else python manage.py runserver 0.0.0.0:8000; fi"]