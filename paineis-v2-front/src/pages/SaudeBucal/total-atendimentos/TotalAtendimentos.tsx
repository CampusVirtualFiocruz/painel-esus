import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import { Api } from "../../../services/api";
import './style.css';
import AsyncDataLoad from "../async-data-load";

type PainelParams = {
    id: string;
}

type TotalAtendimentosResponse = {
    total: number
}

const TotalAtendimentos = () => {
    const { id } = useParams<PainelParams>();
    const { data: dataTotal, isLoading, error } = useQuery<TotalAtendimentosResponse>(['saude-bucal-total-atendimentos', id], async () => {
        const url = 'oral-health/total';
        let path = id ? `${url}/${id}` : url;
        const response = await Api.get(path);
        return response.data
    });
    return (
        <>
            <AsyncDataLoad {...{ isLoading, error }}>
                <div className="col-12 chart-container total-atd-container">
                    <h2>Total de atendimentos</h2>
                    <div className="total-atd" >
                        {dataTotal?.total.toLocaleString('pt-BR')}
                    </div>
                </div>
            </AsyncDataLoad>
        </>
    );
}

export default TotalAtendimentos;