# pylint: disable=invalid-name
# pylint: disable=unused-import
from pprint import pprint

import pytest

from src.data.use_cases.tests.data_frame_mocks.atendimento_individual_df import \
    atendimento_individual_df

from .hypertension_complications import HypertensionComplications


@pytest.mark.usefixtures('atendimento_individual_df')
def test_hypertension_complications(atendimento_individual_df):
    hypertension_complications = HypertensionComplications(
        atendimento_individual_df)
    response = hypertension_complications.compute_statistics()
    pprint(response)
