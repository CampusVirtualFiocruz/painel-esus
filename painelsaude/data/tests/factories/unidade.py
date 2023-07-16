from ...entities.unidade_saude import UnidadeSaude, Cidade

def unidade_factory( unidade_saude: int = 1):
    cidade = Cidade(
        co_ibge=1,
        co_municipio=1,
        no_municipio='FIOCRUZLÂNDIA',
        no_uf='FC',
        sg_uf='FC'
    )
    if unidade_saude == 1:
        unidade = UnidadeSaude(
            co_unidade_saude=1,
            ds_unidade_saude='Oswaldo Cruz',
            cnes=1,
            cidade=cidade
        )
    elif unidade_saude == 2:
        unidade = UnidadeSaude(
            co_unidade_saude=2,
            ds_unidade_saude='Carlos Chagas',
            cnes=2,
            cidade=cidade
        )
    
    return unidade