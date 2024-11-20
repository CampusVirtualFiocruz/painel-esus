# pylint: disable=R0913,C0103
from src.domain.entities.diabetes import Diabetes

from .get_cids import get_cids

diabetes = Diabetes()
diabetes_cids = ",".join([ f"'{cid}'" for cid in diabetes.target])

LISTA_NOMINAL_DIABETES = f"""
with 
autoreferidos as (
	select distinct tfci.co_fat_cidadao_pec, tfci.st_diabete from tb_fat_cad_individual tfci where  tfci.st_diabete = 1
),
codigos_relevantes as (
		{get_cids(diabetes_cids)}
),
max_date as (select max(co_dim_tempo::text::date) max_date from tb_fat_atendimento_individual tfai),
todos_cids as (
        select 
                tfai.co_fat_cidadao_pec, 
            regexp_replace(string_agg(tfai.ds_filtro_cids,''), '[||]+','|', 'g') cids,
            regexp_replace(string_agg(tfai.ds_filtro_ciaps,''), '[||]+','|', 'g') ciaps
        from tb_fat_atendimento_individual tfai 
        where 
                substring(co_dim_tempo::text, 0, 5)<= substring(now()::text, 0, 5)
                and
                co_dim_tempo::text::date between 
                        (select max_date from max_date) - interval '12 month' and (select max_date from max_date)
        group by tfai.co_fat_cidadao_pec
),
atendimento_individual_filtrado2 as (
        select 
                ai.*,
                ar.st_diabete,
                (
                EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE ai.cids LIKE '%' || cr.codigo || '%'
            ) 
            OR 
            EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE ai.ciaps LIKE '%' || cr.codigo || '%'
            )
        ) "cid",
        case 
                when ar.st_diabete = 1 and  (
                EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE ai.cids LIKE '%' || cr.codigo || '%'
            ) 
            OR 
            EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE ai.ciaps LIKE '%' || cr.codigo || '%'
            )
        ) = false then 'autorreferido'
        when (
                EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE ai.cids LIKE '%' || cr.codigo || '%'
            ) 
            OR 
            EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE ai.ciaps LIKE '%' || cr.codigo || '%'
            )
        ) then 'cid/ciap'
        end diagnostico
        from todos_cids ai 
        left join autoreferidos ar on ar.co_fat_cidadao_pec = ai.co_fat_cidadao_pec
        where 
        ar.st_diabete = 1 or
        (
                EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE ai.cids LIKE '%' || cr.codigo || '%'
            ) 
            OR 
            EXISTS (
                SELECT 1 
                FROM codigos_relevantes cr
                WHERE ai.ciaps LIKE '%' || cr.codigo || '%'
            )
        )
),
atendimento_individual as (
        select 
                tfai.co_fat_cidadao_pec, aif.diagnostico, tfai.co_dim_tempo::text::date, tfai.co_dim_equipe_1, tfai.co_dim_unidade_saude_1 , tfai.co_dim_cbo_1, cbo.no_cbo, cbo.nu_cbo,
                tfai.ds_filtro_proced_avaliados,tfai.ds_filtro_proced_solicitados, aif.cids, aif.ciaps
        from tb_fat_atendimento_individual tfai 
        join atendimento_individual_filtrado2 aif on aif.co_fat_cidadao_pec = tfai.co_fat_cidadao_pec
        left join tb_dim_cbo cbo on cbo.co_seq_dim_cbo = tfai.co_dim_cbo_1
        where 
                substring(co_dim_tempo::text, 0, 5)<= substring(now()::text, 0, 5)
                and
                co_dim_tempo::text::date between 
                        (select max_date from max_date) - interval '12 month' and (select max_date from max_date)
),
visita_acs as (
        select distinct
                tfvd.co_fat_cidadao_pec,
                max(tcfvd.dt_ficha::text::date) as data_ultima_visita,
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
                tcp.nu_cbo_2002 like any(array['5151%', '3233%']) and  tte.nu_ms in ('70', '76')
        group by 1
),
consulta_medico as (
        select co_fat_cidadao_pec, count(*) as total_consulta_individual_medico from atendimento_individual where nu_cbo like any (array['2251%', '2252%','2253%']) group by 1
),
consulta_enfermeiro as(
        select co_fat_cidadao_pec, count(*) as total_consulta_individual_enfermeiro from atendimento_individual where nu_cbo like any (array['2235%','2231%']) group by 1
),
ultima_consulta_medica as (
        select co_fat_cidadao_pec, max(ai.co_dim_tempo::text::date) ultimo_atendimento_medico,
        (
                extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) 
        ) meses_desde_ultima_visita_medica
        from atendimento_individual ai where nu_cbo like any (array[ '2251%', '2252%','2253%']) group by 1
),
ultima_consulta_enfermeiro as (
        select co_fat_cidadao_pec, max(ai.co_dim_tempo::text::date) ultimo_atendimento_enfermeiro,
        (
                extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) 
        ) meses_desde_ultima_visita_enfermeiro
        from atendimento_individual ai where nu_cbo like any (array['2235%', '2231%']) group by 1
),
odonto as (
        select tfao.co_fat_cidadao_pec, max(co_dim_tempo::text::date) ultimo_atendimento_odonto, (
                extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) 
        ) meses_desde_ultima_visita_odontologica from tb_fat_atendimento_odonto tfao where tfao.co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual) group by 1
),
afericao_pa as (
        select co_fat_cidadao_pec , max(co_dim_tempo::text::date) as ultima_data_afericao_pa,
        extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_afericao_pa
        from 
        tb_fat_proced_atend where ds_filtro_procedimento like '%|0301100039|%' and co_fat_cidadao_pec in ( select co_fat_cidadao_pec from atendimento_individual) group by 1
),
glicemia_capilar as (
        select distinct on (co_fat_cidadao_pec) * from (
                select 
                        co_fat_cidadao_pec , max(co_dim_tempo::text::date) as ultima_data_glicemia_capilar,
                        extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_glicemia_capilar
                from 
                        tb_fat_proced_atend where ds_filtro_procedimento like any(array['%|0214010015|%'])  group by 1
                union all 
                select 
                        co_fat_cidadao_pec , max(co_dim_tempo::text::date) as ultima_data_glicemia_capilar,
                        extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_glicemia_capilar
                from 
                        atendimento_individual where 
                        ds_filtro_proced_avaliados like  any(array['%|0214010015|%'])  group by 1
        ) lista_procedimentos
),
hemoglobina_glicada as (
        select distinct on (co_fat_cidadao_pec) * from (
                select 
                        co_fat_cidadao_pec , max(co_dim_tempo::text::date) as ultima_data_hemoglobina_glicada,
                        extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_hemoglobina_glicada
                from 
                        tb_fat_proced_atend where ds_filtro_procedimento like any(array['%|0202010503|%'])  group by 1
                union all 
                select 
                        co_fat_cidadao_pec , max(co_dim_tempo::text::date) as ultima_data_hemoglobina_glicada,
                        extract(year from age(now(), max(co_dim_tempo::text::date) ))*12 + extract(month from age(now(), max(co_dim_tempo::text::date) )) as meses_ultima_data_hemoglobina_glicada
                from 
                        atendimento_individual where 
                        ds_filtro_proced_avaliados like  any(array['%|0202010503|%'])  group by 1
        ) lista_procedimentos
),
date_range as (
        select tfai.co_fat_cidadao_pec, min(tfai.co_dim_tempo::text::date) min_date from tb_fat_atendimento_individual tfai join atendimento_individual_filtrado2 aif on aif.co_fat_cidadao_pec = tfai.co_fat_cidadao_pec group by 1
),
lista as (
        select distinct
        lci.co_fat_cidadao_pec co_fat_cidadao_pec,
        lci.diagnostico,
        tc.cids,
        tc.ciaps,
        dr.min_date,
        vacs.data_ultima_visita as data_ultima_visita_acs,
        coalesce((meses_desde_ultima_visita > 6), true) as alerta_visita_acs,
        -----
        cm.total_consulta_individual_medico,
        ce.total_consulta_individual_enfermeiro,
        (cm.total_consulta_individual_medico + ce.total_consulta_individual_enfermeiro) total_consulta_individual_medico_enfermeiro,
        ucm.ultimo_atendimento_medico,
        uce.ultimo_atendimento_enfermeiro,
        coalesce(((cm.total_consulta_individual_medico + ce.total_consulta_individual_enfermeiro) < 2), true) as alerta_total_de_consultas_medico, 
        ----
        GREATEST(ucm.ultimo_atendimento_medico, uce.ultimo_atendimento_enfermeiro) ultimo_atendimento_medico_enfermeiro,
        coalesce((GREATEST(ucm.meses_desde_ultima_visita_medica, uce.meses_desde_ultima_visita_enfermeiro )   > 6), true) as alerta_ultima_consulta_medico,
        -----
        o.ultimo_atendimento_odonto,
        coalesce((meses_desde_ultima_visita_odontologica > 6), true) as alerta_ultima_consulta_odontologica,
        -----
        pa.ultima_data_afericao_pa,
        coalesce((meses_ultima_data_afericao_pa > 6), true) as alerta_afericao_pa,
        ---
        gc.ultima_data_glicemia_capilar,
        coalesce((meses_ultima_data_glicemia_capilar > 6), true) as alerta_ultima_glicemia_capilar,
        ---
        hg.ultima_data_hemoglobina_glicada,
        coalesce((meses_ultima_data_hemoglobina_glicada > 6), true) as alerta_ultima_hemoglobina_glicada
        from 
                atendimento_individual lci
        left join 
                visita_acs vacs on vacs.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
        left join consulta_medico cm on cm.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
        join consulta_enfermeiro ce on ce.co_fat_cidadao_pec = cm.co_fat_cidadao_pec
        join ultima_consulta_medica ucm on ucm.co_fat_cidadao_pec = cm.co_fat_cidadao_pec
        join ultima_consulta_enfermeiro uce on uce.co_fat_cidadao_pec = cm.co_fat_cidadao_pec
        left join ultima_consulta_medica um on um.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
        left join odonto o on o.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
        left join afericao_pa pa on pa.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
        left join todos_cids tc on tc.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
        left join date_range dr on dr.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
        left join glicemia_capilar gc on gc.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
        left join hemoglobina_glicada hg on hg.co_fat_cidadao_pec = lci.co_fat_cidadao_pec
) 
select * from           lista l 
"""
