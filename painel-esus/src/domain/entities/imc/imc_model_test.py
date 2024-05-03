# pylint: disable=E0401
import pandas as pd

from .imc_model import ImcModel


def test_imc_model():
    data_frame = pd.DataFrame(
        columns=['nu_altura', 'nu_peso'],
        data=[
            [170, 90],
            [157, 90],
            [170, 80],
            [100, 1]
        ]
    )
    imc_model = ImcModel()

    data_frame.apply(lambda x: imc_model.check_presence(
        weight=x['nu_peso'],
        height=x['nu_altura']
    ), axis=1)
    print()
    for imc_item in imc_model.get_list():
        print(imc_item.statistics_response(data_frame.shape[0]))
