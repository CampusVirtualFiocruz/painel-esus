Module nominal_list.diabetes_nominal_list_repositorio
=====================================================
Criação/atualização da base nominal de Diabetes.

Consolidar e gravar a base nominal de pessoas com diabetes a partir de
diversas fontes (atendimentos, procedimentos, autoreferidos).

Classes
-------

`DiabeteNominalListRepository()`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * src.data.interfaces.create_bases.create_bases_repository.CreateBasesRepositoryInterface
    * abc.ABC

    ### Methods

    `create_base(self)`
    :   Constrói e persiste a base nominal consolidada de diabéticos.
        
        Integra autoreferidos, atendimentos (médico/enfermagem/odonto),
        aferições e hemoglobina glicada, derivando colunas de alerta e datas-chave.

    `get_afericao_pa(self)`
    :   Data da última aferição de PA e meses decorridos.

    `get_atendimento_odonto(self)`
    :   Data do último atendimento odontológico e meses decorridos.

    `get_autorreferidos(self)`
    :   Obtém pacientes autoreferidos com diabetes da base de cadastro.

    `get_creatinina(self)`
    :   Data da última creatinina (exames/procedimentos) e meses decorridos.

    `get_hemoglobina_glicada(self)`
    :   Data da última hemoglobina glicada e meses decorridos.

    `get_query(self, sql)`
    :   Executa consulta via SQLAlchemy/Polars retornando DataFrame Polars.

    `visita_acs(self)`
    :   Última visita ACS e meses desde a última visita por cidadão.