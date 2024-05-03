import { useNavigate, useParams } from "react-router-dom";
import { useQuery } from "react-query";
import { Alert, Spinner } from "reactstrap";
import moment from 'moment';

import { Header } from "../components/Header";
import { Footer } from "../components/Footer";

import { Api } from "../services/api";
import "../styles/gestante.scss";
import { cpfMask } from "../utils";

type PainelParams = {
    id: string;
}

type TGestante = {
    nome: string | undefined;
    dataNascimento: string | undefined;
    cpf: string;
    co_dim_tempo: string;
    co_fat_cidadao_pec: number,
    consultaOdonto: string;
    esquemaVacinal: string;
    exameVdrlAntiHiv: string;
    idade: number;
    igPrimeiraConsulta: number;
    pendencia: boolean;
    temDiabetes: string;
    temHas: string;
    tipoResidencia: string;
    totalConsultas: number;
}

export function Gestante() {
    let navigate = useNavigate();
    const { id } = useParams<PainelParams>();
    const txtNaoCadastrado = 'NÃO CADASTRADO'

    const { data, isLoading, error } = useQuery<TGestante>(['pregnants-by-id', id], async () => {
        const response = await Api.get(`pregnants/by-id/${id}`);
        const data = response.data;

        return data.data;
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });

    function handleToGestante() {
        navigate('/gestantes/list');
    }

    function idadeEmAnosEmMeses(date: string | undefined) {
        if (date) {
            let m = moment(date, "YYYY-MM-DD");
            let years = moment().diff(m, 'years', false);
            let months = moment().diff(m.add(years, 'years'), 'months', false)

            return `${years} anos e ${months} meses`
        }

        return 'NÃO CADASTRADO'
    }

    return (
        <div id="page-gestante">
            <Header />

            {isLoading ? (
                <div className="contentWrapperLoading">
                    <Spinner color="#343131" className="me-2" /> Carregando dados da gestante...
                </div>
            ) : error ? (
                <div className="contentWrapperError">
                    <Alert color="danger">
                        Erro ao carregar dados da gestante.
                    </Alert>
                </div>
            ) : (
                <>
                    <div className="contentGestanteWrapper">
                        <div className="container">
                            <div className="row justify-content-center">
                                <div className="col-12 col-md-8">
                                    <hr className="linha my-4" />
                                    <h1>{data?.nome ?? txtNaoCadastrado}</h1>
                                    <p className="fw-bold mb-4">CPF: {cpfMask(data?.cpf)}</p>
                                    <p>{idadeEmAnosEmMeses(data?.dataNascimento)}</p>
                                    <p>{/*11 semanas de gestação*/} {txtNaoCadastrado}</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="contentWrapper">
                        <div className="container">
                            <div className="row justify-content-center mb-2">
                                <div className="col-12 col-md-8">
                                    <h2>PENDÊNCIAS IDENTIFICADAS</h2>
                                    <ul>
                                        {/*
                                        <li className="mb-1">Verificar vacinas.</li>
                                        <li className="mb-1">Verificar solicitação do VDRL.</li>
                                        <li className="mb-1">Verificar resultado do VDRL.</li>
                                        <li className="mb-1">Menos de 6 consultas de pré-natal realizadas - verificar idade gestacional e acompanhar.</li>
                                        <li className="mb-1">Encaminhar para consulta odontológica.</li>
                                        */}

                                        <li className="mb-1">NÃO CONSTA</li>
                                    </ul>
                                </div>
                            </div>
                            <div className="row justify-content-center mb-2">
                                <div className="col-12 col-md-8">
                                    <h2>Outras informações relevantes:</h2>
                                    <ul>
                                        {/*
                                        <li className="mb-1">Data do último atendimento: 23 de abril de 2021.</li>
                                        <li className="mb-1">Maria da Fonseca Silva tem 3 gestações prévias.</li>
                                        <li className="mb-1">Partos prévios: 2.</li>
                                        */}
                                        <li className="mb-1">NÃO CONSTA</li>
                                    </ul>
                                </div>
                            </div>
                            <div className="row justify-content-center mb-2">
                                <div className="col-12 col-md-8">
                                    <h2>Exames e/ou procedimentos realizados nos últimos 6 meses:</h2>
                                    <ul>
                                        {/*
                                        <li className="mb-1">Ultrassonografia obstétrica</li>
                                        <li className="mb-1">EAS</li>
                                        <li className="mb-1">Hemograma completo</li>
                                        <li className="mb-1">Colesterol total</li>
                                        <li className="mb-1">Sorologia para HIV</li>
                                        */}
                                        <li className="mb-1">NÃO CONSTA</li>
                                    </ul>
                                </div>
                            </div>
                            <div className="row justify-content-center mb-2">
                                <div className="col-12 col-md-8">
                                    <h2>Exames e/ou procedimentos solicitados nos últimos 6 meses:</h2>
                                    <ul>
                                        {/*
                                        <li className="mb-1">Ultrassonografia obstétrica</li>
                                        <li className="mb-1">Hemograma completo</li>
                                        <li className="mb-1">Sorologia para Sífilis (VDRL)</li>
                                        */}
                                        <li className="mb-1">NÃO CONSTA</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <div className="container">
                            <div className="row justify-content-center mb-2">
                                <div className="col-12 col-md-8 containerButtons d-flex justify-content-center my-5">
                                    <button
                                        type="button"
                                        onClick={handleToGestante}
                                        className="btn btn-light me-5">
                                        Voltar
                                    </button>

                                    <button
                                        type="button"
                                        onClick={() => { }}
                                        disabled
                                        className="btn btn-primary">
                                        Imprimir
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </>
            )}

            <Footer />
        </div>
    )
}
