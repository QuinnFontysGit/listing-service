#!/bin/sh

# Exit on any error
set -e

# Set the Django settings module environment variable
export DJANGO_SETTINGS_MODULE=listingservice.settings

# Ensure the project root (x folder) is in the Python path
export PYTHONPATH=/app:$PYTHONPATH

# Apply database migrations
python manage.py migrate

# Collect static files (if needed)
# python manage.py collectstatic --noinput

# Start Django development server
python manage.py runserver 0.0.0.0:8020 &

# Start the consumer script
python quickstart/consumer.py

# Wait for all background processes to finish
wait
