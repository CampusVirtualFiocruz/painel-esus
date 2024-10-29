QUERY_SESSAO = """{
        "query":" query sessaoQuery {
            sessao {
                id
                recursos
                profissional {
                id
                cpf
                cns
                nome
                usuario {
                    id
                    bloqueado
                }
                acessos{
                    id
                    tipo
                }
                endereco {
                    uf {
                        id
                        nome
                        sigla
                    }
                }
                lotacoes {
                    id
                    ativo
                    tipo
                    cbo {
                        id
                        nome
                        cbo2002
                    }
                    equipe {
                        id
                        nome
                    }
                    unidadeSaude {
                        id
                        nome
                        cnes
                        endereco {
                            uf {
                                id
                                nome
                                sigla
                            }
                        }
                    }
                    municipio {
                        id
                        nome
                        ibge
                    }
                    perfis {
                        id
                        nome
                        ativo
                        recursos
                        tipoPerfil
                    }
                }
                }
            }
        }",
        "variables":{
        }
}
"""
