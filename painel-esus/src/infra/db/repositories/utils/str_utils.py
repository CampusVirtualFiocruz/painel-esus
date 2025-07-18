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
    return mock_word( data, 3, True)

def anonymize_data_frame( data):
    mock = getenv("MOCK", False, False) == "True"
    if not mock:
        return data

    columns = [
        "cpf",
        "cns",
        "nome",
        "telefone",
        "endereco",
        "numero",
        "cep",
        "complemento",
        "bairro",
        "nome_unidade_saude",
        "nome_equipe",
        "logradouro",
        "municipio",
        "cnes_equipe",
        "telefone",
        "micro_area",
        "ine_equipe",
        "data_nascimento",
    ]
    for col in columns:
        if col in data:
            data[col] = anonymize_data(str(data[col]))
    return data
