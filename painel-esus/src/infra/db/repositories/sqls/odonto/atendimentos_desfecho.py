def get_oral_health_cares_by_outcome(cnes: int = None):
    if cnes:
        return """
            with 
                desfecho as ( 
                    select
                    distinct co_seq_fat_atd_odnt ,
                    st_conduta_consulta_agendada,
                    st_conduta_outros_profissio_ab,
                    st_conduta_agendamento_nasf,
                    st_conduta_agendamento_grupos,
                    st_conduta_alta_episodio,
                    st_conduta_tratamento_concluid
                    from atendimento_odontologico ao
                    where co_dim_unidade_saude_1 = :cnes
                )
            select count(*) as total, 'Retorno por consulta agendada' as label from desfecho where st_conduta_consulta_agendada = 1
            union select count(*) as total, 'Agendamento por outros profissionais da APS' as label from desfecho where st_conduta_outros_profissio_ab = 1
            union select count(*) as total, 'Agendamento para NASF' as label from desfecho where st_conduta_agendamento_nasf = 1
            union select count(*) as total, 'Agendamento para grupos' as label from desfecho where st_conduta_agendamento_grupos = 1
            union select count(*) as total, 'Alta do episódio' as label from desfecho where st_conduta_alta_episodio = 1
            union select count(*) as total, 'Tratamento concluído' as label from desfecho where st_conduta_tratamento_concluid = 1
            ;
        """

    return """
            with 
                desfecho as ( 
                    select
                    distinct co_seq_fat_atd_odnt ,
                    st_conduta_consulta_agendada,
                    st_conduta_outros_profissio_ab,
                    st_conduta_agendamento_nasf,
                    st_conduta_agendamento_grupos,
                    st_conduta_alta_episodio,
                    st_conduta_tratamento_concluid
                    from atendimento_odontologico ao
                )
            select count(*) as total, 'Retorno por consulta agendada' as label from desfecho where st_conduta_consulta_agendada = 1
            union select count(*) as total, 'Agendamento por outros profissionais da APS' as label from desfecho where st_conduta_outros_profissio_ab = 1
            union select count(*) as total, 'Agendamento para NASF' as label from desfecho where st_conduta_agendamento_nasf = 1
            union select count(*) as total, 'Agendamento para grupos' as label from desfecho where st_conduta_agendamento_grupos = 1
            union select count(*) as total, 'Alta do episódio' as label from desfecho where st_conduta_alta_episodio = 1
            union select count(*) as total, 'Tratamento concluído' as label from desfecho where st_conduta_tratamento_concluid = 1
            ;
        """


CARES_BY_OUTCOME = get_oral_health_cares_by_outcome
