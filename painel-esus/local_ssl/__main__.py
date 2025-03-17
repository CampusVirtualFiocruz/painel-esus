import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization.pkcs12 import (
    load_key_and_certificates,
)
from OpenSSL.crypto import *
from src.env.conf import env

PATH = env["CERT_PATH"]
CERT_PASSWORD = env["CERT_PASSWORD"]
last_index = PATH.rfind(os.sep)
root_project = PATH[:last_index]

client_cert = f"{PATH}"
certificate_password = CERT_PASSWORD


with open(client_cert, 'rb') as pkcs12_file:  
    pkcs12_data = pkcs12_file.read()  

pkcs12_password_bytes = certificate_password.encode('utf8')  
backend = default_backend()  
py_ca_p12 = load_key_and_certificates(pkcs12_data, pkcs12_password_bytes, backend)  

pkey = py_ca_p12[0].private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)
cert = (
    py_ca_p12[1]
    .public_bytes(
        encoding=serialization.Encoding.PEM,
    )

)


with open( f"{root_project}{os.sep}private-key.pem", 'wb') as file:
    file.write(pkey)
with open(f"{root_project}{os.sep}pcert.pem", "wb") as file:
    file.write(cert)
