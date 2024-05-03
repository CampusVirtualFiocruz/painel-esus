import * as React from 'react';
import { DonutChart, TDonutChart } from "../../../charts/Donut";
import { useParams } from 'react-router-dom';
import { PainelParams } from '../faixa-etaria/FaixaEtaria';
import { useQuery } from 'react-query';
import { Api } from '../../../services/api';
import { STALE_TIME } from '../../../config/stale-time';
import AsyncDataLoad from '../async-data-load';

type TipoAtentimentoResponse = {
    label: string;
    value: number;
    total: number;
};

const TipoConsulta = () => {
    const { id } = useParams<PainelParams>();
    const { data: tipoResponse, isLoading, error } = useQuery(
        ['saude-bucal-tipo-consulta', id],
        async () => {
            const url = 'oral-health/cares-by-type-of-services'
            let path = id ? `${url}/${id}` : url;
            const response = await Api.get<TipoAtentimentoResponse[]>(path);
            const res = response.data?.map((item: TipoAtentimentoResponse) => ({ value: item.value, name: item.label }))
            console.log(res)
            return res
        },
        {
            staleTime: STALE_TIME
        }
    );
    return (<AsyncDataLoad {...{ isLoading, error }}>
        <div className="col-12 chart-container total-atd-container">
            <h2>Cuidado em saude bucal por tipo de consulta</h2>
            <DonutChart {...new TDonutChart(
                '',
                tipoResponse || [],
                '#5cd2c8'
            )} />
        </div>
    </AsyncDataLoad>);
}

export default TipoConsulta;
