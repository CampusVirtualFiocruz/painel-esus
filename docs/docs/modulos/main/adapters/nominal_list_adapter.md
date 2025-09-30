Module adapters.nominal_list_adapter
====================================
Adapters para listas nominais (Crianças, Idosos, Hipertensão, Diabetes).

Transformam bases nominais em estruturas tipadas para exibição no
frontend, aplicando anonimização e compondo registros/alertas quando necessário.

Functions
---------

`is_sequence(obj)`
:   Verifica se o objeto é uma estrutura NumPy (array ou escalar).

Classes
-------

`AlertRecord(descricao: str, data, exibir_alerta, tipo_alerta: str, classificacao: str = None)`
:   Representa um registro de alerta exibido na lista nominal.

    ### Methods

    `to_dict(self)`
    :   Converte o alerta para dicionário serializável.

`BaseNominalAdapter(user)`
:   Campos e utilidades comuns às listas nominais de diferentes módulos.
    
    Inicializa campos comuns da lista nominal a partir do registro de entrada.

    ### Descendants

    * adapters.nominal_list_adapter.DiabetesNominalListAdapter
    * adapters.nominal_list_adapter.HypertensionNominalListAdapter

    ### Methods

    `get(self, item, field)`
    :   Leitura segura de campo opcional no item de entrada.

`CriancaNominalListAdapter(user: src.infra.db.entities.crianca.Crianca)`
:   Adapter de lista nominal de Crianças com regras específicas de alerta.
    
    Inicializa campos e compõe alertas específicos da lista nominal de crianças.

    ### Methods

    `check_alert(self, user, column)`
    :   Indica se há alerta (valor igual a 0).

    `check_card_alert(self, user)`
    :   Consolida presença de alertas do cartão da criança.

    `convert_nan(self, dt)`
    :   Converte NaN/None para 0 para exibição numérica.

    `get_last_height_weight_measure(self, user)`
    :   Retorna última medida de peso/altura com classificação, ou 'Não se aplica'.

    `get_numeric_data(self, user, column)`
    :   Lê coluna numérica tratando NaN/None.

    `get_yes_no_data(self, user, column)`
    :   Converte flags 0/1/99 para 'Não'/'Sim'/'Não se aplica'.

    `select_column(self, user, column)`
    :   Seleciona coluna do dicionário de entrada.

    `to_dict(self)`
    :   Retorna dicionário anonimizando dados sensíveis.

`DiabetesNominalListAdapter(user: src.infra.db.entities.diabetes_nominal.DiabetesNominal)`
:   Adapter de lista nominal de Diabetes com composição de alertas.
    
    Monta estrutura e alertas para uma pessoa com diabetes.

    ### Ancestors (in MRO)

    * adapters.nominal_list_adapter.BaseNominalAdapter

    ### Methods

    `to_dict(self)`
    :   Retorna dicionário anonimizando dados sensíveis.

`HypertensionNominalListAdapter(user)`
:   Adapter de lista nominal de Hipertensão com composição de alertas.
    
    Monta estrutura e alertas para um hipertenso.

    ### Ancestors (in MRO)

    * adapters.nominal_list_adapter.BaseNominalAdapter

    ### Methods

    `to_dict(self)`
    :   Retorna dicionário anonimizando dados sensíveis.

`IdosoNominalListAdapter(user: src.infra.db.entities.crianca.Crianca)`
:   Adapter de lista nominal de Idosos com formatação de registros/alertas.

    ### Methods

    `convert_date(self, dt)`
    :   Normaliza datas, retornando None para NaT.

    `convert_nan(self, dt)`
    :   Converte NaN para 0 para contagens.

    `to_dict(self)`
    :   Retorna dicionário anonimizando dados sensíveis.

`OralHealtNominalListAdapter(user, category: str = 'atendidas')`
:   Adapter para lista nominal de Saúde Bucal.
    
    Inicializa campos e prepara lista de alertas odontológicos.

    ### Methods

    `check_alert(self, user)`
    :   Avalia se há alertas conforme categoria selecionada.

    `convert_date(self, dt)`
    :   Normaliza datas, retornando None para NaT.

    `convert_nan(self, dt)`
    :   Converte NaN para 0 para contagens.

    `extract_procedures(self, user, column)`
    :   Extrai lista de procedimentos separados por '|' para a categoria.

    `select_column(self, user, column)`
    :   Seleciona coluna ajustada pela categoria.

    `to_dict(self)`
    :   Retorna dicionário anonimizando dados sensíveis.

`RecordNominalListAdapter(user)`
:   Adapter de lista nominal de Cadastros (Cadastro Individual).

    ### Methods

    `to_dict(self)`
    :   Retorna dicionário anonimizando dados sensíveis.