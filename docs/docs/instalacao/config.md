---
sidebar_position: 2
---

# Configurações

## Backend

### Docker

- Faça o build da imagem
    - `docker build -t painel-esus-flask .`

- Inicie o container
    - `docker run -d -p 5001:5001 --name painel-esus-flask-container painel-esus-flask`

    - Se preferir, use volume:
        - `docker run -d -v <PATH>/painel-esus/painel-esus:/app" -w /app -e FLASK_ENV=development -p 5001:5001 --name painel-esus-flask-vol painel-esus-flask python run.py`

## Frontend

- `cd paineis-v2-front && yarn`
- `yarn start`

## Documentação

- Desenvolvimento
    - `cd docs && yarn`
    - `yarn start`

- Build
    - `yarn build`
