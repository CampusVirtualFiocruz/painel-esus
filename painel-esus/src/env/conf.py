import os

from dotenv import dotenv_values

VERSION_PAINEL = "${VERSION}"

env = {
    **dotenv_values(os.path.abspath(".env")),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
    "APPLICATION_VERSION": VERSION_PAINEL,
}

def getenv(key, default, numeric=True):
    if key in env:
        if not numeric:
            return str(env[key].strip())
        return int(env[key].strip())
    return default

def is_installed_ok():
    try:
        return (
            env["DB_HOST"] is not None
            and env["DB_DATABASE"] is not None
            and env["DB_USER"] is not None
            and env["DB_PASSWORD"] is not None
            and env["DB_PORT"] is not None
            and env["CIDADE_IBGE"] is not None
            and env["ADMIN_USERNAME"] is not None
            and env["ADMIN_PASSWORD"] is not None
            and env["ADMIN_EMAIL"] is not None
            and env["ADMIN_NAME"] is not None
            and env["BRIDGE_LOGIN_URL"] is not None
        ), {
            "DB_HOST": env["DB_HOST"],
            "DB_DATABASE": env["DB_DATABASE"],
            "DB_USER": env["DB_USER"],
            "DB_PASSWORD": env["DB_PASSWORD"],
            "DB_PORT": env["DB_PORT"],
            "CIDADE_IBGE": env["CIDADE_IBGE"],
            "ADMIN_USERNAME": env["ADMIN_USERNAME"],
            "ADMIN_PASSWORD": env["ADMIN_PASSWORD"],
            "ADMIN_EMAIL": env["ADMIN_EMAIL"],
            "ADMIN_NAME": env["ADMIN_NAME"],
            "BRIDGE_LOGIN_URL": env["BRIDGE_LOGIN_URL"],
        }
    except:
        return (False, 
            {
                "DB_HOST": env.get("DB_HOST", ""),
                "DB_DATABASE": env.get("DB_DATABASE", ""),
                "DB_USER": env.get("DB_USER", ""),
                "DB_PASSWORD": env.get("DB_PASSWORD", ""),
                "DB_PORT": env.get("DB_PORT", ""),
                "CIDADE_IBGE": env.get("CIDADE_IBGE", ""),
                "ADMIN_USERNAME": env.get("ADMIN_USERNAME", ""),
                "ADMIN_PASSWORD": env.get("ADMIN_PASSWORD", ""),
                "ADMIN_EMAIL": env.get("ADMIN_EMAIL", ""),
                "ADMIN_NAME": env.get("ADMIN_NAME", ""),
                "BRIDGE_LOGIN_URL": env.get("BRIDGE_LOGIN_URL", ""),
            })
