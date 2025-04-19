#!/bin/sh

echo "Waiting for backend to be ready..."
until curl -f http://backend:8000/api/v1/health; do
  echo "Backend is unavailable - sleeping"
  sleep 2
done
echo "Backend is up - starting frontend"

exec npm run dev 