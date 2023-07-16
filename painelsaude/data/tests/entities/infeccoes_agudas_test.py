from ...entities.infeccoes_agudas import AcuteInfectionsCollection
from mock.mock import patch, mock_open

def test_infecoes_agudas_singleton(mock_open):
    infeccoes_collection = AcuteInfectionsCollection()
    assert len(infeccoes_collection.list) > 0
    
@patch('builtins.open',new_callable=mock_open, read_data="data")
def test_infecoes_agudas_singleton(mock_open):
    infeccoes_collection = AcuteInfectionsCollection()
    infeccoes_collection2 = AcuteInfectionsCollection()
    infeccoes_collection3 = AcuteInfectionsCollection()
    # assert len(infeccoes_collection.list) > 0
    assert mock_open.call_count == 1