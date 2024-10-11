MAX_DATE = """
SELECT 
    tfai.co_fat_cidadao_pec, 
    max(tfai.co_dim_tempo)::text::date as max_date  
FROM 
    tb_fat_atendimento_individual tfai 
GROUP BY tfai.co_fat_cidadao_pec 
order by co_fat_cidadao_pec asc
"""
