import re

from src.env.conf import getenv


def mock_word(phrase, gap=2, skip_first=False):
    mock = getenv("MOCK", False, False) == "True"
    if not mock or phrase == "" or phrase is None:
        return phrase
    words = phrase.split()
    if skip_first and len(words)>1:
        return " ".join(
            [
                words[0],
                *[
                    word[:gap] + "".join(["*" for n in word[gap:]])
                    for word in words[1:]
                ],
            ]
        )
    else:
        return " ".join(
            [word[:gap] + "".join(["*" for n in word[gap:]]) for word in words]
        )

def anonymize_data( data:str ) ->str:
    mock = getenv("MOCK", False, False) == "True"
    if not mock:
        return data
    return mock_word( data, 4, True)


def anonymize_data_name(data: str) -> str:
    mock = getenv("MOCK", False, False) == "True"
    if not mock:
        return data
    return mock_word(data, 0, True)


def anonymize_data_frame( data):
    mock = getenv("MOCK", False, False) == "True"
    if not mock:
        return data

    columns = [
        ("cpf", anonymize_data_doc),
        ("cns", anonymize_data_doc),
        ("nome", anonymize_data_name),
        ("telefone", anonymize_data),
        ("endereco", anonymize_data_address),
        ("numero", anonymize_data),
        ("cep", anonymize_data_cep),
        ("complemento", anonymize_data),
        ("bairro", anonymize_data),
        ("nome_unidade_saude", anonymize_data_equipe),
        ("nome_equipe", anonymize_data_equipe),
        ("logradouro", anonymize_data_equipe),
        ("municipio", anonymize_data_equipe),
        ("cnes_equipe", anonymize_data_equipe),
        ("telefone", anonymize_data),
        ("micro_area", anonymize_data),
        ("ine_equipe", anonymize_data_equipe),
        ("data_nascimento", anonymize_data_nascimento),
    ]
    for col in columns:
        if col[0] in data:
            data[col[0]] = col[1](str(data[col[0]]))
    return data

def anonymize_data_nascimento(data):
    data = str(data).split(" ")[0]
    sep = "/" if "/" in data else "-"
    input_data = data.split(sep)
    response = []
    for data in input_data:
        if len(data) == 2:
            response.append('**')
        else:
            response.append(data)
    return sep.join(response)

def anonymize_data_equipe(data):
    return mock_word(data, 0, False)

def anonymize_data_address(data):
    return mock_word(data, 0, False)

def anonymize_data_cep(data):
    return f"****{str(data)[4:]}"


def anonymize_data_doc(data):
    return re.sub(r'[0-9+]','*', str(data))
