from __future__ import absolute_import
from django.core.exceptions import ImproperlyConfigured

from .project_settings.base import get_env_variable

PROJECT_ENV = get_env_variable("PROJECT_ENV")

if PROJECT_ENV == 'dev':
    from .project_settings.dev import *
elif PROJECT_ENV == 'prod':
    from .project_settings.prod import *
elif PROJECT_ENV == 'test':
    from .project_settings.test import *
else:
    error_msg = "Unidentified PROJECT_ENV. Please define the PROJECT_ENV as either dev or prod"
    raise ImproperlyConfigured(error_msg)
