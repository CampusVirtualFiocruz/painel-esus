import os
from datetime import datetime

import pandas as pd
import polars as pl
from sqlalchemy import text
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.domain.entities.hypertension import Hypertension
from src.env.conf import getenv
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)


class HypertensionNominalListRepository(CreateBasesRepositoryInterface):
    _base = 'hipertensao_nominal'
    def get_query(self, sql):
        result = None
        with DBConnectionHandler() as con:
            engine = con.get_engine()
            for df in pl.read_database(
                query=sql,
                connection=engine,
                iter_batches=True,
                batch_size=getenv("CHUNK_SIZE", 1000),
            ):
                if result is None:
                    result = df
                else:
                    result = pl.concat([result, df])
        return result if not None else []

    def get_autorreferidos(self):
        working_directory = os.getcwd()
        input_path = os.path.join(working_directory, "dados", "input")
        cad = pl.read_parquet(input_path + os.sep + "tb_fat_cad_individual.parquet")

        result = (
            cad.filter((pl.col("st_hipertensao_arterial") == 1))
            .sort("co_fat_cidadao_pec", "co_dim_tempo", descending=[False, True])
            .unique(subset=["co_fat_cidadao_pec"], maintain_order=True)
        )
        result = result[["co_fat_cidadao_pec", "st_diabete", "st_hipertensao_arterial"]]
        return result

    def visita_acs(self):
        sql = f"""select distinct
                            tfvd.co_fat_cidadao_pec cidadao_pec,
                            max(tcfvd.dt_ficha::text::date) as data_ultima_visita_acs,
                            (
                                extract(year from age(now(), max(tcfvd.dt_ficha::text::date) ))*12 + extract(month from age(now(), max(tcfvd.dt_ficha::text::date) )) 
                            ) meses_desde_ultima_visita
                        from tb_cds_ficha_visita_domiciliar tcfvd 
                        left join tb_cds_prof tcp  on tcfvd.co_cds_prof = tcp.co_seq_cds_prof 
                        left join tb_fat_visita_domiciliar tfvd on tcfvd.co_unico_ficha = tfvd.nu_uuid_ficha 
                        left join tb_dim_equipe tde on tde.co_seq_dim_equipe = tfvd.co_dim_equipe 
                        left join tb_equipe te  on tde.nu_ine = te.nu_ine
                        left join tb_tipo_equipe tte  on te.tp_equipe = tte.co_seq_tipo_equipe
                        where 
                            tcp.nu_cbo_2002 like any(array['5151%', '3233%']) and  tte.nu_ms in ('70', '76') group by 1"""
        return self.get_query(sql)

    def get_atendimento_odonto(self):
        sql = """select
                    tfao.co_fat_cidadao_pec cidadao_pec,
                    max(co_dim_tempo::text::date) ultimo_atendimento_odonto,
                    (
                        extract(year
                from
                    age(now(),
                    max(co_dim_tempo::text::date) ))* 12 + extract(month
                from
                    age(now(),
                    max(co_dim_tempo::text::date) )) 
                    ) meses_desde_ultima_visita_odontologica
                from
                    tb_fat_atendimento_odonto tfao
                group by
                    1"""
        return self.get_query(sql)

    def get_afericao_pa(self):
        sql = """select
                        co_fat_cidadao_pec cidadao_pec,
                        max(co_dim_tempo::text::date) as ultima_data_afericao_pa,
                        extract(year
                    from
                        age(now(),
                        max(co_dim_tempo::text::date) ))* 12 + extract(month
                    from
                        age(now(),
                        max(co_dim_tempo::text::date) )) as meses_ultima_data_afericao_pa
                    from 
                        tb_fat_proced_atend
                    where
                        ds_filtro_procedimento like '%|0301100039|%'
                    group by
                        1"""
        return self.get_query(sql)

    def get_creatinina(self):
        sql = """select distinct on (cidadao_pec) * from (
		select 
			co_fat_cidadao_pec cidadao_pec, max(co_dim_tempo::text::date) as ultima_data_creatinina,
			extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_creatinina
		from 
			tb_fat_proced_atend where ds_filtro_procedimento like any(array['%|0202010317|%', '%|ABEX003|%'])  group by 1
		union all 	
		select 
			co_fat_cidadao_pec cidadao_pec, max(co_dim_tempo::text::date) as ultima_data_creatinina,
			extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_creatinina
		from 
			tb_fat_atendimento_individual where 
			ds_filtro_proced_avaliados like  any(array['%|0202010317|%', '%|ABEX003|%'])  group by 1
	) lista_procedimentos;"""
        return self.get_query(sql)

    def create_base(self):
        working_directory = os.getcwd()
        input_path = os.path.join(working_directory, "dados", "input")

        hypertension = Hypertension()
        hypertension_cids = hypertension.target
        fai = pl.read_parquet(
            input_path + os.sep + "tb_fat_atendimento_individual.parquet"
        )
        cbo = pl.read_parquet(input_path + os.sep + "tb_dim_cbo.parquet")
        fai = fai.join(
            cbo, left_on="co_dim_cbo_1", right_on="co_seq_dim_cbo", how="left"
        )

        autoreferidos = self.get_autorreferidos()
        cidadaos_pec = autoreferidos["co_fat_cidadao_pec"].to_list()

        fai_agg = (
            fai.group_by("co_fat_cidadao_pec")
            .agg(
                pl.col("ds_filtro_cids").str.join("").alias("cids"),
                pl.col("ds_filtro_ciaps").str.join("").alias("ciaps"),
            )
            .with_columns(
                pl.col("cids").str.replace_all(r"[||]+", "|"),
                pl.col("ciaps").str.replace_all(r"[||]+", "|"),
                pl.concat_str(pl.col("cids"), pl.col("ciaps"))
                .str.replace_all(r"[||]+", "|")
                .alias("diagnostico"),
            )
        )
        fai_agg = fai_agg.with_columns(
            tipo=(
                pl.when(pl.col("diagnostico").str.contains_any(hypertension_cids))
                .then(pl.lit("cid/ciaps"))
                .when(
                    pl.col("co_fat_cidadao_pec").is_in(cidadaos_pec)
                    & ~pl.col("diagnostico").str.contains_any(hypertension_cids)
                )
                .then(pl.lit("autorreferido"))
            )
        ).unique(subset=["co_fat_cidadao_pec"])

        hypertension_list = fai_agg.filter(
            (
                pl.col("tipo").str.contains("cid/ciaps")
                | pl.col("tipo").str.contains("autorreferido")
            )
        )
        hypertension_list = hypertension_list.select(pl.all().exclude("diagnostico"))
        hypertension_list = hypertension_list.with_columns(pl.col('tipo').alias('diagnostico'))

        fai_cids = fai.join(
            hypertension_list,
            left_on="co_fat_cidadao_pec",
            right_on="co_fat_cidadao_pec",
        )

        fai_cids = (
            fai_cids.filter(
                ((
                    pd.to_datetime("today").normalize().to_pydatetime()
                    - pl.col("co_dim_tempo").cast(pl.String).str.to_date("%Y%m%d")
                ).dt.total_days()
                <= 365 )| pl.col('tipo').str.contains('autorreferido')
            )
            .select("co_fat_cidadao_pec")
            .unique(subset=["co_fat_cidadao_pec"])
        )
        fai_cids= fai_cids["co_fat_cidadao_pec"].to_list()

        min_date_atendimentos = (
            fai.select(
                "co_fat_cidadao_pec",
                "co_dim_tempo",
                "ds_filtro_cids",
                "ds_filtro_ciaps",
            )
            .filter(
                pl.col("ds_filtro_cids").str.contains_any(hypertension_cids)
                | pl.col("ds_filtro_ciaps").str.contains_any(hypertension_cids)
            )
            .group_by("co_fat_cidadao_pec")
            .agg(pl.all().unique())
            .with_columns(
                pl.col("co_dim_tempo")
                .list.first()
                .alias("min_date")
                .cast(pl.String)
                .str.to_date("%Y%m%d")
                .alias("min_date"),
                pl.col("co_fat_cidadao_pec").alias("cidadao_pec"),
            )
            .select("cidadao_pec", "min_date")
        )

        nominal_list = hypertension_list.with_columns(
            pl.col("co_fat_cidadao_pec").alias("cidadao_pec"),
        ).select(
            "cidadao_pec",
            "diagnostico",
            "cids",
            "ciaps",
            "tipo",
        )

        visita_acs = self.visita_acs()

        nominal_list = nominal_list.join(min_date_atendimentos, on='cidadao_pec', how='left')

        if visita_acs is not None and visita_acs.shape[0] > 0:
            nominal_list = nominal_list.join(visita_acs, on="cidadao_pec", how="left")
        else:
            nominal_list = nominal_list.with_columns(
                pl.lit(None).alias('data_ultima_visita_acs'),
                pl.lit(99).alias('meses_desde_ultima_visita')
            )

        atendimentos_medicos = fai.filter(
            pl.col("nu_cbo").str.contains_any(["2251", "2252", "2253"])
        )
        max_date_atendimentos_medicos = (
            atendimentos_medicos.select("co_fat_cidadao_pec", "co_dim_tempo")
            .with_columns(pl.max("co_dim_tempo"))
            .group_by("co_fat_cidadao_pec")
            .agg(pl.all().unique())
            .with_columns(
                pl.col("co_dim_tempo")
                .list.first()
                .alias("ultimo_atendimento_medico")
                .cast(pl.String)
                .str.to_date("%Y%m%d"),
                pl.col("co_fat_cidadao_pec").alias("cidadao_pec"),
            )
        )

        total_atendimentos_medicos = (
            atendimentos_medicos.group_by("co_fat_cidadao_pec")
            .count()
            .with_columns(
                pl.col("co_fat_cidadao_pec").alias("cidadao_pec"),
                pl.col("count").alias("total_consulta_individual_medico"),
            )
            .select("cidadao_pec", "total_consulta_individual_medico")
        )

        nominal_list = nominal_list.join(
            total_atendimentos_medicos,
            left_on="cidadao_pec",
            right_on="cidadao_pec",
            how="left",
        )
        nominal_list = nominal_list.join(
            max_date_atendimentos_medicos,
            left_on="cidadao_pec",
            right_on="cidadao_pec",
            how="left",
        )

        atendimentos_enfermeiros = fai.filter(
            pl.col("nu_cbo").str.contains_any(
                [
                    "2235",
                    "2231",
                ]
            )
        )
        max_date_atendimentos_enfermeiros = (
            atendimentos_enfermeiros.select("co_fat_cidadao_pec", "co_dim_tempo")
            .with_columns(pl.max("co_dim_tempo"))
            .group_by("co_fat_cidadao_pec")
            .agg(pl.all().unique())
            .with_columns(
                pl.col("co_dim_tempo")
                .list.first()
                .alias("ultimo_atendimento_enfermeiro")
                .cast(pl.String)
                .str.to_date("%Y%m%d"),
                pl.col("co_fat_cidadao_pec").alias("cidadao_pec"),
            )
        )
        nominal_list = nominal_list.join(
            max_date_atendimentos_enfermeiros,
            left_on="cidadao_pec",
            right_on="cidadao_pec",
            how="left",
        )
        total_atendimentos_enfermeiros = (
            atendimentos_enfermeiros.group_by("co_fat_cidadao_pec")
            .count()
            .with_columns(
                pl.col("co_fat_cidadao_pec").alias("cidadao_pec"),
                pl.col("count").alias("total_consulta_individual_enfermeiro"),
            )
            .select("cidadao_pec", "total_consulta_individual_enfermeiro")
        )
        nominal_list = nominal_list.join(
            total_atendimentos_enfermeiros,
            left_on="cidadao_pec",
            right_on="cidadao_pec",
            how="left",
        )
        odonto = self.get_atendimento_odonto()
        if odonto is not None and odonto.shape[0] > 0:
            nominal_list = nominal_list.join(
                odonto,
                left_on="cidadao_pec",
                right_on="cidadao_pec",
                how="left",
            )
        else:
            nominal_list = nominal_list.with_columns(
                pl.lit(None).alias("ultimo_atendimento_odonto"),
                pl.lit(99).alias("meses_desde_ultima_visita_odontologica"),
            )

        afericao_pa = self.get_afericao_pa()
        if afericao_pa is not None and afericao_pa.shape[0] > 0:
            nominal_list = nominal_list.join(
                afericao_pa,
                left_on="cidadao_pec",
                right_on="cidadao_pec",
                how="left",
            )
        else:
            nominal_list = nominal_list.with_columns(
                pl.lit(None).alias("ultima_data_afericao_pa"),
                pl.lit(99).alias("meses_ultima_data_afericao_pa"),
            )

        creatinina = self.get_creatinina()
        if creatinina is not None and creatinina.shape[0] > 0:
            nominal_list = nominal_list.join(
                creatinina,
                left_on="cidadao_pec",
                right_on="cidadao_pec",
                how="left",
            )
        else:
            nominal_list = nominal_list.with_columns(
                pl.lit(None).alias("ultima_data_creatinina"),
                pl.lit(99).alias("meses_ultima_data_creatinina"),
            )

        nominal_list = nominal_list.with_columns(
            alerta_visita_acs=(
                pl.when(pl.col("meses_desde_ultima_visita") < 6)
                .then(False)
                .otherwise(True)
            ),
            alerta_total_de_consultas_medico=(
                pl.when(
                    (
                        pl.col("total_consulta_individual_medico")
                        + pl.col("total_consulta_individual_enfermeiro")
                    )
                    > 2
                )
                .then(False)
                .otherwise(True)
            ),
            total_consulta_individual_medico_enfermeiro=(
                pl.col("total_consulta_individual_medico")
                + pl.col("total_consulta_individual_enfermeiro")
            ),
            ultimo_atendimento_medico_enfermeiro=pl.max_horizontal(
                "ultimo_atendimento_medico",
                "ultimo_atendimento_enfermeiro",
            ),
            alerta_ultima_consulta_medico=(
                pl.when(
                    (
                        pd.to_datetime("today").normalize().to_pydatetime()
                        - pl.max_horizontal(
                            "ultimo_atendimento_medico",
                            "ultimo_atendimento_enfermeiro",
                        ).cast(pl.Date)
                    ).dt.total_days()
                    < 180
                )
                .then(False)
                .otherwise(True)
            ),
            alerta_ultima_consulta_odontologica=(
                pl.when(pl.col("meses_desde_ultima_visita_odontologica") < 6)
                .then(False)
                .otherwise(True)
            ),
            alerta_afericao_pa=(
                pl.when(pl.col("meses_ultima_data_afericao_pa") < 6)
                .then(False)
                .otherwise(True)
            ),
            alerta_creatinina=(
                pl.when(pl.col("meses_ultima_data_creatinina").cast(pl.Int64) < 6)
                .then(False)
                .otherwise(True)
            ),
        )
        nominal_list = nominal_list.filter(pl.col("cidadao_pec").is_in(fai_cids))
        # print(
        #     nominal_list.filter(pl.col("co_fat_cidadao_pec") == 10242)[
        #         ["alerta_ultima_consulta_medico", "total_days"]
        #     ]
        # )
        nominal_list_output = nominal_list.select(
                "co_fat_cidadao_pec",
                "diagnostico",
                "cids",
                "ciaps",
                "min_date",
                "data_ultima_visita_acs",
                "alerta_visita_acs",
                "total_consulta_individual_medico",
                "total_consulta_individual_enfermeiro",
                "total_consulta_individual_medico_enfermeiro",
                "ultimo_atendimento_medico",
                "ultimo_atendimento_enfermeiro",
                "alerta_total_de_consultas_medico",
                "ultimo_atendimento_medico_enfermeiro",
                "alerta_ultima_consulta_medico",
                "ultimo_atendimento_odonto",
                "alerta_ultima_consulta_odontologica",
                "ultima_data_afericao_pa",
                "alerta_afericao_pa",
                "ultima_data_creatinina",
                "alerta_creatinina",
            )
        nominal_list_output = nominal_list_output.with_columns(
            pl.col("min_date").cast(pl.String).str.to_datetime("%Y-%m-%d"),
            pl.col("data_ultima_visita_acs").cast(pl.String).str.to_datetime("%Y-%m-%d"),
            pl.col("ultimo_atendimento_medico").cast(pl.String).str.to_datetime("%Y-%m-%d"),
            pl.col("ultimo_atendimento_enfermeiro").cast(pl.String).str.to_datetime("%Y-%m-%d"),
            pl.col("ultimo_atendimento_medico_enfermeiro").cast(pl.String).str.to_datetime("%Y-%m-%d"),
            pl.col("ultimo_atendimento_odonto").cast(pl.String).str.to_datetime("%Y-%m-%d"),
            pl.col("ultima_data_afericao_pa").cast(pl.String).str.to_datetime("%Y-%m-%d"),
            pl.col("ultima_data_creatinina").cast(pl.String).str.to_datetime("%Y-%m-%d"),
        )

        with LocalDBConnectionHandler() as con:
            engine = con.get_engine()
            nominal_list_output.write_database(
                table_name=self._base,
                connection=engine,
                if_table_exists="append",
                engine="sqlalchemy",
            )
