import { memo, useCallback, useEffect, useState } from "react";
import { useQuery } from "react-query";
import { useNavigate, useParams } from "react-router-dom";
import { DonutChart, TDonutChart } from "../../charts/Donut";
import { LineChart } from "../../charts/LineChart";
import { PieChart, TPieChart } from "../../charts/Pie";
import { StackedArea } from "../../charts/StackedArea";
import { Footer } from "../../components/Footer";
import { Header } from "../../components/Header";
import { Api as Api2} from "../../services/api";
import { Api } from "../../services/api2";
import '../../styles/sindromeAguda.scss';
import { parseChartData, filterStackAccuteCare, TResponse } from './chart-data';
import { numberFormat } from '../../utils/stringUtils'
import { Spinner, Alert } from "reactstrap";
type PainelParams = {
    id: string;
}

type TStackDataValues = {
    name: string;
    type: string;
    color: string;
    data: number[]
};
type TStackData = {
    labels: string[];
    data: any[]
    setRangeData: (args: string[]) => void
}

type ParsedChartData = {
    totalInfeccoesRespiratorias: number;
    totalInfeccoesIntestinais: number;
    totalFebreExantematicas: number;
    totalFebreInespecificas: number;
    totalAtendimentosPorSindromesAgudas: number;
    totalAtendimentosPorOutrosCasos: number;
}
const MemoStackArea = memo(function MemoStackArea(stackData: any) {
    return <StackedArea {...stackData} />
});


type LoadingData = {
    frequency: boolean;
    stackData: boolean;
    donut: boolean;
    lineChart: boolean
}
export function SindromesAgudas() {
    let navigate = useNavigate();
    const [loading, setLoading] = useState(true);
    const [infecaoRespiratoriaState, setInfecaoRespiratoriaState] = useState<number>(0);
    const [infecaoIntestinalState, setInfecaoIntestinalState] = useState<number>(0);
    const [febreExantematicaState, setFebreExantematicaState] = useState<number>(0);
    const [febreInespecificaState, setFebreInespecificaState] = useState<number>(0);
    const [totalAtendimentosState, setTotalAtendimentosState] = useState<number>(0);
    const [totalAtendimentosAgudosState, setTotalAtendimentosAgudosState] = useState<number>(0);
    const [totalOutrosAtendimentosState, setTotalOutrosAtendimentosState] = useState<number>(0);
    const [stackData, setStackData] = useState<TStackData>({
        labels: [],
        data: [],
        setRangeData: () => { }
    });
    const [lineData, setLineData] = useState<TStackData>({
        labels: [],
        data: [],
        setRangeData: () => { }
    });
    const [rangeData, setRangeData] = useState<string[]>([]);
    const [responseData, setResponseData] = useState<TResponse[]>([]);
    const [isLoadingData, setLoadingData] = useState<LoadingData>({
        frequency: true,
        stackData: true,
        donut: true,
        lineChart: true,
    })

    const { id } = useParams<PainelParams>();
    const { data: sindromesAgudasData, isLoading, error } = useQuery(['sindromes-agudas', id], async () => {
        // let path = id ? `pregnants/exams-table/${id}` : 'pregnants/exams-table';
        let path = '/data/get-chart-data.json';
        const response = await Api.get(path);
        let data = response.data.data;
        if (id) {
            data = data.filter((item: TResponse) => item.nu_cnes == id)
        }
        handleSindromeAgudaData(data);
        handleStackData(data);
        setResponseData(data)
        return data;
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const handleSindromeAgudaData = useCallback((response: TResponse[]) => {
        setLoadingData((prev: LoadingData) => ({
            ...prev,
            frequency: true,
            donut: true,
            lineChart: true,
        }));
        if (response == undefined || response.length == 0) return;
        const parsedData: ParsedChartData = parseChartData(response) as ParsedChartData;
        setFebreExantematicaState(parsedData.totalFebreExantematicas);
        setFebreInespecificaState(parsedData.totalFebreInespecificas);
        setInfecaoIntestinalState(parsedData.totalInfeccoesIntestinais);
        setInfecaoRespiratoriaState(parsedData.totalInfeccoesRespiratorias);

        setTotalOutrosAtendimentosState(parsedData.totalAtendimentosPorOutrosCasos);
        setTotalAtendimentosAgudosState(parsedData.totalAtendimentosPorSindromesAgudas);

        setTotalAtendimentosState(

            (parsedData.totalAtendimentosPorOutrosCasos + parsedData.totalAtendimentosPorSindromesAgudas)
        );
        console.log('response', response)
        setLoadingData((prev: LoadingData) => ({
            ...prev,
            frequency: false,
            donut: false,
            lineChart: false,
        }))
    }, [])

    function handleStackData(response: TResponse[]) {
        setLoadingData((prev: LoadingData) => ({
            ...prev,
            stackData: true
        }));

        const accuteFiltred = filterStackAccuteCare(response);

        setStackData({
            labels: accuteFiltred.labels,
            data: accuteFiltred.stack.slice(0,
                -2),
            setRangeData: setRangeData
        });
        setLineData({
            labels: accuteFiltred.labels,
            data: [
                {
                    name: 'Outros atendimentos',
                    type: 'outros atendimentos',
                    color: '#5cd2c8fc',
                    data: accuteFiltred.stack[4].data
                },
                {
                    name: 'Atendimentos por síndromes agudas',
                    type: 'atendimentos por sindrome agudas',
                    color: '#09406a',
                    data: accuteFiltred.stack[5].data
                }],
            setRangeData: setRangeData
        });
        setLoadingData((prev: LoadingData) => ({
            ...prev,
            stackData: false
        }));
    }
    const filterRange = useCallback(() => {
        const startDate = new Date(rangeData[0]);
        const endDate = new Date(rangeData[1]);
        return responseData.filter((item: TResponse) => {
            const itemDate = new Date(item.time);
            return itemDate >= startDate && itemDate <= endDate
        })
    }, [rangeData[0], rangeData[1]]);

    useEffect(() => {
        let filteredData = []
        filteredData = filterRange();
        handleSindromeAgudaData(filteredData);
    }, [rangeData[0], rangeData[1]]);

    function handleToHome() {
        setLoading(true);
        navigate('/painelx');
    }

    return (
        <div id="page-painel">
            <Header />

            <div className="contentWrapper">

                <hr className="linha my-4" />

                <h2>
                    Painel Sindromes Agudas
                </h2>

                <div className="container-fluid">
                    <div className="row gx-5">
                        <div className="col-12 col-lg-5">
                            <div className="painel-lateral">
                                {/* <h4 className="my-5 text-center">Frequência de atendimentos por síndrome aguda</h4> */}
                                <h4 className="my-5 text-center">Frequência de sintomas por atendimentos</h4>
                                {isLoadingData.frequency ? (
                                    <div className="d-flex my-5 align-items-center justify-content-center">
                                        <Spinner className="me-2" />
                                        Carregando...
                                    </div>
                                ) : error ? (
                                    <div className="d-flex my-5 align-items-center justify-content-center">
                                        <Alert color="danger">
                                            Erro ao carregar dados.
                                        </Alert>
                                    </div>
                                ) : (
                                    <div className="row gx-5  d-flex-center">
                                        <div className="col-12 col-lg-5">
                                            <PieChart {...new TPieChart(
                                                'Infeccoes respiratórias',
                                                [
                                                    { value: infecaoRespiratoriaState },
                                                    { value: totalAtendimentosAgudosState },
                                                ],
                                                '#5cd2c8'
                                            )} />
                                        </div>
                                        <div className="col-12 col-lg-5">
                                            <PieChart {...new TPieChart(
                                                'Infeccoes Intestinais',
                                                [
                                                    { value: infecaoIntestinalState },
                                                    { value: totalAtendimentosAgudosState },
                                                ],
                                                '#3996c1'
                                            )} />
                                        </div>
                                        <div className="col-12 col-lg-5 mt-10">
                                            <PieChart {...new TPieChart(
                                                'Febres Exantemáticas',
                                                [
                                                    { value: febreExantematicaState },
                                                    { value: totalAtendimentosAgudosState },
                                                ],
                                                '#2775b0'
                                            )} />
                                        </div>
                                        <div className="col-12 col-lg-5 mt-10">
                                            <PieChart {...new TPieChart(
                                                'Febres Inespecíficas',
                                                [
                                                    { value: febreInespecificaState },
                                                    { value: totalAtendimentosAgudosState },
                                                ],
                                                '#09406a'
                                            )} />
                                        </div>
                                    </div>
                                )}

                            </div>
                        </div>

                        <div className="col-12 col-lg-7 ">
                            <div className="painel-lateral">
                                <h4 className="my-5 text-center">Relação de atendimentos por síndrome aguda</h4>
                                {isLoadingData.stackData ? (
                                    <div className="d-flex my-5 align-items-center justify-content-center">
                                        <Spinner className="me-2" />
                                        Carregando...
                                    </div>
                                ) : error ? (
                                    <div className="d-flex my-5 align-items-center justify-content-center">
                                        <Alert color="danger">
                                            Erro ao carregar dados.
                                        </Alert>
                                    </div>
                                ) : (
                                    <MemoStackArea {...stackData} />
                                )}
                            </div>
                        </div>

                        <div className="col-12 col-lg-4 label-container " style={{ marginTop: 30 }}>
                            <div className="label">
                                Número de atendimentos por síndromes agudas
                            </div>
                            {isLoadingData.frequency ? (
                                <div className="d-flex my-5 align-items-center justify-content-center">
                                    <Spinner className="me-2" />
                                    Carregando...
                                </div>
                            ) : error ? (
                                <div className="d-flex my-5 align-items-center justify-content-center">
                                    <Alert color="danger">
                                        Erro ao carregar dados.
                                    </Alert>
                                </div>
                            ) : (
                                <div className="label-value">{numberFormat(totalAtendimentosAgudosState)}</div>
                            )}
                        </div>

                    </div>
                </div>

                <div className="container-fluid">
                    <div className="row gx-5">
                        <div className="col-12 col-lg-5">
                            <div className="painel-lateral">
                                <h4 className="my-5 text-center">Relação de atendimentos por outras causas x sídromes agudas</h4>
                            </div>
                            {isLoadingData.donut ? (
                                <div className="d-flex my-5 align-items-center justify-content-center">
                                    <Spinner className="me-2" />
                                    Carregando...
                                </div>
                            ) : error ? (
                                <div className="d-flex my-5 align-items-center justify-content-center">
                                    <Alert color="danger">
                                        Erro ao carregar dados.
                                    </Alert>
                                </div>
                            ) : (
                                <div className="col-12">
                                    <DonutChart {...new TDonutChart(
                                        'Febres Inespecíficas',
                                        [
                                            { value: totalOutrosAtendimentosState, name: 'Atendimentos por outras causas' },
                                            { value: totalAtendimentosAgudosState, name: 'Atendimentos por síndromes agudas' },
                                        ],
                                        '#5cd2c8'
                                    )} />
                                </div>
                            )}

                        </div>

                        <div className="col-12 col-lg-7" >
                            <div className="painel-lateral">
                                <h4 className="my-5 text-center">Comparativo do volume de atendimentos gerais em relacao às síndromes  agudas</h4>
                                {isLoadingData.lineChart ? (
                                    <div className="d-flex my-5 align-items-center justify-content-center">
                                        <Spinner className="me-2" />
                                        Carregando...
                                    </div>
                                ) : error ? (
                                    <div className="d-flex my-5 align-items-center justify-content-center">
                                        <Alert color="danger">
                                            Erro ao carregar dados.
                                        </Alert>
                                    </div>
                                ) : (
                                    <LineChart {...lineData} />
                                )}
                            </div>
                        </div>
                        <div className="col-12 col-lg-4 label-container">
                            <div className="label" style={{ display: 'flex', 'justifyContent': 'center' }}>
                                Total de atendimentos
                            </div>
                            <div className="label-value">{numberFormat(totalAtendimentosState)}</div>
                        </div>
                    </div>
                    <div className="row gx-5">
                        <div className="col-12 col-lg-12 d-flex-center">
                            <button
                                type="button"
                                onClick={handleToHome}
                                className="btn btn-primary">
                                Voltar
                            </button>
                        </div>
                    </div>
                </div>


            </div>

            <Footer />
        </div>
    );
}
