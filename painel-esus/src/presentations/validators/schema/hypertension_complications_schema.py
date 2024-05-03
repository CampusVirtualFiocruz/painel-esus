hypertension_complications_schema = {
    'data': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'valuesrules': {
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

        }
    }
}
