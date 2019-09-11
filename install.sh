#!/usr/bin/env bash

echo "Checking prerequisites..."
EXIT_CODE=0
if command -v python3.5 &>/dev/null; then
    echo "Python 3.5 exists"
else
    echo "Install Python 3.5 then run install script again"
    EXIT_CODE=1
fi

if pip freeze | grep "virtualenv" > /dev/null; then
    echo "Virtualenv exists"
else
    echo "Install Virtualenv using sudo pip install virtualenv==16.7.4"
    EXIT_CODE=1
fi

if command -v sqlite3 &>/dev/null; then
    echo "Sqlite 3 exists"
else
    echo "Install sqlite3 then run install script again"
    EXIT_CODE=1
fi

if [[ "$EXIT_CODE" -ne "0" ]]; then
    exit 1
fi

if [[ ! -d "venv-d1g1t" ]]; then
	echo "Creating python virtual environment..."
    virtualenv -p python3.5 ./venv-d1g1t/
    echo "Virtual environment created"
fi

if [[ -z "$VIRTUAL_ENV" ]]; then
    source ./venv-d1g1t/bin/activate
    pip install -r ./pulse/requirments.txt
fi

echo "Setting up Pulse"
echo "Migrating the database schema"
python ./pulse/manage.py migrate
echo "Populating Happiness Level"
python ./pulse/manage.py populate_happiness_level
echo "Creating Super User"
python ./pulse/manage.py createsuperuser
echo "Done"
