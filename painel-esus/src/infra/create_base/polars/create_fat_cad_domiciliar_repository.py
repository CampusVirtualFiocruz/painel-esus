import os

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from sqlalchemy import text
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.env.conf import getenv
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)

EQUIPES = "select * from tb_fat_cad_domiciliar"

class CreateCadDomiciliarBaseRepository(CreateBasesRepositoryInterface):
    _base = 'tb_fat_cad_domiciliar'

    def __init__(self):
        ...

    def get_base(self):
        return self._base

    def create_base(self):
        try:

            schema_fixo =  self.get_schema() 

            local_db = LocalDBConnectionHandler()
            local_engine = local_db.get_engine()
            _next = True
            offset = 0
            chunk_size = getenv("CHUNK_SIZE", 25000)
            parquet_file = f"{self._base}.parquet"
            # os.remove("dados/input/" + parquet_file)
            writer = None 
            while _next:
                with DBConnectionHandler() as db:
                    engine = db.get_engine()
                    print(text(f"{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};"))
                    df = pd.read_sql_query(
                        text(f'{EQUIPES}  LIMIT {chunk_size} OFFSET {offset};'), con=engine,dtype_backend='pyarrow')

                    if df.shape[0] is not None and df.shape[0] > 0:
                        _next = True
                    else:
                        _next = False

                    offset += chunk_size

                    df.to_sql(name=self._base, con=local_engine,
                                if_exists='append')
                    if not df.empty:

                        table = pa.Table.from_pandas(df,schema=schema_fixo,preserve_index = False)

                        if writer is None:

                            writer = pq.ParquetWriter("dados/input/"+parquet_file,schema=schema_fixo) #, schema=schema_fixo

                        writer.write_table(table)

            if writer:
                writer.close()  
        except Exception as e:
            print(e)
            print(f'Erro {self._base} already destroyed!')

    def get_schema(self):
        # Definindo o schema fixo
        schema = pa.schema([
            pa.field('co_seq_fat_cad_domiciliar', pa.int64(), nullable=False),
            pa.field('nu_uuid_ficha', pa.string(), nullable=True),
            pa.field('nu_uuid_ficha_origem', pa.string(), nullable=True),
            pa.field('qt_morador', pa.int32(), nullable=True),
            pa.field('nu_comodo', pa.int32(), nullable=True),
            pa.field('st_recusa_cadastro', pa.int32(), nullable=True),
            pa.field('co_dim_tipo_ficha', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_imovel', pa.int64(), nullable=True),
            pa.field('co_dim_profissional', pa.int64(), nullable=True),
            pa.field('co_dim_municipio', pa.int64(), nullable=True),
            pa.field('co_dim_unidade_saude', pa.int64(), nullable=True),
            pa.field('co_dim_equipe', pa.int64(), nullable=True),
            pa.field('co_dim_tempo', pa.int64(), nullable=True),
            pa.field('co_dim_tempo_validade', pa.int64(), nullable=True),
            pa.field('co_dim_tempo_validade_recusa', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_logradouro', pa.int64(), nullable=True),
            pa.field('co_dim_municipio_cidadao', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_situacao_moradia', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_localizacao', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_domicilio', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_posse_terra', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_acesso_domicilio', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_material_parede', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_abastecimento_agua', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_tratamento_agua', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_escoamento_sanitar', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_destino_lixo', pa.int64(), nullable=True),
            pa.field('co_dim_cbo', pa.int64(), nullable=True),
            pa.field('st_disp_energia', pa.int32(), nullable=True),
            pa.field('st_animal_domiciliar', pa.int32(), nullable=True),
            pa.field('qt_animal_domiciliar', pa.int32(), nullable=True),
            pa.field('st_animal_gato', pa.int32(), nullable=True),
            pa.field('st_animal_cachorro', pa.int32(), nullable=True),
            pa.field('st_animal_passaro', pa.int32(), nullable=True),
            pa.field('st_animal_outros', pa.int32(), nullable=True),
            pa.field('st_outros_prof_vinclds', pa.int32(), nullable=True),
            pa.field('nu_micro_area', pa.string(), nullable=True),
            pa.field('st_processo_linha_tempo', pa.int32(), nullable=True),
            pa.field('st_processo_familia', pa.int32(), nullable=True),
            pa.field('st_familias', pa.int32(), nullable=True),
            pa.field('ds_filtro_tipo_renda_familiar', pa.string(), nullable=True),
            pa.field('nu_cep', pa.string(), nullable=True),
            pa.field('no_logradouro', pa.string(), nullable=True),
            pa.field('nu_num_logradouro', pa.string(), nullable=True),
            pa.field('no_complemento', pa.string(), nullable=True),
            pa.field('no_bairro', pa.string(), nullable=True),
            pa.field('no_ponto_referencia', pa.string(), nullable=True),
            pa.field('nu_telefone_residencia', pa.string(), nullable=True),
            pa.field('nu_telefone_contato', pa.string(), nullable=True),
            pa.field('no_instituicao_nome', pa.string(), nullable=True),
            pa.field('no_instituicao_cargo', pa.string(), nullable=True),
            pa.field('nu_instituicao_cns', pa.string(), nullable=True),
            pa.field('nu_instituicao_telefone', pa.string(), nullable=True),
            pa.field('nu_uuid_dado_transp', pa.string(), nullable=True),
            pa.field('co_dim_tipo_origem_dado_transp', pa.int64(), nullable=True),
            pa.field('co_dim_cds_tipo_origem', pa.int64(), nullable=True),
            pa.field('st_gerado_automaticamente', pa.int32(), nullable=True),
            pa.field('st_proc_operacionais', pa.int32(), nullable=True),
            pa.field('st_processa_familita_terrtro', pa.int32(), nullable=True),
            pa.field('nu_latitude', pa.float64(), nullable=True),
            pa.field('nu_longitude', pa.float64(), nullable=True),
            pa.field('co_dim_tipo_origem_energ_eletr', pa.int64(), nullable=True),
            pa.field('co_dim_tipo_endereco', pa.int64(), nullable=True),
            pa.field('co_dim_aldeia', pa.int64(), nullable=True),
            pa.field('co_dim_municipio_aldeia', pa.int64(), nullable=True),
            pa.field('nu_residencia_indigena', pa.string(), nullable=True),
            pa.field('st_animal_macaco', pa.int32(), nullable=True),
            pa.field('st_animal_galinha', pa.int32(), nullable=True),
            pa.field('st_animal_porco', pa.int32(), nullable=True),
            pa.field('st_animal_repteis', pa.int32(), nullable=True)
        ])
        return schema
