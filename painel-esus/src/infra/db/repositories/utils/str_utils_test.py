import src.infra.db.repositories.utils.str_utils as str_utils


def test_anonymize_data():
    name = "Goku Sayajin"
    expected = "Goku *******"

    assert str_utils.anonymize_data_name(name) == expected

def test_anonymize_data_nascimento():
    input = "10/12/2002"
    expected = "**/**/2002"

    assert str_utils.anonymize_data_nascimento(input) == expected

    input = "10-12-2002"
    expected = "**-**-2002"

    assert str_utils.anonymize_data_nascimento(input) == expected

    input = "2002-12-20"
    expected = "2002-**-**"

    assert str_utils.anonymize_data_nascimento(input) == expected

def test_anonymize_data_equipe():
    input = "Equipe 1"
    expected = "****** *"

    assert str_utils.anonymize_data_equipe(input) == expected


def test_anonymize_data_address():
    input = "Equipe 1"
    expected = "****** *"

    assert str_utils.anonymize_data_address(input) == expected


def test_anonymize_data_cep():
    input = "35400-000"
    expected = "****0-000"

    assert str_utils.anonymize_data_cep(input) == expected


def test_anonymize_data_doc():
    input = "35400-000"
    expected = "*****-***"

    assert str_utils.anonymize_data_doc(input) == expected
