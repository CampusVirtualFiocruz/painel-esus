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
                    cbo {
                        id
                        nome
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