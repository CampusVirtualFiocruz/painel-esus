from ...models.infections.accute_infections import ClassifyDF, AccuteInfection, ExanthematousFever, IntestinalInfections, NonspecificFever, RespiratoryInfections
from ...models.infections.stub.infeccoes_agudas import INFECCOES_AGUDAS
from ...models.infections.individual_care import get_list_for_all_cares_by_class_grouped_by_year
from ...infra.config.connection import con

def get_chart_data( date_range = []):
    infeccao_respiratoria = RespiratoryInfections()
    infeccao_intestinal = IntestinalInfections()
    febre_exantematica = ExanthematousFever()
    febre_inespecifica = NonspecificFever()

    target_list = [infeccao_respiratoria, infeccao_intestinal, febre_exantematica, febre_inespecifica]

    return get_list_for_all_cares_by_class_grouped_by_year(con, date_range, INFECCOES_AGUDAS, target_list, ClassifyDF)