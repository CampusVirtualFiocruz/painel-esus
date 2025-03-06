import os

from dotenv import dotenv_values

env = {
    **dotenv_values(os.path.abspath(".env")),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

def getenv(key, default, numeric=True):
    if key in env:
        if not numeric:
            return str(env[key].strip())
        return int(env[key].strip())
    return default
