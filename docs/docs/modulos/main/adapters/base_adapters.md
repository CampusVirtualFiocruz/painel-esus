Module adapters.adapters
========================
Adapters base para formatar respostas para o frontend.

Os adapters aqui definidos transformam resultados brutos em estruturas
padronizadas, reduzindo acoplamento entre as camadas de dados e apresentação.

Classes
-------

`AbstractAdapter()`
:   Base para adapters com utilitários de hidratação/formatação.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Descendants

    * adapters.adapters.DemographicAdapter

    ### Methods

    `total_adapter(self, response) ‑> adapters.adapters.TypeTotal`
    :

`DemographicAdapter()`
:   Adapter de Demografia para totais, tipos de localidade, pirâmide etária e sexo.

    ### Ancestors (in MRO)

    * adapters.adapters.AbstractAdapter
    * abc.ABC

    ### Methods

    `age_group_pyramid(self, response)`
    :

    `gender_apadter(self, response)`
    :

    `location_type_adapter(self, response)`
    :

    `total_adapter(self, response) ‑> adapters.adapters.TypeTotal`
    :

`TypeTotal(*args, **kwargs)`
:   dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `data: int`
    :