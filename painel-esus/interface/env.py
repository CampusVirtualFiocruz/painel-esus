ENV = [
    {
        "section": "Banco de Dados.",
        "visible": True,
        "values": [
            {
                "name": "DB_HOST",
                "label": "Host:",
            },
            {
                "name": "DB_DATABASE",
                "label": "Base de dados:",
            },
            {
                "name": "DB_USER",
                "label": "Usuário do banco de dados:",
            },
            {
                "name": "DB_PASSWORD",
                "label": "Senha do banco de dados:",
            },
            {
                "name": "DB_PORT",
                "label": "Porta do banco de dados:",
            },
        ],
    },
    {
        "section": "Painel E-sus.",
        "visible": True,
        "values": [
            {
                "name": "CIDADE_IBGE",
                "label": "Código IBGE da Cidade:",
            },
            {
                "name": "ADMIN_USERNAME",
                "label": "Usuário de acesso ao painel-esus:",
            },
            {
                "name": "ADMIN_PASSWORD",
                "label": "Senha de acesso ao painel-esus:",
            },
            {
                "name": "BRIDGE_LOGIN_URL",
                "label": "Url de login:",
            },
            {
                "name": "RELOAD_BASE_SCHELDULE",
            },
            {"name": "PRIVATE_KEY", "label": "Chave privada (server.key):"},
            {"name": "CERTIFICATE", "label": "Certificado (server.crt):"},
            {"name": "PORT"},
        ],
    },
    {
        "section": "Configurações internas.",
        "visible": "False",
        "values": [
            {
                "name": "PASSWORD_SALT",
                "default": "painel",
            },
            {
                "name": "ARTEFACT",
                "default": "instalador",
            },
            {
                "name": "ENV",
                "default": "instalador",
            },
            {
                "name": "SECRET_TOKEN",
                "default": "111111111111111111111",
            },
            {
                "name": "GENERATE_BASE",
                "default": "True",
            },
            {
                "name": "CHUNK_SIZE",
                "default": "50000",
            },
            {
                "name": "POLARS_SKIP_CPU_CHECK",
                "default": "True",
            },
            {
                "name": "LOG_API",
                "default": "https://painel-logs.painelsaude.info",
            },
            {
                "name": "APPLICATION_VERSION",
                "default": "0.9.2",
            },        
        ],
    },
    {
    "section": "Configurações avançadas.",
    "visible": "False",
    "values": []
    }
]
