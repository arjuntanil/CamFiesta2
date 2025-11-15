"""
WSGI config for camfiesta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'camfiesta.production')

application = get_wsgi_application()

# Add whitenoise middleware for static files
from whitenoise import WhiteNoise
application = WhiteNoise(application)
application.add_files('staticfiles', prefix='static/')
