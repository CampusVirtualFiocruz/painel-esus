def nominal_download(cnes: int = None, equipe: int = None):
    where_clause = " "
    if cnes is not None and cnes:
        where_clause = " where "
        where_clause += f" codigo_unidade_saude  = {cnes} "
        if equipe is not None and equipe:
            where_clause += f" and codigo_equipe  = {equipe} "
    return f"""
            SELECT
                cidadao_pec,
                nome,
                cns,
                cpf,
                sexo,
                raca_cor,
                micro_area,
                nome_equipe,
                nome_unidade_saude,
                STRFTIME( '%d/%m/%Y',data_nascimento) data_nascimento,
                idade,
                tipo_logradouro tipo_endereco,
                logradouro endereco,
                numero,
                complemento,
                bairro,
                cep,
                tipo_localizacao_domicilio tipo_localidade,
                total_consulta_medico_enfermeiro,
                STRFTIME( '%d/%m/%Y',data_ultima_consulta_medico_enfermeiro) data_ultima_consulta_medico_enfermeiro, 
                STRFTIME( '%d/%m/%Y', data_penultima_consulta_medico_enfermeiro ) data_penultima_consulta_medico_enfermeiro,
                case 
                    when agg_alerta_medicos_enfermeiros = 1 then 'SIM'
                    when agg_alerta_medicos_enfermeiros = 0 then 'NÃO'
                end alerta_medicos_enfermeiros,
                case 
                    when agg_alerta_peso_altura = 1 then 'SIM'
                    when agg_alerta_peso_altura = 0 then 'NÃO'
                end alerta_peso_altura,
                STRFTIME( '%d/%m/%Y', data_ultimo_creatinina ) data_ultimo_registro_creatinina,
                case 
                    when agg_alerta_creatinina = 1 then 'SIM'
                    when agg_alerta_creatinina = 0 then 'NÃO'
                end alerta_creatinina,
                total_visitas_domiciliares_acs,
                case 
                    when agg_alerta_visitas_domiciliares_acs = 1 then 'SIM'
                    when agg_alerta_visitas_domiciliares_acs = 0 then 'NÃO'
                end alerta_visitas_domiciliares_acs,
                STRFTIME( '%d/%m/%Y',data_ultima_vacina) data_ultima_vacina_influenza,
                case 
                    when agg_alerta_vacinas_influenza = 1 then 'SIM'
                    when agg_alerta_vacinas_influenza = 0 then 'NÃO'
                end alerta_vacinas_influenza,
                STRFTIME( '%d/%m/%Y',data_ultimo_atendendimento_odonto) data_ultimo_atendendimento_odonto,
                case 
                    when agg_alerta_cirurgiao_dentista = 1 then 'SIM'
                    when agg_alerta_cirurgiao_dentista = 0 then 'NÃO'
                end alerta_cirurgiao_dentista,
                case 
                    when agg_alerta_ivcf_aplicado = 1 then 'SIM'
                    when agg_alerta_ivcf_aplicado = 0 then 'NÃO'
                end alerta_ivcf_aplicado
            FROM read_parquet('./dados/output/idoso.parquet') 
            {where_clause}
            order by nome """