Module nominal_list.hypertension_nominal_list_repository
========================================================
Criação/atualização da base nominal de Hipertensão.

Consolidar e gravar a base nominal de hipertensos a partir de
diversas fontes (atendimentos, procedimentos, autoreferidos).

Classes
-------

`HypertensionNominalListRepository()`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * src.data.interfaces.create_bases.create_bases_repository.CreateBasesRepositoryInterface
    * abc.ABC

    ### Methods

    `create_base(self)`
    :   Constrói e persiste a base nominal consolidada de hipertensos.
        
        Integra autoreferidos, atendimentos (médico/enfermagem/odonto),
        aferições e creatinina, derivando colunas de alerta e datas-chave.

    `get_afericao_pa(self)`
    :   Data da última aferição de PA e meses decorridos.

    `get_atendimento_odonto(self)`
    :   Data do último atendimento odontológico e meses decorridos.

    `get_autorreferidos(self)`
    :   Obtém pacientes autoreferidos com hipertensão da base de cadastro.

    `get_creatinina(self)`
    :   Data da última creatinina e meses decorridos.

    `get_query(self, sql)`
    :   Executa consulta via SQLAlchemy/Polars retornando DataFrame Polars.

    `visita_acs(self)`
    :   Última visita de ACS e meses desde a última visita por cidadão.