hypertension_complications_schema = {
    'Acidente Vascular Encefálico': {
        'type': 'dict',
        'schema': {
            'com_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'com_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
            'sem_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'sem_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
        }
    },
    'Doença Cerebrovascular': {
        'type': 'dict',
        'schema': {
            'com_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'com_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
            'sem_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'sem_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
        }
    },
    'Doença Coronariana': {
        'type': 'dict',
        'schema': {
            'com_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'com_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
            'sem_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'sem_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
        }
    },
    'Doença renal': {
        'type': 'dict',
        'schema': {
            'com_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'com_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
            'sem_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'sem_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
        }
    },
    'Infarto Agudo do Miocárdio': {
        'type': 'dict',
        'schema': {
            'com_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'com_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
            'sem_consulta': {
                'type': 'float',
                'required': True,
                'empty': False
            },
            'sem_consulta_abs': {
                'type': 'integer',
                'required': True,
                'empty': False
            },
        }
    }
}
