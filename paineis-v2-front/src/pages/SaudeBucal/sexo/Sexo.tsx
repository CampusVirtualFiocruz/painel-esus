import * as React from 'react';
import './style.scss';
import { useQuery } from 'react-query';
import { Api } from '../../../services/api';
import { STALE_TIME } from '../../../config/stale-time';
import { BarChart, FaixaEtariaResponse, PainelParams } from '../faixa-etaria/FaixaEtaria';
import { useParams } from 'react-router-dom';
import AsyncDataLoad from '../async-data-load';


type sexoResponse = FaixaEtariaResponse;
const Sexo = () => {

    const { id } = useParams<PainelParams>();
    const { data: sexoResponse, isLoading, error } = useQuery(
        ['saude-bucal-sexo', id],
        async () => {
            const url = 'oral-health/get-cares-by-gender'
            const path = id ? `${url}/${id}` : url;
            const response = await Api.get<sexoResponse[]>(path);
            return response.data
        },
        {
            staleTime: STALE_TIME
        }
    );
    return (<AsyncDataLoad {...{ isLoading, error }}>
        <div className="col-12">
            <h2 >Atendimentos em Saúde Bucal por sexo</h2>
            {!isLoading && sexoResponse && <BarChart  {...{ data: sexoResponse, titulo: 'Total de atendimentos' }} />}
        </div>
    </AsyncDataLoad>);
}

export default Sexo;