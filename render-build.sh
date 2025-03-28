#!/usr/bin/env bash
# Install dependencies, apply migrations, and collect static files

echo "▶ Installing dependencies..."
pip install -r requirements.txt

echo "▶ Running Django migrations..."
python manage.py migrate

echo "▶ Collecting static files..."
python manage.py collectstatic --noinput
