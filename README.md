# Exemplo_CC

Projeto de exemplo criado durante a Formação Claude Code 2026 — IA com Claude e Cowork.

## Sobre

Este repositório demonstra o uso do Claude Code como ferramenta de desenvolvimento assistido por IA, explorando funcionalidades como:

- Criação e edição de arquivos
- Integração com Git e GitHub
- Automação de tarefas de desenvolvimento

## Tecnologias

- Claude Code (CLI)
- Git / GitHub
- Python 3 / Django

## Como usar

```bash
# Clone o repositório
git clone https://github.com/EduardoLaucis/Exemplo_CC.git
cd Exemplo_CC

# Crie e ative um ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Rode o servidor de desenvolvimento
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` para ver a página inicial.

## Estrutura

- `manage.py` — utilitário do Django
- `exemplo_cc/` — configurações do projeto (settings, urls, wsgi)
- `ola/` — app simples com uma view "Olá, mundo!"

## Licença

Este projeto é de uso educacional.
