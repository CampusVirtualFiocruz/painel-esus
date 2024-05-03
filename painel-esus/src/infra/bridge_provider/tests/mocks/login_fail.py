#pylint: disable=line-too-long
import pytest

@pytest.fixture
def login_fail_response():
    return {
        "errors":[
            {
                "message":"Usuário ou senha incorretos. Após 10 tentativas o seu login será bloqueado.",
                "locations":[
                ],
                "extensions":{
                    "classification":"BadCredentialsException"
                }
            }
        ],
        "extensions":{
            "tracing":{
                "version":1,
                "startTime":"2023-09-17T01:32:04.790Z",
                "endTime":"2023-09-17T01:32:04.897Z",
                "duration":107064138,
                "parsing":{
                    "startOffset":1811099,
                    "duration":1724672
                },
                "validation":{
                    "startOffset":2823265,
                    "duration":959695
                },
                "execution":{
                    "resolvers":[
                    {
                        "path":[
                            "login"
                        ],
                        "parentType":"Mutation",
                        "returnType":"LoginPayload!",
                        "fieldName":"login",
                        "startOffset":3589262,
                        "duration":100809095
                    }
                    ]
                }
            }
        },
        "data":None
}
