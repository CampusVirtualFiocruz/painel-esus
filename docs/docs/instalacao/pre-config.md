---
sidebar_position: 1
---

# Pré-configurações

## Requisitos

- Python 3.10
- Docker
- *OpenVPN client (recomenda-se Pritunl)

## Preparando o ambiente

- *Conectar VPN.

- Criar `.env` no diretório do back-end.
    - `cp painel-esus/.example.env painel-esus/.env`

- Caso queira inicializar o front-end localmente, atualize o Dockerfile comentando os comandos referentes ao front-end.
    - `# RUN mkdir paineis-v2-front`
    - `# COPY ./paineis-v2-front/static-files ./paineis-v2-front/static-files`

- Se necessário, atualize o `.env` para não fazer build da base.
    - `GENERATE_BASE=False`

- Se necessário, atualize `.dockerignore` comentando o glob pattern `**/.env`.

> *Para acesso ao banco de dados remoto.
