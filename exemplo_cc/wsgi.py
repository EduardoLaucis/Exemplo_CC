"""Configuração WSGI para o projeto Exemplo_CC."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exemplo_cc.settings")

application = get_wsgi_application()
