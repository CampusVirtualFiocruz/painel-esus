import * as React from 'react';
import { useQuery } from 'react-query';
import { Header } from '../components/Header';
import { Alert, Spinner } from "reactstrap";
import { AiFillCheckCircle, AiFillCloseCircle } from "react-icons/ai";

import Pagination from "../components/Pagination";
import { Api } from "../services/api";
import "../styles/gestanteList.scss";
import "../styles/hipertensosList.scss";
type TDiabetico = {
    'Retinopatia diabética': boolean,
    'Doença renal': boolean,
    'Doença Coronariana': boolean,
    'Doença Cerebrovascular': boolean,
    'Neuropatia': boolean,
    'Doença Arterial Oclusiva': boolean,
    'nome': string,
    'idade': number,
}

type ResponseDataListUbs = {
    data: TDiabetico[];
}
export function DiabeticosList() {
    const [currentPage, setCurrentPage] = React.useState<any>(1)
    const [totalPages, setTotalPages] = React.useState<any>(1)
    const [response, setResponse] = React.useState<any>(null)
    const { data: diabeticosList, isLoading, error } = useQuery(['lista-diabeticos', currentPage], async () => {
        const total = 20;
        if (response == null) {
            const response = await Api.get<ResponseDataListUbs>('get-diabetes-list')
            const data = response.data;
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
                Lista de pacientes com Diabetes
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
                                        <th scope="col" className="text-center">Retinopatia diabética</th>
                                        <th scope="col" className="text-center">Doença renal</th>
                                        <th scope="col" className="text-center">Doença Coronariana</th>
                                        <th scope="col" className="text-center">Doença Cerebrovascular</th>
                                        <th scope="col" className="text-center">Neuropatia</th>
                                        <th scope="col" className="text-center">Doença Arterial Oclusiva</th>
                                    </tr>
                                </thead>
                                <tbody className="tbody-gestantes">
                                    {diabeticosList?.map((diabetico: TDiabetico, i: number) => {
                                        return (
                                            <tr key={i}>
                                                <th className="d-flex align-items-center justify-content-between">
                                                    <span className="nomeGestante">{diabetico.nome ?? 'NÃO CADASTRADO'}</span>
                                                </th>
                                                <td className="text-center">{diabetico.idade ?? 'NÃO CADASTRADO'}</td>
                                                <td className="text-center">{diabetico['Retinopatia diabética'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{diabetico['Doença renal'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{diabetico['Doença Coronariana'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{diabetico['Doença Cerebrovascular'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{diabetico['Neuropatia'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
                                                <td className="text-center">{diabetico['Doença Arterial Oclusiva'] ? <AiFillCheckCircle className="green" /> : <AiFillCloseCircle className="red" />}</td>
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
