#!/bin/bash
# Activate the virtual environment
source /home/ubuntu/satisactual/.venv/bin/activate

# Start Django server
exec python manage.py runserver 0.0.0.0:8003
