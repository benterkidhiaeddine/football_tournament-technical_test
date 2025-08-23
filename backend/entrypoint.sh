#!/bin/sh

# Wait for PostgreSQL to be available
while ! nc -z db 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

# Apply database migrations
python3 manage.py migrate

# Start the Django application
exec python3 manage.py runserver 0.0.0.0:8000