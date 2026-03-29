"""
WSGI config for carteira_pet project.
PJI110 - UNIVESP 2026

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carteira_pet.settings')

application = get_wsgi_application()