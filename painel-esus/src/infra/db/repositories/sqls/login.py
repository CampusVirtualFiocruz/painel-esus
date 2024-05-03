LOGIN = """
select
        distinct on (tfai.co_dim_unidade_saude_1) co_dim_unidade_saude_1 as  unidadeSaude,
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
    join tb_dim_profissional tdp on
        tp.nu_cns = tdp.nu_cns
    join tb_fat_atendimento_individual tfai on tfai.co_dim_profissional_1  = tdp.co_seq_dim_profissional 
    join tb_dim_municipio tbm on tbm.co_seq_dim_municipio = tfai.co_dim_municipio 
    join tb_dim_uf tduf on tduf.co_seq_dim_uf = tbm.co_dim_uf	
    where
        tdp.st_registro_valido = 1
        and tp.nu_cpf = :username
        and concat( tp.nu_cns , :password_salt) = :password;
"""