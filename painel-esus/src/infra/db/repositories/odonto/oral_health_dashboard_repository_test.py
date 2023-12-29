# pylint: disable=C0301
from unittest import mock

from src.infra.db.repositories.odonto.oral_health_dashboard_repository import \
    OralHealthDashboardRepository


# @pytest.mark.skip('avoid hit db')
def test_get_total():
    repo = OralHealthDashboardRepository()
    total = repo.get_total()
    print('total', total)
    assert total > 0
    total_cnes = repo.get_total(56)
    assert total_cnes > 0

    assert total > total_cnes


@mock.patch(
    'src.infra.db.repositories.odonto.oral_health_dashboard_repository.OralHealthDashboardRepository'
)
def test_get_total_mock(repository):
    repository.get_total.return_value = 123
    total = repository.get_total()
    assert total == 123


def test_get_cares_by_line_of_service():
    repo = OralHealthDashboardRepository()
    total = repo.get_cares_by_line_of_services()
    print(total)
    assert total['total'].iloc[0] > 0
    assert total['gestantes'].iloc[0] > 0
    assert total['especiais'].iloc[0] > 0
    assert total['total'].iloc[0] > total['gestantes'].iloc[0]
    assert total['total'].iloc[0] > total['especiais'].iloc[0]


def test_get_cares_by_type_of_services():
    repo = OralHealthDashboardRepository()
    total = repo.get_cares_by_type_of_services()
    print(total.to_dict(orient='records'))
    assert total.shape[0] > 0
    assert any(total['ds_tipo_consulta_odonto'] ==
               'Consulta de manutenção em odontologia')
    assert any(total['ds_tipo_consulta_odonto'] ==
               'Consulta de retorno em odontologia')


def test_get_extraction_procedures_proportion():
    repo = OralHealthDashboardRepository()
    total = repo.get_extraction_procedures_proportion()

    assert total['total_dente_deciduo'].iloc[0] > 0
    assert total['total_dente_permanente'].iloc[0] > 0
    assert total['total_outros'].iloc[0] > 0

    total_cnes = repo.get_extraction_procedures_proportion(56)

    assert total_cnes['total_dente_deciduo'].iloc[0] > 0
    assert total_cnes['total_dente_permanente'].iloc[0] > 0
    assert total_cnes['total_outros'].iloc[0] > 0

    assert \
        total['total_dente_deciduo'].iloc[0] > total_cnes['total_dente_deciduo'].iloc[0]
    assert \
        total['total_dente_permanente'].iloc[0] > total_cnes['total_dente_permanente'].iloc[0]
    assert \
        total['total_outros'].iloc[0] > total_cnes['total_outros'].iloc[0]


def test_get_oral_health_cares_by_gender():
    repo = OralHealthDashboardRepository()
    total = repo.get_oral_health_cares_by_gender()

    print(total)


def test_get_oral_health_cares_by_age_range():
    repo = OralHealthDashboardRepository()
    total = repo.get_oral_health_cares_by_age_range()

    print(total)


def test_get_oral_health_cares_by_place():
    repo = OralHealthDashboardRepository()
    total = repo.get_oral_health_cares_by_place()

    print(total)


def test_get_oral_health_cares_by_outcome():
    repo = OralHealthDashboardRepository()
    total = repo.get_oral_health_cares_by_outcome()
    print(total)
    assert any(total['label'] == 'Agendamento para NASF')
    assert any(total['label'] == 'Agendamento para grupos')
    assert any(total['label'] == 'Agendamento por outros profissionais da APS')
    assert any(total['label'] == 'Alta do episódio')
    assert any(total['label'] == 'Tratamento concluído')
    assert any(total['label'] == 'Retorno por consulta agendada')

    total_cnes = repo.get_oral_health_cares_by_outcome(56)

    assert total[total['label'] ==
                 'Retorno por consulta agendada']['total'].iloc[0] > total_cnes[total_cnes['label'] ==
                                                                                'Retorno por consulta agendada']['total'].iloc[0]
    assert total[total['label'] ==
                 'Tratamento concluído']['total'].iloc[0] > total_cnes[total_cnes['label'] ==
                                                                       'Tratamento concluído']['total'].iloc[0]


def test_get_oral_health_all_cares_by_place():
    repo = OralHealthDashboardRepository()
    total = repo.get_oral_health_all_cares_by_place()
    print(total)
    assert total.shape[0] >= 2
    total = repo.get_oral_health_all_cares_by_place(56)
    print(total)
    assert total.shape[0] >= 2
