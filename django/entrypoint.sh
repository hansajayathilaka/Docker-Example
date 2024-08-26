#!/bin/sh

# Apply database migrations
python manage.py migrate

# Start the Django production server
gunicorn setup.wsgi:application --bind 0.0.0.0:${PORT} \
    --workers 3 \
    --log-level=info \
    --access-logfile - \
    --error-logfile - \
    --timeout 90 \
    --graceful-timeout 10 \
    --keep-alive 5 \
    --max-requests 1000 \
    --max-requests-jitter 50 \
    --preload
