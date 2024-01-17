professionals_count_schema = {
    'data': {
        'type': 'list',
        'schema': {
                'type': 'dict',
                'schema': {
                    'profissao': {
                        'type': 'string',
                        'required': True,
                        'empty': False,
                    },
                    'total': {
                        'required': True,
                        'empty': False,
                        'type': 'float'
                    },
                    'totalCount': {
                        'required': True,
                        'empty': False,
                        'type': 'integer'
                    },
                }
        }
    }
}
