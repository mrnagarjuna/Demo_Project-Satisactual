#!/bin/bash
set -e

echo "Waiting for MySQL to be ready..."

# Wait until MySQL is ready
until nc -z -v -w30 mysql_db 3306
do
  echo "Waiting 1s..."
  sleep 1
done

echo "MySQL started!"

# Run migrations
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files (optional for production)
# python manage.py collectstatic --noinput

# Start Django server
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000