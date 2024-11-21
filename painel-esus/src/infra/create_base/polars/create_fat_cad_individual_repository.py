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

EQUIPES = "select * from tb_fat_cad_individual"

class CreateCadIndividualBaseRepository(CreateBasesRepositoryInterface):
    _base = 'tb_fat_cad_individual'

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

                #    df.to_sql(name=self._base, con=local_engine,
                #              if_exists='append')
                    if not df.empty:

                        table = pa.Table.from_pandas(df,schema=schema_fixo,preserve_index = False)

                        if writer is None:

                            writer = pq.ParquetWriter("dados/input/"+parquet_file, schema_fixo)


                        writer.write_table(table)

            if writer:
                writer.close()  
        except Exception as e:
            print(e)
            print(f'Erro {self._base} already destroyed!')


    def get_schema(self):
            # Definindo o schema fixo
        schema = pa.schema([
            pa.field('co_seq_fat_cad_individual', pa.int64()),
            pa.field('nu_uuid_ficha', pa.string()),
            pa.field('nu_uuid_ficha_origem', pa.string()),
            pa.field('st_recusa_cadastro', pa.int64()),
            pa.field('nu_cns', pa.string()),
            pa.field('dt_nascimento', pa.string()),
            pa.field('st_desconhece_mae', pa.int64()),
            pa.field('co_dim_profissional', pa.int64()),
            pa.field('co_dim_tipo_ficha', pa.int64()),
            pa.field('co_dim_municipio', pa.int64()),
            pa.field('co_dim_unidade_saude', pa.int64()),
            pa.field('co_dim_equipe', pa.int64()),
            pa.field('co_dim_tempo', pa.int64()),
            pa.field('co_dim_tempo_validade', pa.int64()),
            pa.field('co_dim_tempo_validade_recusa', pa.int64()),
            pa.field('co_dim_sexo', pa.int64()),
            pa.field('co_dim_raca_cor', pa.int64()),
            pa.field('co_dim_nacionalidade', pa.int64()),
            pa.field('co_dim_pais_nascimento', pa.int64()),
            pa.field('co_dim_municipio_cidadao', pa.int64()),
            pa.field('nu_cns_responsavel', pa.string()),
            pa.field('st_responsavel_familiar', pa.int64()),
            pa.field('st_frequenta_creche', pa.int64()),
            pa.field('st_frequenta_cuidador', pa.int64()),
            pa.field('st_participa_grupo_comunitario', pa.int64()),
            pa.field('st_plano_saude_privado', pa.int64()),
            pa.field('st_comunidade_tradicional', pa.int64()),
            pa.field('st_deficiencia', pa.int64()),
            pa.field('st_defi_auditiva', pa.int64()),
            pa.field('st_defi_intelectual_cognitiva', pa.int64()),
            pa.field('st_defi_outra', pa.int64()),
            pa.field('st_defi_visual', pa.int64()),
            pa.field('st_defi_fisica', pa.int64()),
            pa.field('st_gestante', pa.int64()),
            pa.field('st_doenca_respiratoria', pa.int64()),
            pa.field('st_doenca_respira_asma', pa.int64()),
            pa.field('st_doenca_respira_dpoc_enfisem', pa.int64()),
            pa.field('st_doenca_respira_outra', pa.int64()),
            pa.field('st_doenca_respira_n_sabe', pa.int64()),
            pa.field('st_fumante', pa.int64()),
            pa.field('st_alcool', pa.int64()),
            pa.field('st_outra_droga', pa.int64()),
            pa.field('st_hipertensao_arterial', pa.int64()),
            pa.field('st_diabete', pa.int64()),
            pa.field('st_avc', pa.int64()),
            pa.field('st_infarto', pa.int64()),
            pa.field('st_hanseniase', pa.int64()),
            pa.field('st_tuberculose', pa.int64()),
            pa.field('st_cancer', pa.int64()),
            pa.field('st_internacao_12', pa.int64()),
            pa.field('st_tratamento_psiquiatra', pa.int64()),
            pa.field('st_acamado', pa.int64()),
            pa.field('st_domiciliado', pa.int64()),
            pa.field('st_usa_planta_medicinal', pa.int64()),
            pa.field('st_doenca_cardiaca', pa.int64()),
            pa.field('st_doenca_card_insuficiencia', pa.int64()),
            pa.field('st_doenca_card_outro', pa.int64()),
            pa.field('st_doenca_card_n_sabe', pa.int64()),
            pa.field('st_problema_rins', pa.int64()),
            pa.field('st_problema_rins_insuficiencia', pa.int64()),
            pa.field('st_problema_rins_outro', pa.int64()),
            pa.field('st_problema_rins_nao_sabe', pa.int64()),
            pa.field('st_pic', pa.int64()),
            pa.field('st_morador_rua', pa.int64()),
            pa.field('st_recebe_beneficio', pa.string()),
            pa.field('st_referencia_familiar', pa.string()),
            pa.field('co_dim_frequencia_alimentacao', pa.int64()),
            pa.field('st_orig_alimen_restaurante_pop', pa.int64()),
            pa.field('st_orig_alimen_doacao_reli', pa.int64()),
            pa.field('st_orig_alimen_doacao_rest', pa.int64()),
            pa.field('st_orig_alimen_doacao_popular', pa.int64()),
            pa.field('st_orig_alimen_outros', pa.int64()),
            pa.field('st_acompanhado_instituicao', pa.int64()),
            pa.field('st_visita_familiar_frequente', pa.string()),
            pa.field('st_higiene_pessoal_acesso', pa.string()),
            pa.field('st_hig_pess_banho', pa.int64()),
            pa.field('st_hig_pess_sanitario', pa.int64()),
            pa.field('st_hig_pess_higiene_bucal', pa.int64()),
            pa.field('st_hig_pess_outros', pa.int64()),
            pa.field('co_dim_tipo_parentesco', pa.int64()),
            pa.field('co_dim_cbo', pa.int64()),
            pa.field('co_dim_tipo_escolaridade', pa.int64()),
            pa.field('co_dim_situacao_trabalho', pa.int64()),
            pa.field('co_dim_tipo_orientacao_sexual', pa.int64()),
            pa.field('co_dim_tipo_saida_cadastro', pa.int64()),
            pa.field('co_dim_tipo_condicao_peso', pa.int64()),
            pa.field('co_dim_tempo_morador_rua', pa.int64()),
            pa.field('co_dim_etnia', pa.int64()),
            pa.field('co_dim_cbo_cidadao', pa.int64()),
            pa.field('co_dim_identidade_genero', pa.int64()),
            pa.field('co_dim_faixa_etaria', pa.int64()),
            pa.field('st_desconhece_pai', pa.int64()),
            pa.field('st_informar_orientacao_sexual', pa.int64()),
            pa.field('st_informar_identidade_genero', pa.int64()),
            pa.field('dt_naturalizacao', pa.string()),
            pa.field('dt_entrada_brasil', pa.string()),
            pa.field('dt_obito', pa.string()),
            pa.field('st_respons_crianca_adulto_resp', pa.int64()),
            pa.field('st_respons_crianca_outra_crian', pa.int64()),
            pa.field('st_respons_crianca_adolescente', pa.int64()),
            pa.field('st_respons_crianca_sozinha', pa.int64()),
            pa.field('st_respons_crianca_creche', pa.int64()),
            pa.field('st_respons_crianca_outro', pa.int64()),
            pa.field('nu_micro_area', pa.string()),
            pa.field('st_processo_linha_tempo', pa.int64()),
            pa.field('st_processo_cidadao', pa.int64()),
            pa.field('no_nome', pa.string()),
            pa.field('no_nome_social', pa.string()),
            pa.field('no_nome_mae', pa.string()),
            pa.field('no_nome_pai', pa.string()),
            pa.field('nu_nis', pa.string()),
            pa.field('nu_portaria_naturalizacao', pa.string()),
            pa.field('nu_celular', pa.string()),
            pa.field('no_email', pa.string()),
            pa.field('nu_obito_do', pa.string()),
            pa.field('no_maternidade_referencia', pa.string()),
            pa.field('no_causa_internacao12', pa.string()),
            pa.field('no_plantas_medicinais', pa.string()),
            pa.field('no_outra_condicao1', pa.string()),
            pa.field('no_outra_condicao2', pa.string()),
            pa.field('no_outra_condicao3', pa.string()),
            pa.field('no_acompanhado_instituicao', pa.string()),
            pa.field('no_visita_familiar_parentesco', pa.string()),
            pa.field('nu_uuid_dado_transp', pa.string()),
            pa.field('co_dim_tipo_origem_dado_transp', pa.int64()),
            pa.field('co_dim_cds_tipo_origem', pa.int64()),
            pa.field('st_gerado_automaticamente', pa.int64()),
            pa.field('st_ficha_inativa', pa.int64()),
            pa.field('co_fat_cidadao_pec', pa.int64()),
            pa.field('co_fat_cidadao_pec_responsvl', pa.int64()),
            pa.field('st_proc_operacionais', pa.int64()),
            pa.field('nu_cpf_cidadao', pa.string()),
            pa.field('nu_cpf_responsavel', pa.string()),
            pa.field('co_dim_povo_comunidad_trad', pa.int64()),
            pa.field('st_comeu_que_tinha_dnheir_acab', pa.int64()),
            pa.field('st_alimentos_acab_sem_dinheiro', pa.int64()),
        ])

        return schema
