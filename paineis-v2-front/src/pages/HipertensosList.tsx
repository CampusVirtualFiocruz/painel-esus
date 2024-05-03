import * as React from 'react';
import { useQuery } from 'react-query';
import { Header } from '../components/Header';
import { Alert, Spinner } from "reactstrap";
import { AiFillExclamationCircle, AiFillCheckCircle, AiFillCloseCircle } from "react-icons/ai";

import { Footer } from "../components/Footer";
import Pagination from "../components/Pagination";
import { Api } from "../services/api";
import "../styles/gestanteList.scss";
import "../styles/hipertensosList.scss";
import { useParams } from 'react-router-dom';
type THipertenso = {
    'Acidente Vascular Encefálico': boolean | boolean[],
    'Doença Cerebrovascular': boolean | boolean[],
    'Doença Coronariana': boolean | boolean[],
    'Doença renal': boolean | boolean[],
    'Infarto Agudo do Miocárdio': boolean | boolean[],
    'nome': string,
    'idade': number,
}

type ResponseDataListUbs = {
    data: THipertenso[];
}
type PainelParams = {
    id: string;
}

export function HipertensosList() {
    const [currentPage, setCurrentPage] = React.useState<any>(1)
    const [totalPages, setTotalPages] = React.useState<any>(1)
    const [response, setResponse] = React.useState<any>(null)
    const { id } = useParams<PainelParams>()

    const { data: hipertensosList, isLoading, error } = useQuery(['lista-hipertensos', id, currentPage], async () => {
        const total = 20;
        if (response == null) {
            let path = id ? `arterial-hypertension/get-hypertensive-list/${id}` : 'arterial-hypertension/get-hypertensive-list';

            const response = await Api.get<ResponseDataListUbs>(path)
            const data = response.data;
            console.log(response.data)
            setTotalPages(data.data.length)
            setResponse(data.data)
            return data.data.slice((currentPage - 1) * total, currentPage * total)
        } else {
            return response.slice((currentPage - 1) * total, currentPage * total)
        }
    }, {
        staleTime: 1000 * 60 * 10, //10 minutos
    });
    return (<div id="page-painel">
        <Header />

        <div className="contentWrapper">

            <hr className="linha my-4" />

            <h2>
                Lista de Hipertensos
            </h2>
            <div className="container my-5">
                {isLoading ? (
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
                    <>
                        <div className="table-responsive-md">
                            <table className="table table-striped table-bordered">
                                <thead>
                                    <tr style={{ backgroundColor: "#EEEEEE" }}>
                                        <th scope="col">Nome</th>
                                        <th scope="col">Idade</th>
                                        <th scope="col" className="text-center align-middle">Infarto Agudo do Miocárdio</th>
                                        <th scope="col" className="text-center">Doença renal</th>
                                        <th scope="col" className="text-center">Doença Coronariana:</th>
                                        <th scope="col" className="text-center">Doença Cerebrovascular</th>
                                        <th scope="col" className="text-center"> Acidente Vascular Encefálico:</th>
                                    </tr>
                                </thead>
                                <tbody className="tbody-gestantes">
                                    {hipertensosList?.map((hipertenso: THipertenso, i: number) => {
                                        return (
                                            <tr key={i}>
                                                <th className="d-flex align-items-center justify-content-between">
                                                    <span className="nomeGestante">{hipertenso.nome ?? 'NÃO CADASTRADO'}</span>
                                                </th>
                                                <td className="text-center">{hipertenso.idade ?? 'NÃO CADASTRADO'}</td>
                                                <td className="text-center">{hipertenso['Infarto Agudo do Miocárdio'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{hipertenso['Doença renal'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{hipertenso['Doença Coronariana'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{hipertenso['Doença Cerebrovascular'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{hipertenso['Acidente Vascular Encefálico'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                            </tr>
                                        )
                                    })}
                                </tbody>
                            </table>
                        </div>
                        <Pagination
                            className="pagination-bar"
                            currentPage={currentPage}
                            totalCount={totalPages}
                            pageSize={10}
                            onPageChange={page => {
                                setCurrentPage(page)
                            }}
                        />
                    </>
                )}
            </div>
        </div>
    </div>
    );
}
