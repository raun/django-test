from .base import *

from pulse.pulse.project_settings.base import get_env_variable

DEBUG = False
SECRET_KEY = '--hg(fb6pc5fpk#1)aqe200&5!4ezy)7$z%xi^q_^m9w(#oeq%'

DB_USER = get_env_variable('DB_USER')
DB_PASS = get_env_variable('DB_PASS')
DB_NAME = get_env_variable('DB_NAME', 'django_pulse')
DB_HOST = get_env_variable('DB_HOST', '127.0.0.1')
DB_PORT = get_env_variable('DB_PORT', '')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': DB_PORT,  # Set to empty string for default.
    }
}
