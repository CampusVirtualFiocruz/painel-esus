Module demographic.ibge_population_repository
=============================================
Demografia: População do IBGE.

Lê um CSV local com colunas "IBGE" e "POPULACAO" e retorna a população
formatada (ex.: 123.456) do município configurado via variável de ambiente
"CIDADE_IBGE".

Classes
-------

`IBGEPopulationRepository(csv_path: str = None)`
:   Define o caminho do CSV do IBGE. Usa "ibge.csv" no diretório atual
    por padrão.

    ### Methods

    `get_ibge_population(self)`
    :   Retorna população do município (a partir de "CIDADE_IBGE").
        
        Em falhas ou IBGE não configurado, retorna 0.