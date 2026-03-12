#!/bin/bash
set -e

echo "Waiting for MySQL to be ready..."

# Wait until MySQL is ready
until nc -z mysql_db 3306; do
  echo "MySQL is unavailable - sleeping"
  sleep 1
done

echo "MySQL started!"

echo "Applying database migrations..."

# Apply migrations automatically
python manage.py migrate --noinput

echo "Collecting static files..."

# Optional but recommended
python manage.py collectstatic --noinput || true

echo "Starting Django server..."

# Start Django
python manage.py runserver 0.0.0.0:8000