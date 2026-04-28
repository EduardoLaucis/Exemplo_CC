"""Configuração ASGI para o projeto Exemplo_CC."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exemplo_cc.settings")

application = get_asgi_application()
