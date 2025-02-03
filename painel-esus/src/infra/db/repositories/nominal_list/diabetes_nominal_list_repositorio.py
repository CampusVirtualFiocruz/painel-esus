import os
from datetime import datetime

import pandas as pd
import polars as pl
from sqlalchemy import text
from src.data.interfaces.create_bases.create_bases_repository import (
    CreateBasesRepositoryInterface,
)
from src.domain.entities.diabetes import Diabetes
from src.env.conf import getenv
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.connection_local import (
    DBConnectionHandler as LocalDBConnectionHandler,
)


class DiabeteNominalListRepository(CreateBasesRepositoryInterface):
    _base = "diabetes_nominal"

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
        return result if result is not None else pl.DataFrame([[]])

    def get_autorreferidos(self):
        working_directory = os.getcwd()
        input_path = os.path.join(working_directory, "dados", "input")
        cad = pl.read_parquet(input_path + os.sep + "tb_fat_cad_individual.parquet")

        result = (
            cad.filter((pl.col("st_diabete") == 1))
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

    def get_hemoglobina_glicada(self):
        sql = """select distinct on (cidadao_pec) * from (
            select
                    co_fat_cidadao_pec cidadao_pec, max(co_dim_tempo::text::date) as ultima_data_hemoglobina_glicada,
                    extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_hemoglobina_glicada
            from
                    tb_fat_proced_atend where ds_filtro_procedimento like any(array['%|0202010503|%'])  group by 1
            union all
            select
                    co_fat_cidadao_pec cidadao_pec, max(co_dim_tempo::text::date) as ultima_data_hemoglobina_glicada,
                    extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_hemoglobina_glicada
            from
                    tb_fat_atendimento_individual tfai  where
                    ds_filtro_proced_avaliados like  any(array['%|0202010503|%'])  group by 1
        ) lista_procedimentos"""
        return self.get_query(sql)

    def create_base(self):
        working_directory = os.getcwd()
        input_path = os.path.join(working_directory, "dados", "input")

        diabetes = Diabetes()
        diabetes_cids = diabetes.target
        fai = pl.read_parquet(
            input_path + os.sep + "tb_fat_atendimento_individual.parquet"
        )
        cbo = pl.read_parquet(input_path + os.sep + "tb_dim_cbo.parquet")

        print("fai: ", fai.shape)
        fai = fai.join(
            cbo, left_on="co_dim_cbo_1", right_on="co_seq_dim_cbo", how="left"
        )
        print("fai - cbo: ", fai.shape)

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
                pl.when(pl.col("diagnostico").str.contains_any(diabetes_cids))
                .then(pl.lit("cid/ciaps"))
                .when(
                    pl.col("co_fat_cidadao_pec").is_in(cidadaos_pec)
                    & ~pl.col("diagnostico").str.contains_any(diabetes_cids)
                )
                .then(pl.lit("autorreferido"))
            )
        ).unique(subset=["co_fat_cidadao_pec"])

        diabetes_list = fai_agg.filter(
            (
                pl.col("tipo").str.contains("cid/ciaps")
                | pl.col("tipo").str.contains("autorreferido")
            )
        )

        diabetes_list = diabetes_list.select(pl.all().exclude("diagnostico"))
        diabetes_list = diabetes_list.with_columns(pl.col("tipo").alias("diagnostico"))

        min_date_atendimentos = (
            fai.select(
                "co_fat_cidadao_pec",
                "co_dim_tempo",
                "ds_filtro_cids",
                "ds_filtro_ciaps",
            )
            .filter(
                pl.col("ds_filtro_cids").str.contains_any(diabetes_cids)
                | pl.col("ds_filtro_ciaps").str.contains_any(diabetes_cids)
            )
            .group_by("co_fat_cidadao_pec")
            .agg(pl.all().unique())
            .with_columns(
                pl.col("co_dim_tempo")
                .list.first()
                .cast(pl.String)
                .str.to_date("%Y%m%d")
                .alias("min_date"),
                pl.col("co_fat_cidadao_pec").alias("cidadao_pec"),
            )
            .select("cidadao_pec", "min_date")
        )

        fai_cids = fai.join(
            diabetes_list,
            left_on="co_fat_cidadao_pec",
            right_on="co_fat_cidadao_pec",
        )

        fai_cids = (
            fai_cids.filter(
                (
                    (
                        pd.to_datetime("today").normalize().to_pydatetime()
                        - pl.col("co_dim_tempo").cast(pl.String).str.to_date("%Y%m%d")
                    ).dt.total_days()
                    <= 365
                )
                | pl.col("tipo").str.contains("autorreferido")
            )
            .select("co_fat_cidadao_pec")
            .unique(subset=["co_fat_cidadao_pec"])
        )
        fai_cids = fai_cids["co_fat_cidadao_pec"].to_list()

        nominal_list = diabetes_list.with_columns(
            pl.col("co_fat_cidadao_pec").alias("cidadao_pec"),
        ).select(
            "cidadao_pec",
            "diagnostico",
            "cids",
            "ciaps",
            "tipo",
        )

        # print("nominal_lis head", nominal_list.head())
        visita_acs = self.visita_acs()
        print("nominal_list: ", nominal_list.shape)
        print("visita_acs: ", visita_acs.shape)
        nominal_list = nominal_list.join(
            min_date_atendimentos, on="cidadao_pec", how="left"
        )
        if visita_acs is not None and visita_acs.shape[0] > 0:
            nominal_list = nominal_list.join(visita_acs, on="cidadao_pec", how="left")
            print("nominal_list - visita_acs: ", nominal_list.shape)
        else:
            nominal_list = nominal_list.with_columns(
                pl.lit(None).alias("data_ultima_visita_acs"),
                pl.lit(99).alias("meses_desde_ultima_visita"),
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
        print("nominal_list - total_atendimentos_medicos: ", nominal_list.shape)
        nominal_list = nominal_list.join(
            max_date_atendimentos_medicos,
            left_on="cidadao_pec",
            right_on="cidadao_pec",
            how="left",
        )
        print("nominal_list - max_date_atendimentos_medicos: ", nominal_list.shape)

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

        hemoglobina_glicada = self.get_hemoglobina_glicada()

        if hemoglobina_glicada is not None and hemoglobina_glicada.shape[0] > 0:
            hemoglobina_glicada = hemoglobina_glicada.with_columns(
                pl.col("meses_ultima_data_hemoglobina_glicada").cast(pl.Int64),
                pl.col("cidadao_pec").cast(pl.Int64),
            )

            nominal_list = nominal_list.join(
                hemoglobina_glicada,
                left_on="co_fat_cidadao_pec",
                right_on="cidadao_pec",
                how="left",
                join_nulls=True,
                coalesce=True,
            )
        else:
            nominal_list = nominal_list.with_columns(
                pl.lit(None).alias('ultima_data_hemoglobina_glicada'),
                pl.lit(99).alias('meses_ultima_data_hemoglobina_glicada')
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
            alerta_ultima_hemoglobina_glicada=(
                pl.when(
                    pl.coalesce(pl.col("meses_ultima_data_hemoglobina_glicada"), 0) < 6
                )
                .then(False)
                .otherwise(True)
            ),
        )
        nominal_list = nominal_list.filter(pl.col("cidadao_pec").is_in(fai_cids))

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
            "ultima_data_hemoglobina_glicada",
            "alerta_ultima_hemoglobina_glicada",
        )
        nominal_list_output = nominal_list_output.with_columns(
            pl.col("min_date").cast(pl.Datetime).dt.convert_time_zone("UTC"),
            pl.col("data_ultima_visita_acs")
            .cast(pl.Datetime)
            .dt.convert_time_zone("UTC"),
            pl.col("ultimo_atendimento_medico")
            .cast(pl.Datetime)
            .dt.convert_time_zone("UTC"),
            pl.col("ultimo_atendimento_enfermeiro")
            .cast(pl.Datetime)
            .dt.convert_time_zone("UTC"),
            pl.col("ultimo_atendimento_medico_enfermeiro")
            .cast(pl.Datetime)
            .dt.convert_time_zone("UTC"),
            pl.col("ultimo_atendimento_odonto")
            .cast(pl.Datetime)
            .dt.convert_time_zone("UTC"),
            pl.col("ultima_data_afericao_pa")
            .cast(pl.Datetime)
            .dt.convert_time_zone("UTC"),
            pl.col("ultima_data_hemoglobina_glicada")
            .cast(pl.Datetime)
            .dt.convert_time_zone("UTC"),
        )
        with LocalDBConnectionHandler() as con:
            engine = con.get_engine()
            nominal_list_output.write_database(
                table_name=self._base,
                connection=engine,
                if_table_exists="append",
                engine="sqlalchemy",
            )
