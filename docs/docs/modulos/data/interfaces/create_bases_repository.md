Module create_bases_repository
==============================
Interface para criação/atualização de bases nominais derivadas.

Usada por processos que consolidam dados do e-SUS em tabelas auxiliares
para consumo rápido pelo Painel (ex.: bases nominais de hipertensão/diabetes).

Classes
-------

`CreateBasesRepositoryInterface()`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Methods

    `create_base(self)`
    :   Gera ou atualiza a base nominal alvo, persistindo no banco local.