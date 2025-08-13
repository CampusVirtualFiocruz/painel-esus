import { useNavigate, useParams } from "react-router-dom";
import { useQuery } from "react-query";

import { Alert, Spinner } from "reactstrap";
import { AiFillExclamationCircle } from "react-icons/ai";

import { Header } from "../components/Header";
import { Footer } from "../components/Footer";
import Pagination from "../components/Pagination";

import { Api } from "../services/api";
import { getUserLocalStorage } from "../context/AuthProvider/util";
import { getNomeUbs, ReportBasicParams } from "../utils";

import "../styles/gestanteList.scss";
import { useState } from "react";

type Lista = {
  co_dim_unidade_saude: number;
  no_unidade_saude: string;
  nu_cnes: number;
};

type TypeUbs = {
  label: string;
  value: number | string;
};

type ResponseDataListUbs = {
  data: Lista[];
};

type TGestante = {
  nome: string | undefined;
  co_dim_tempo: string;
  co_fat_cidadao_pec: number;
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
};

export function tipoResidencia(tipo: string) {
  if (tipo === "Urbano") {
    return (
      <div className="iconCircle iconUrbano ms-2" title="Urbano">
        U
      </div>
    );
  } else if (tipo === "Rural") {
    return (
      <div className="iconCircle iconRural ms-2" title="Rural">
        R
      </div>
    );
  } else {
    return "";
  }
}

export function temPendencias(tipo: boolean) {
  if (!tipo) {
    return (
      <AiFillExclamationCircle
        size={"1.2rem"}
        className="aviso"
        title="Pendências"
      />
    );
  }

  return "";
}

export function GestantesList() {
  let navigate = useNavigate();
  const { id } = useParams<ReportBasicParams>();
  const user = getUserLocalStorage();
  let paramRoute = id ? id : "all";
  const [currentPage, setCurrentPage] = useState<any>(1);

  //get nome ubs
  const { data: dataUbs, isLoading: isLoadingUbs } = useQuery(
    "ubs",
    async () => {
      const response = await Api.get<ResponseDataListUbs>("get-units");
      const data = response.data;

      const listData: TypeUbs[] = data.data.map((ubs: any) => {
        return {
          label: ubs.no_unidade_saude,
          value: ubs.co_seq_dim_unidade_saude,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  //get nome ubs
  const nomeUbs = id && !isLoadingUbs ? getNomeUbs(dataUbs, id) : "-";

  const { isLoading, error, data } = useQuery(
    ["pregnants-table", paramRoute, currentPage],
    async () => {
      let path = id
        ? `pregnants/pregnants-table/${id}?page=${currentPage}`
        : `pregnants/pregnants-table?page=${currentPage}`;

      const response = await Api.get(path);
      const { data, total }: any = response.data;

      return { gestantes: data, total: total };
    },
    {
      keepPreviousData: true,
      cacheTime: 600000,
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  function handleToGestante(gestante: TGestante) {
    navigate(`/gestante/${gestante.co_fat_cidadao_pec}`);
  }

  function handleToPainelGestante() {
    if (id !== undefined) {
      navigate(`/gestantes/${id}`);
    } else {
      navigate("/gestantes");
    }
  }

  return (
    <div id="page-painel">
      <Header />

      <div className="contentWrapper">
        <hr className="linha my-4" />

        <div>
          <h2>
            {id
              ? !isLoadingUbs
                ? nomeUbs
                : "Carregando..."
              : user.municipio + " - " + user.uf}{" "}
            / Lista das gestantes
          </h2>
          <p className="text-end fw-bold">(referente aos últimos 12 meses)</p>
        </div>

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
                      <th scope="col" className="text-center align-middle">
                        Idade
                      </th>
                      <th scope="col" className="text-center">
                        IG 1ª Consulta
                      </th>
                      <th scope="col" className="text-center">
                        Total de Consultas
                      </th>
                      <th scope="col" className="text-center">
                        Tem Diabetes
                      </th>
                      <th scope="col" className="text-center">
                        Tem Has
                      </th>
                      <th scope="col" className="text-center">
                        Exame VDRL e Anti HIV
                      </th>
                      <th scope="col" className="text-center">
                        Consulta Odontológica
                      </th>
                      <th scope="col" className="text-center">
                        Esquema Vacinal
                      </th>
                    </tr>
                  </thead>
                  <tbody className="tbody-gestantes">
                    {data?.gestantes.map((gestante: TGestante, i: number) => {
                      return (
                        <tr key={i}>
                          <th
                            onClick={() => handleToGestante(gestante)}
                            className="d-flex align-items-center justify-content-between"
                          >
                            <span className="nomeGestante">
                              {gestante.nome ?? "NÃO CADASTRADO"}
                            </span>
                            <div className="d-flex">
                              {temPendencias(gestante.pendencia)}
                              {tipoResidencia(gestante.tipoResidencia)}
                            </div>
                          </th>
                          <td className="text-center">
                            {gestante.idade ?? "NÃO CADASTRADO"}
                          </td>
                          <td className="text-center">
                            {gestante.igPrimeiraConsulta ?? 0}
                          </td>
                          <td className="text-center">
                            {gestante.totalConsultas ?? 0}
                          </td>
                          <td className="text-center">
                            {gestante.temDiabetes ?? "NÃO CADASTRADO"}
                          </td>
                          <td className="text-center">
                            {gestante.temHas ?? "NÃO CADASTRADO"}
                          </td>
                          <td className="text-center">
                            {gestante.exameVdrlAntiHiv ?? "NÃO CADASTRADO"}
                          </td>
                          <td className="text-center">
                            {gestante.consultaOdonto ?? "NÃO CADASTRADO"}
                          </td>
                          <td className="text-center">
                            {gestante.esquemaVacinal ?? "NÃO CADASTRADO"}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
                <div className="mb-2">
                  <p className="text-end mb-0 small">
                    <AiFillExclamationCircle
                      size={"1.3rem"}
                      className="mb-1 me-2 aviso"
                    />
                    Pendências: Socilitação de exame, avaliação de exames ou
                    esquema vacina incompleto.
                  </p>
                </div>
              </div>
              <Pagination
                className="pagination-bar"
                currentPage={currentPage}
                totalCount={data?.total}
                pageSize={10}
                onPageChange={(page) => setCurrentPage(page)}
              />
            </>
          )}
        </div>

        <div className="d-flex flex-column containerButtons align-items-center gap-3">
          {!isLoading && (
            <button
              type="button"
              onClick={() => {}}
              disabled
              className="btn btn-primary my-5"
            >
              Exportar lista
            </button>
          )}
          <button
            type="button"
            onClick={handleToPainelGestante}
            className="btn btn-light mb-5"
          >
            Voltar para o Painel de Gestantes
          </button>
        </div>
      </div>
      <Footer />
    </div>
  );
}
