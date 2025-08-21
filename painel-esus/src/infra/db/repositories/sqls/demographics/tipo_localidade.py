from src.infra.db.repositories import CADASTRO_PATH
from src.infra.db.repositories.sqls.parquet.tb_acompanhamento_vinculo import get_pessoas


def filter_by_localidade(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None:
        where_clause += f""" AND co_dim_unidade_saude = {cnes}
                """
        if equipe and equipe is not None:
            where_clause += f"  and codigo_equipe = {equipe} "

    return f"""
        SELECT 
            ds_tipo_localizacao_domicilio, count(*) as total
        FROM read_parquet('{CADASTRO_PATH}') 
        WHERE 1=1 {where_clause} 
        group by ds_tipo_localizacao_domicilio
    """
