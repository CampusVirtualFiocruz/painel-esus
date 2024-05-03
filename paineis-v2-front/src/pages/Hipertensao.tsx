import { useNavigate, useParams } from "react-router-dom";
import { useQuery } from "react-query";
import { Alert, Progress, Spinner } from "reactstrap";

import { Footer } from "../components/Footer";
import { getUserLocalStorage } from "../context/AuthProvider/util";

import { Modal } from '../components/Modal';

import info from "../assets/images/people.svg";

import "../styles/diabetesHipertensao.scss";
import { Api } from "../services/api";
import { Header } from "../components/Header";

import { Bar } from "../charts/Bar";
import { Donut } from "../charts/Donut";
import { Pie } from "../charts/Pie";
import { getNomeUbs } from "../utils";
import { useState } from "react";
import { BarSexo } from "../charts/BarSexo";

type TModal = {
    loaded: number;
    tipo?: string;
    cnes?: string | undefined
}

type PainelParams = {
    id: string;
}

type TypeUbs = {
    label: string;
    value: number | string;
};

type Lista = {
    co_dim_unidade_saude_1: number;
    no_unidade_saude: string;
    nu_cnes: number;
}

type ResponseDataListUbs = {
    data: Lista[];
}

export function Hipertensao() {
    let navigate = useNavigate();
    const user = getUserLocalStorage();
    const { id } = useParams<PainelParams>();
    const [showModal, setShowModal] = useState(false);
    const [data, setData] = useState<TModal>({ loaded: 0 });

    let paramRoute = id ? id : 'all';

    const wait = (milliseconds: number) => {
        return new Promise((resolve) => setTimeout(resolve, milliseconds));
    };

    const getData = async (idModal: number, tipo?: string) => {
        await wait(100);
        setData({ loaded: idModal, tipo, cnes: id });
    };

    //get nome ubs
    const { data: dataUbs, isLoading: isLoadingUbs } = useQuery('ubs', async () => {
        const response = await Api.get<ResponseDataListUbs>('get-units')
        const data = response.data

        const listData: TypeUbs[] = data.data.map((ubs) => {
            return {
                "label": ubs.no_unidade_saude,
                "value": ubs.nu_cnes,
            }
        })

        return listData
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : '-';

    const { data: dataTotalHipertensao, isLoading: isLoadingTotalHipertensao, error: errorTotalHipertensao } = useQuery(['arterial-hypertension/total', paramRoute], async () => {
        let path = id ? `arterial-hypertension/total/${id}` : 'arterial-hypertension/total';
        const response = await Api.get(path);
        const responseData = response.data;

        let total = responseData.data;

        return total.toLocaleString('pt-BR');
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const { data: dataHipertensao, isLoading: isLoadingHipertensao, error: errorHipertensao } = useQuery(['arterial-hypertension-age-group-location', paramRoute], async () => {
        let path = id ? `arterial-hypertension/age-group-location/${id}` : 'arterial-hypertension/age-group-location';
        const response = await Api.get(path);
        const responseData = response.data;

        return responseData.data;
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const { data: dataHipertensaoAgeGroupGender, isLoading: isLoadingHipertensaoAgeGroupGender, error: errorHipertensaoAgeGroupGender } = useQuery(['arterial-hypertension-age-group-gender', paramRoute], async () => {
        let path = id ? `arterial-hypertension/age-group-gender/${id}` : 'arterial-hypertension/age-group-gender';
        const response = await Api.get(path);
        const responseData = response.data;

        return responseData.data;
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const { data: dataHipertensaoIndicators, isLoading: isLoadingHipertensaoIndicators, error: errorHipertensaoIndicators } = useQuery(['arterial-hypertension-complications', paramRoute], async () => {
        let path = id ? `arterial-hypertension/complications/${id}` : 'arterial-hypertension/complications';
        const response = await Api.get(path);
        const responseData = response.data;
        console.log(responseData)

        const arrData = responseData.data.map((item: any, i: number) => {
            let obj = Object.entries(item);
            return [obj[0][0], obj[0][1]]
        });

        return arrData;
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const { data: dataHipertensaoFactors, isLoading: isLoadingHipertensaoFactors, error: errorHipertensaoFactors } = useQuery(['arterial-hypertension-imc', paramRoute], async () => {
        let path = id ? `arterial-hypertension/imc/${id}` : 'arterial-hypertension/imc';
        const response = await Api.get(path);
        const responseData = response.data;

        return responseData.data;
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const { data: dataExamsTable, isLoading: isLoadingExamsTable, error: errorExamsTable } = useQuery(['arterial-hypertension-exams', paramRoute], async () => {
        let path = id ? `arterial-hypertension/exams/${id}` : 'arterial-hypertension/exams';
        const response = await Api.get(path);
        const data = response.data;

        return data.data;
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    const { data: dataProffessionals, isLoading: isLoadingProffessionals, error: errorProffessionals } = useQuery(['arterial-hypertension-proffessionals', paramRoute], async () => {
        let path = id ? `arterial-hypertension/professionals/${id}` : 'arterial-hypertension/professionals';
        const response = await Api.get(path);
        const data = response.data;

        return data.data;
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    function handleToPainelUbs() {
        navigate(`/painel/${id}`);
    }

    function handleToPainelMunicipio() {
        navigate("/painelx");
    }

    const handleClick = (idModal: number) => {
        setData({ loaded: 0 });
        setShowModal(true);
        getData(idModal);
    };

    const random_hex_color_code = () => {
        let n = (Math.random() * 0x361949 * 1000000).toString(16);
        return '#' + n.slice(0, 6);
    };

    const handleToHipertensosList = () => {
        navigate(`/hipertensos/${id}`)
    }
    return (
        <div id="page-painel">
            <Header />

            <div className="contentWrapper">

                <hr className="linha my-4" />

                <h2>
                    {id ? (!isLoadingUbs ? nomeUbs : 'Carregando...') : user.municipio + " - " + user.uf} / Painel Hipertensão
                </h2>

                {showModal && <Modal data={data} setShowModal={setShowModal} />}

                <div className="container-fluid">
                    <div className="row gx-5">
                        <div className="col-12 col-lg-5">
                            <div className="painel-lateral">
                                <h4 className="mt-5 text-center">Pessoas com hipertensão por faixa etária</h4>
                                {isLoadingHipertensao ? (
                                    <div className="d-flex align-items-center justify-content-center">
                                        <Spinner size="sm" type="grow" className="me-2" />
                                        Carregando...
                                    </div>
                                ) : errorHipertensao ? (
                                    <div className="d-flex align-items-center justify-content-center">
                                        <Alert color="danger">
                                            Erro ao carregar dados.
                                        </Alert>
                                    </div>
                                ) : (
                                    <Bar data={dataHipertensao} titulo="Total de pessoas com hipertensão no município" />
                                )}
                            </div>

                            <div className="painel-lateral">
                                <h4 className="mt-5 text-center">Pessoas com hipertensão por sexo</h4>
                                {isLoadingHipertensaoAgeGroupGender ? (
                                    <div className="d-flex align-items-center justify-content-center">
                                        <Spinner size="sm" type="grow" className="me-2" />
                                        Carregando...
                                    </div>
                                ) : errorHipertensaoAgeGroupGender ? (
                                    <div className="d-flex align-items-center justify-content-center">
                                        <Alert color="danger">
                                            Erro ao carregar dados.
                                        </Alert>
                                    </div>
                                ) : (
                                    <BarSexo data={dataHipertensaoAgeGroupGender} titulo="Total de pessoas com hipertensão no município" />
                                )}
                            </div>

                            <div className="painel-lateral situacao-exames">
                                <h3 className="my-5 text-center">Situação dos exames nos últimos 12 meses</h3>

                                <div className="row gx-4 my-3">
                                    <div className="col-5 col-lg-6">

                                    </div>
                                    <div className="col col-lg-3">
                                        <div className="tipo p-2 text-center">Solicitação pendente</div>
                                    </div>
                                    <div className="col col-lg-3">
                                        <div className="tipo p-2 text-center">Avaliação pendente</div>
                                    </div>
                                </div>

                                {isLoadingExamsTable ? (
                                    <div className="d-flex align-items-center justify-content-center">
                                        <Spinner size="sm" type="grow" className="me-2" />
                                        Carregando...
                                    </div>
                                ) : errorExamsTable ? (
                                    <div className="d-flex align-items-center justify-content-center">
                                        <Alert color="danger">
                                            Erro ao carregar dados.
                                        </Alert>
                                    </div>
                                ) : (
                                    <>
                                        {dataExamsTable?.map((situacao: any, i: number) => (
                                            <div key={i} className="row gx-4 my-3">
                                                <div className="col-5 col-lg-6">
                                                    <div className="tipo p-2 bordas">{situacao.tipo}</div>
                                                </div>
                                                <div className="col col-lg-3">
                                                    <div className="tipo p-2 text-center bordas">{situacao.solicitados}</div>
                                                </div>
                                                <div className="col col-lg-3">
                                                    <div className="tipo p-2 text-center bordas">{situacao.avaliados}</div>
                                                </div>
                                            </div>
                                        ))}
                                    </>
                                )}
                            </div>
                        </div>

                        <div className="col-12 col-lg-7 d-flex flex-column">
                            <div className="painel-lateral">
                                <h4 className="mt-5 mb-4 text-center">Total de atendimento nos últimos 12 meses</h4>

                                <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                                    <div>
                                        <div className="container-atendimentos">
                                            <div className="titulo d-flex align-items-center">
                                                <img src={info} alt="Total de atendimento nos últimos 12 meses" className="info mx-2" />
                                            </div>
                                            <span className="total-trimestre ms-4">
                                                {isLoadingTotalHipertensao ? (
                                                    <div className="d-flex align-items-center justify-content-center">
                                                        <Spinner size="sm" type="grow" className="me-2" />
                                                        0
                                                    </div>
                                                ) : errorTotalHipertensao ? (
                                                    <div className="d-flex align-items-center justify-content-center">
                                                        <Alert color="danger">
                                                            Erro ao carregar dados.
                                                        </Alert>
                                                    </div>
                                                ) : dataTotalHipertensao
                                                }
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div className="painel-secundario my-2">
                                <h4 className="my-4 text-center">Frequência de complicações relacionadas à hipertensão</h4>

                                <div className="d-flex flex-wrap flex-xl-nowrap justify-content-center">
                                    {isLoadingHipertensaoIndicators ? (
                                        <div className="d-flex align-items-center justify-content-center">
                                            <Spinner size="sm" type="grow" className="me-2" />
                                            Carregando...
                                        </div>
                                    ) : errorHipertensaoIndicators ? (
                                        <div className="d-flex align-items-center justify-content-center">
                                            <Alert color="danger">
                                                Erro ao carregar dados.
                                            </Alert>
                                        </div>
                                    ) : (
                                        <>
                                            {dataHipertensaoIndicators?.map((indicador: any, i: number) => <Donut key={i} data={indicador} />)}
                                        </>
                                    )}
                                </div>

                                <button
                                    type="button"
                                    onClick={() => handleClick(5)}
                                    className="btn btn-primary mt-5">
                                    Boas práticas na assistência a pessoas com hipertensão
                                </button>
                            </div>

                            <div className="painel-secundario">
                                <h4 className="mt-5 mb-4 text-center">Adultos com hipertensão de acordo com o IMC</h4>

                                <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                                    {isLoadingHipertensaoFactors ? (
                                        <div className="d-flex align-items-center justify-content-center">
                                            <Spinner size="sm" type="grow" className="me-2" />
                                            Carregando...
                                        </div>
                                    ) : errorHipertensaoFactors ? (
                                        <div className="d-flex align-items-center justify-content-center">
                                            <Alert color="danger">
                                                Erro ao carregar dados.
                                            </Alert>
                                        </div>
                                    ) : (
                                        <>
                                            {dataHipertensaoFactors?.map((diabete: any, i: number) => <Pie key={i} data={diabete} />)}
                                        </>
                                    )}
                                </div>
                            </div>

                            <div className="painel-secundario">
                                <h4 className="mt-5 mb-4 text-center">Extratificação de atendimentos por profissional</h4>
                                <div className="w-100">
                                    {isLoadingProffessionals ? (
                                        <div className="d-flex align-items-center justify-content-center">
                                            <Spinner size="sm" type="grow" className="me-2" />
                                            Carregando...
                                        </div>
                                    ) : errorProffessionals ? (
                                        <div className="d-flex align-items-center justify-content-center">
                                            <Alert color="danger">
                                                Erro ao carregar dados.
                                            </Alert>
                                        </div>
                                    ) : (
                                        <>
                                            {dataProffessionals?.map((item: any, i: number) => (
                                                <div key={i} className="d-flex align-items-center mt-2">
                                                    <div className="container-extratificacao-atendimentos">
                                                        <span className="profissao-nome">{item.profissao}</span>
                                                        <Progress value={item.total} className="w-75" barStyle={{ backgroundColor: random_hex_color_code() }} />
                                                    </div>
                                                    <span className="total ms-2">{item.total}%</span>
                                                </div>
                                            ))}
                                        </>
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="row my-5 text-center">
                        <div className="col-12">
                            <button
                                type="button"
                                onClick={() => handleToHipertensosList()}
                                className="btn btn-secondary my-2">
                                Ver todos Hipertensos
                            </button>
                        </div>
                    </div>
                </div>

                <div className="d-flex flex-column align-items-center mt-5">
                    {id &&
                        <button
                            type="button"
                            onClick={handleToPainelUbs}
                            className="btn btn-light my-2">
                            Voltar para o Painel da UBS
                        </button>
                    }
                    <button
                        type="button"
                        onClick={handleToPainelMunicipio}
                        className="btn btn-primary my-4">
                        Visualizar dados do painel do Município
                    </button>
                </div>
            </div>

            <Footer />
        </div>
    )
}
