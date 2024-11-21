from .cadastros import gera_banco


def test_gera_banco():
    df = gera_banco()
    print(df.shape())
