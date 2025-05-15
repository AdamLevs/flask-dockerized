#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done

echo "Initializing database..."
flask --app flaskr init-db
flask --app flaskr init-demo

echo "Starting Flask..."
exec "$@"