Module city_informations_repository
===================================
Informações do município e de suas unidades/equipes.

Responsabilidades principais:
- Buscar dados gerais do município (código IBGE, UF, CEP etc.).
- Listar unidades de saúde.
- Listar equipes associadas às unidades.

Quando a variável de ambiente "MOCK=True" estiver definida, métodos
retornarão dados fictícios úteis para desenvolvimento e testes.

Classes
-------

`AlchemyEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)`
:   Encoder JSON para serializar modelos do SQLAlchemy.
    
    Converte instâncias de modelos em dicionários
    JSON-serializáveis, ignorando atributos não serializáveis.
    
    Constructor for JSONEncoder, with sensible defaults.
    
    If skipkeys is false, then it is a TypeError to attempt
    encoding of keys that are not str, int, float or None.  If
    skipkeys is True, such items are simply skipped.
    
    If ensure_ascii is true, the output is guaranteed to be str
    objects with all incoming non-ASCII characters escaped.  If
    ensure_ascii is false, the output can contain non-ASCII characters.
    
    If check_circular is true, then lists, dicts, and custom encoded
    objects will be checked for circular references during encoding to
    prevent an infinite recursion (which would cause an RecursionError).
    Otherwise, no such check takes place.
    
    If allow_nan is true, then NaN, Infinity, and -Infinity will be
    encoded as such.  This behavior is not JSON specification compliant,
    but is consistent with most JavaScript based encoders and decoders.
    Otherwise, it will be a ValueError to encode such floats.
    
    If sort_keys is true, then the output of dictionaries will be
    sorted by key; this is useful for regression tests to ensure
    that JSON serializations can be compared on a day-to-day basis.
    
    If indent is a non-negative integer, then JSON array
    elements and object members will be pretty-printed with that
    indent level.  An indent level of 0 will only insert newlines.
    None is the most compact representation.
    
    If specified, separators should be an (item_separator, key_separator)
    tuple.  The default is (', ', ': ') if *indent* is ``None`` and
    (',', ': ') otherwise.  To get the most compact JSON representation,
    you should specify (',', ':') to eliminate whitespace.
    
    If specified, default is a function that gets called for objects
    that can't otherwise be serialized.  It should return a JSON encodable
    version of the object or raise a ``TypeError``.

    ### Ancestors (in MRO)

    * json.encoder.JSONEncoder

    ### Methods

    `default(self, obj)`
    :   Implement this method in a subclass such that it returns
        a serializable object for ``o``, or calls the base implementation
        (to raise a ``TypeError``).
        
        For example, to support arbitrary iterators, you could
        implement default like this::
        
            def default(self, o):
                try:
                    iterable = iter(o)
                except TypeError:
                    pass
                else:
                    return list(iterable)
                # Let the base class default method raise the TypeError
                return super().default(o)

`CityInformationsRepository()`
:   Implementação do repositório de informações da cidade.
    
    Fornece operações para recuperar informações do município, unidades de
    saúde e equipes.

    ### Ancestors (in MRO)

    * src.data.interfaces.city_information_repository.CityInformationRepository
    * abc.ABC

    ### Methods

    `get_city_info(self, cnes: int = None) ‑> Dict`
    :   Obtém informações gerais do município.
        
        Retorna DataFrame com colunas como "municipio", "cep",
           "codibge", "uf" e "estado".

    `get_teams(self, cnes: int = None)`
    :   Lista de equipes de saúde.

    `get_units(self) ‑> Dict`
    :   Lista unidades de saúde do município.
        
        Retorna DataFrame com a listagem de unidades.

    `get_units_with_patients(self) ‑> Dict`
    :   Lista unidades de saúde com agregação de pacientes.
        
        Retorna DataFrame com unidades e informações agregadas de pacientes.