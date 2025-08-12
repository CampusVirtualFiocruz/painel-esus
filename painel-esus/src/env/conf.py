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