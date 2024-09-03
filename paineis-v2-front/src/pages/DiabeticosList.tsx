import * as React from "react";
import { useQuery } from "react-query";
import { Header } from "../components/Header";
import { Alert, Spinner } from "reactstrap";
import {
  AiFillExclamationCircle,
  AiFillCheckCircle,
  AiFillCloseCircle,
} from "react-icons/ai";

import { Footer } from "../components/Footer";
import Pagination from "../components/Pagination";
import { Api } from "../services/api";
import "../styles/gestanteList.scss";
import "../styles/ListaNominal.scss";
type TDiabetico = {
  Glicemia: number[];
  "Hemoglobina glicada": number[];
  Retinografia: number[];
  Creatinina: number[];
  "EAS/EQU (urina rotina)": number[];
  Hemograma: number[];
  "Aferição de PA": number[];
  "Colesterol total": number[];
  "Doença Arterial Oclusiva": number[];
  nome: string;
  idade: number;
};

type ResponseDataListUbs = {
  data: TDiabetico[];
};
export function DiabeticosList() {
  const [currentPage, setCurrentPage] = React.useState<any>(1);
  const [totalPages, setTotalPages] = React.useState<any>(1);
  const [response, setResponse] = React.useState<any>(null);
  const {
    data: diabeticosList,
    isLoading,
    error,
  } = useQuery(
    ["lista-diabeticos", currentPage],
    async () => {
      const total = 20;
      if (response == null) {
        const response = await Api.get<ResponseDataListUbs>(
          "get-diabetes-list"
        );
        const data = response.data;
        setTotalPages(data.data.length);
        setResponse(data.data);
        return data.data.slice((currentPage - 1) * total, currentPage * total);
      } else {
        return response.slice((currentPage - 1) * total, currentPage * total);
      }
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  function handleIcons(row: number[]) {
    console.log(row);

    const icons = [
      <>
        <small>Solicitado</small>
        <AiFillCheckCircle className="green" />
      </>,
      <>
        <small>Avaliado</small>
        <AiFillCheckCircle className="green" />
      </>,
    ];
    if (!row) return icons;

    if (row[0] == 1) {
      icons[0] = (
        <>
          <small>Solicitado</small>
          <AiFillCloseCircle className="red" />
        </>
      );
    }
    if (row[1] == 1) {
      icons[1] = (
        <>
          <small>Avaliado</small>
          <AiFillCloseCircle className="red" />
        </>
      );
    }
    return icons;
  }
  return (
    <div id="page-painel">
      <Header />

      <div className="contentWrapper">
        <hr className="linha my-4" />

        <h2>Lista de pacientes com Diabetes</h2>
        <div className="container my-5">
          {isLoading ? (
            <div className="d-flex my-5 align-items-center justify-content-center">
              <Spinner className="me-2" />
              Carregando...
            </div>
          ) : error ? (
            <div className="d-flex my-5 align-items-center justify-content-center">
              <Alert color="danger">Erro ao carregar dados.</Alert>
            </div>
          ) : (
            <>
              <div className="table-responsive-md">
                <table className="table table-striped table-bordered">
                  <thead>
                    <tr style={{ backgroundColor: "#EEEEEE" }}>
                      <th scope="col">Nome</th>
                      <th scope="col">Idade</th>
                      <th scope="col" className="text-center">
                        Glicemia
                      </th>
                      <th scope="col" className="text-center">
                        Hemoglobina glicada
                      </th>
                      <th scope="col" className="text-center">
                        Retinografia
                      </th>
                      <th scope="col" className="text-center">
                        Creatinina
                      </th>
                      <th scope="col" className="text-center">
                        EAS/EQU (urina rotina)
                      </th>
                      <th scope="col" className="text-center">
                        Hemograma
                      </th>
                      <th scope="col" className="text-center">
                        Aferição de PA
                      </th>
                      <th scope="col" className="text-center">
                        Colesterol total
                      </th>
                      <th scope="col" className="text-center">
                        Doença Arterial Oclusiva
                      </th>
                    </tr>
                  </thead>
                  <tbody className="tbody-gestantes">
                    {diabeticosList?.map((diabetico: TDiabetico, i: number) => {
                      return (
                        <tr key={i}>
                          <th className="d-flex align-items-center justify-content-between">
                            <span className="nomeGestante">
                              {diabetico.nome ?? "NÃO CADASTRADO"}
                            </span>
                          </th>
                          <td className="text-center">
                            {diabetico.idade ?? "NÃO CADASTRADO"}
                          </td>
                          <td className="text-center">
                            {handleIcons(diabetico["Glicemia"]).map((i) => i)}
                          </td>
                          <td className="text-center">
                            {handleIcons(diabetico["Hemoglobina glicada"]).map(
                              (i) => i
                            )}
                          </td>
                          <td className="text-center">
                            {handleIcons(diabetico["Retinografia"]).map(
                              (i) => i
                            )}
                          </td>
                          <td className="text-center">
                            {handleIcons(diabetico["Creatinina"]).map((i) => i)}
                          </td>
                          <td className="text-center">
                            {handleIcons(
                              diabetico["EAS/EQU (urina rotina)"]
                            ).map((i) => i)}
                          </td>
                          <td className="text-center">
                            {handleIcons(diabetico["Hemograma"]).map((i) => i)}
                          </td>
                          <td className="text-center">
                            {handleIcons(diabetico["Aferição de PA"]).map(
                              (i) => i
                            )}
                          </td>
                          <td className="text-center">
                            {handleIcons(diabetico["Colesterol total"]).map(
                              (i) => i
                            )}
                          </td>
                          <td className="text-center">
                            {handleIcons(
                              diabetico["Doença Arterial Oclusiva"]
                            ).map((i) => i)}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
              <Pagination
                className="pagination-bar"
                currentPage={currentPage}
                totalCount={totalPages}
                pageSize={10}
                onPageChange={(page) => {
                  setCurrentPage(page);
                }}
              />
            </>
          )}
        </div>
      </div>
    </div>
  );
}
