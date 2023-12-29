import * as React from 'react';
import { useParams } from 'react-router-dom';
import { BarChart, FaixaEtariaResponse, PainelParams } from '../faixa-etaria/FaixaEtaria';
import { useQuery } from 'react-query';
import { Api } from '../../../services/api';
import { STALE_TIME } from '../../../config/stale-time';
import AsyncDataLoad from '../async-data-load';

type LocalAtentimentoResponse = FaixaEtariaResponse;

const LocalAtendimento = () => {
    const { id } = useParams<PainelParams>();
    const { data: sexoResponse, isLoading, error } = useQuery(
        ['saude-bucal-local-atendimento', id],
        async () => {
            const url = 'oral-health/get-cares-by-place';
            const path = id ? `${url}/${id}` : url
            const response = await Api.get<LocalAtentimentoResponse[]>(path);
            return response.data
        },
        {
            staleTime: STALE_TIME
        }
    );
    return (<AsyncDataLoad {...{ isLoading, error }}>
        <div className="col-12">
            <h2 >Saúde Bucal por local de atendimento</h2>
            {!isLoading && sexoResponse && <BarChart  {...{ data: sexoResponse, titulo: 'Total de atendimentos' }} />}
        </div>
    </AsyncDataLoad>);
}

export default LocalAtendimento;