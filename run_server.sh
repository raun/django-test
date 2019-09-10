#!/usr/bin/env bash

if [[ -z "$VIRTUAL_ENV" ]]; then
    source ./venv-d1g1t/bin/activate
fi

# Set up the environment variable to run the application
export PROJECT_ENV="dev"

echo "Starting Django development server"
python ./pulse/manage.py runserver
