LISTA_CIDS_CIAPS_POR_CIDADAO_PEC = """
SELECT 
    tfai.co_fat_cidadao_pec, 
    regexp_replace(string_agg(tfai.ds_filtro_cids, tfai.ds_filtro_ciaps), '[ | |]+','|', 'g') as cids  
FROM 
    tb_fat_atendimento_individual tfai 
GROUP BY tfai.co_fat_cidadao_pec"""
