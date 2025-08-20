LOGIN = """
select
        distinct on (tfai.co_dim_unidade_saude_1) co_dim_unidade_saude_1 as  unidadeSaude,
        tfai.co_dim_equipe_1 equipe,
        tcp.nu_cbo_2002,
        tbm.co_ibge as  codigoIbge,
        tbm.no_municipio as municipio,
        tduf.sg_uf as uf,  
        tp.nu_cns as cns,
        tp.nu_cpf as cpf,
        tp.nu_conselho_classe  as conselhoClasse,
        tp.ds_email as email,
        tdp.no_profissional as nome,
        tfai.co_dim_municipio as codigoMunicipio
    from
        tb_prof tp
    left join tb_dim_profissional tdp on
        tp.nu_cns = tdp.nu_cns
    left join tb_cds_prof tcp on tcp.nu_cns=tdp.nu_cns
    left join tb_fat_atendimento_individual tfai on tfai.co_dim_profissional_1  = tdp.co_seq_dim_profissional 
    left join tb_dim_municipio tbm on tbm.co_seq_dim_municipio = tfai.co_dim_municipio 
    left join tb_dim_uf tduf on tduf.co_seq_dim_uf = tbm.co_dim_uf	
    where
        tdp.st_registro_valido = 1
        and tp.nu_cpf = :username
        and concat( tp.nu_cns , :password_salt) = :password;
"""

LOGIN_CPF = """
select
        distinct on (tfai.co_dim_unidade_saude_1) co_dim_unidade_saude_1 as  unidadeSaude,
        tp.nu_cns as cns,
        tcp.nu_ine,
		tcp.nu_cnes,
        tde.no_equipe,
        tdus.no_unidade_saude,
        tfai.co_dim_equipe_1 equipe,
        tcp.nu_cbo_2002        
    from
        tb_prof tp
    left join tb_dim_profissional tdp on
        tp.nu_cns = tdp.nu_cns
    left join tb_cds_prof tcp on tcp.nu_cns=tdp.nu_cns
    left join tb_fat_atendimento_individual tfai on tfai.co_dim_profissional_1  = tdp.co_seq_dim_profissional 
    left join tb_dim_municipio tbm on tbm.co_seq_dim_municipio = tfai.co_dim_municipio 
    left join tb_dim_uf tduf on tduf.co_seq_dim_uf = tbm.co_dim_uf	
    left join tb_dim_equipe tde on tde.nu_ine = tcp.nu_ine
    left join tb_dim_unidade_saude tdus on tdus.nu_cnes = tcp.nu_cnes
    where
        tdp.st_registro_valido = 1
        and tp.nu_cpf = :username;
"""
