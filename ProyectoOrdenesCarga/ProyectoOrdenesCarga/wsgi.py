"""
WSGI config for ProyectoOrdenesCarga project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoOrdenesCarga.settings')

application = get_wsgi_application()

from whitenoise import WhiteNoise

application = WhiteNoise(application, root='/ProyectoOrdenesCarga/static/')
#application.add_files('ProyectoOrdenesCarga/static/', prefix='/static/')

