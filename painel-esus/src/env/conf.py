import os

from dotenv import dotenv_values, load_dotenv

env = {
    **dotenv_values(".env"),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}
