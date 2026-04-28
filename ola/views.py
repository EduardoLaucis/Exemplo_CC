from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, mundo! Bem-vindo ao Exemplo_CC com Django.")
