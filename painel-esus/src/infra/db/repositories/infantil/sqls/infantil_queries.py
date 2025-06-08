from src.utils.query_builders import gen_where_cnes_equipe


def sql_total_infantil(cnes: int = None, equipe: int = None):
    return f"""
            SELECT count(*) as total
            FROM read_parquet('/home/allanbontempo/programacao/fiocruz/painel-esus/painel-esus/src/infra/db/repositories/infantil/sqls/dados/crianca.parquet')
            {gen_where_cnes_equipe(None, cnes, equipe)}"""
