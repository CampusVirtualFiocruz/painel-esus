import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useQuery } from "react-query";
import { Alert, Spinner } from "reactstrap";
import { Button } from "bold-ui";

import { Modal } from "../components/Modal";
import { ModalList } from "../components/ModalList";
import { Footer } from "../components/Footer";
import { getUserLocalStorage } from "../context/AuthProvider/util";
import info from "../assets/images/info-circle.svg";
import { Api } from "../services/api";
import { Header } from "../components/Header";
import { Bar } from "../charts/Bar";
import { Donut } from "../charts/Donut";
import { Pie } from "../charts/Pie";
import { getNomeUbs, showValuePerTrimester, showValuePerWeeks } from "../utils";
import { wait } from "../utils/reports";
import "../styles/gestantes.scss";

type PainelParams = {
  id: string;
};

type TModal = {
  loaded: number;
  tipo?: string;
  cnes?: string | undefined;
};

type TypeUbs = {
  label: string;
  value: number | string;
};

type Lista = {
  co_dim_unidade_saude: number;
  no_unidade_saude: string;
  nu_cnes: number;
};

type ResponseDataListUbs = {
  data: Lista[];
};

export function Gestantes() {
  let navigate = useNavigate();
  const user = getUserLocalStorage();
  const { id } = useParams<PainelParams>();

  let paramRoute = id ? id : "all";

  const [showModal, setShowModal] = useState(false);
  const [showModalList, setShowModalList] = useState(false);
  const [data, setData] = useState<TModal>({ loaded: 0 });

  const getData = async (idModal: number, tipo?: string) => {
    await wait(100);

    setData({ loaded: idModal, tipo, cnes: id });
  };

  const handleClick = (idModal: number) => {
    setData({ loaded: 0 });
    setShowModal(true);
    getData(idModal);
  };

  const handleModalList = (e: any, idModal: number, tipo: string) => {
    if (e.currentTarget === e.target) {
      setData({ loaded: idModal, tipo, cnes: id });
      setShowModalList(true);
      getData(idModal, tipo);
    }
  };

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

  const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : "-";

  const {
    data: dataTotalPerTrimester,
    isLoading: isLoadingTotalPerTrimester,
    error: errorTotalPerTrimester,
  } = useQuery(
    ["pregnants-total-per-trimester", paramRoute],
    async () => {
      let path = id
        ? `pregnants/total-per-trimester/${id}`
        : "pregnants/total-per-trimester";
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  //pregnants per weeks
  const {
    data: dataPregnantsPerWeeks,
    isLoading: isLoadingPregnantsPerWeeks,
    error: errorPregnantsPerWeeks,
  } = useQuery(
    ["pregnants-per-weeks", paramRoute],
    async () => {
      let path = id ? `pregnants/per-weeks/${id}` : "pregnants/per-weeks";
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  //prenatal indicators
  const {
    data: dataPrenatalIndicators,
    isLoading: isLoadingPrenatalIndicators,
    error: errorPrenatalIndicators,
  } = useQuery(
    ["pregnants-prenatal-indicators", paramRoute],
    async () => {
      let path = id
        ? `pregnants/prenatal-indicators/${id}`
        : "pregnants/prenatal-indicators";
      const response = await Api.get(path);
      const responseData = response.data;

      const arrData = Object.entries(responseData.data);

      return arrData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  //obstetrics factors
  const {
    data: dataObstetricsFactors,
    isLoading: isLoadingObstetricsFactors,
    error: errorObstetricsFactors,
  } = useQuery(
    ["pregnants-obstetrics-factors", paramRoute],
    async () => {
      let path = id
        ? `pregnants/obstetrics-factors/${id}`
        : "pregnants/obstetrics-factors";
      const response = await Api.get(path);
      const responseData = response.data;

      const arrData = Object.entries(responseData.data);

      return arrData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  //exams table
  const {
    data: dataExamsTable,
    isLoading: isLoadingExamsTable,
    error: errorExamsTable,
  } = useQuery(
    ["pregnants-exams-table", paramRoute],
    async () => {
      let path = id ? `pregnants/exams-table/${id}` : "pregnants/exams-table";
      const response = await Api.get(path);
      const data = response.data;

      return data.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  function handleToPainelUbs() {
    navigate(`/painel/${id}`);
  }

  function handleToPainelMunicipio() {
    navigate("/painelx");
  }

  function handleToGestantesList() {
    if (id !== undefined) {
      navigate(`/gestantes/list/${id}`);
    } else {
      navigate("/gestantes/list");
    }
  }

  return (
    <div id="page-painel">
      <Header />

      <div className="contentWrapper">
        <hr className="linha my-4" />

        <h2>
          {id
            ? !isLoadingUbs
              ? nomeUbs
              : "Carregando..."
            : user.municipio + " - " + user.uf}{" "}
          / Painel das gestantes
        </h2>

        <div className="container-fluid">
          <div className="row gx-5">
            <div className="col-12 col-lg-5">
              <div className="painel-lateral">
                <h4 className="my-5 text-center">Gestantes por faixa etária</h4>
                {isLoadingPregnantsPerWeeks ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorPregnantsPerWeeks ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Alert color="danger">Erro ao carregar dados.</Alert>
                  </div>
                ) : (
                  <Bar
                    data={dataPregnantsPerWeeks}
                    titulo="Total das gestantes do município"
                  />
                )}
              </div>

              <div className="painel-lateral situacao-exames">
                <h3 className="my-5 text-center">Situação dos exames</h3>

                <div className="row gx-4 my-3">
                  <div className="col-5 col-lg-6"></div>
                  <div className="col col-lg-3">
                    <div className="tipo p-2 text-center">
                      Solicitação pendente
                    </div>
                  </div>
                  <div className="col col-lg-3">
                    <div className="tipo p-2 text-center">
                      Avaliação pendente
                    </div>
                  </div>
                </div>

                {isLoadingExamsTable ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorExamsTable ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Alert color="danger">Erro ao carregar dados.</Alert>
                  </div>
                ) : (
                  <>
                    {dataExamsTable?.map((situacao: any, i: number) => (
                      <div key={i} className="row gx-4 my-3">
                        <div className="col-5 col-lg-6">
                          <div className="tipo p-2 bordas">{situacao.tipo}</div>
                        </div>
                        <div className="col col-lg-3">
                          <div className="tipo p-2 text-center bordas">
                            {situacao.solicitados}
                          </div>
                        </div>
                        <div className="col col-lg-3">
                          <div className="tipo p-2 text-center bordas">
                            {situacao.avaliados}
                          </div>
                        </div>
                      </div>
                    ))}
                  </>
                )}
              </div>
            </div>

            <div className="col-12 col-lg-7 d-flex flex-column justify-content-between">
              <div className="painel-lateral">
                <h4 className="my-5 text-center">Gestantes por trimestre</h4>

                <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                  {showModal && (
                    <Modal data={data} setShowModal={setShowModal} />
                  )}
                  {showModalList && (
                    <ModalList
                      params={data}
                      setShowModalList={setShowModalList}
                    />
                  )}

                  {isLoadingTotalPerTrimester ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Spinner size="sm" type="grow" className="me-2" />
                      Carregando...
                    </div>
                  ) : errorTotalPerTrimester ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Alert color="danger">Erro ao carregar dados.</Alert>
                    </div>
                  ) : (
                    <>
                      <div>
                        <div
                          className="container-trimestre"
                          onClick={(e) => handleModalList(e, 1, "trimestre")}
                        >
                          <div className="titulo d-flex align-items-center">
                            1º. trimestre{" "}
                            <img
                              src={info}
                              alt="Orientações - 1º. trimestre"
                              title="Orientações - 1º. trimestre"
                              className="info ms-2"
                              onClick={() => handleClick(1)}
                            />
                          </div>
                          <hr className="separador my-4" />
                          <span className="total-trimestre">
                            {showValuePerTrimester(
                              dataTotalPerTrimester.groupByTrimester,
                              "primeiro"
                            )}
                          </span>
                        </div>
                        <div className="mt-4">
                          <div
                            className="container-semana text-center my-2"
                            onClick={(e) => handleModalList(e, 1, "semana")}
                          >
                            1 a 12 semanas:{" "}
                            {showValuePerWeeks(
                              dataTotalPerTrimester.groupByWeeks,
                              "1 a 12 semanas"
                            )}
                          </div>
                        </div>
                      </div>

                      <div>
                        <div
                          className="container-trimestre"
                          onClick={(e) => handleModalList(e, 2, "trimestre")}
                        >
                          <div className="titulo d-flex align-items-center">
                            2º. trimestre{" "}
                            <img
                              src={info}
                              alt="Orientações - 2º. trimestre"
                              title="Orientações - 2º. trimestre"
                              className="info ms-2"
                              onClick={() => handleClick(2)}
                            />
                          </div>
                          <hr className="separador my-4" />
                          <span className="total-trimestre">
                            {showValuePerTrimester(
                              dataTotalPerTrimester.groupByTrimester,
                              "segundo"
                            )}
                          </span>
                        </div>
                        <div className="mt-4">
                          <div
                            className="container-semana text-center my-2"
                            onClick={(e) => handleModalList(e, 2, "semana")}
                          >
                            13 a 16 semanas:{" "}
                            {showValuePerWeeks(
                              dataTotalPerTrimester.groupByWeeks,
                              "13 a 16 semanas"
                            )}
                          </div>
                          <div
                            className="container-semana text-center my-2"
                            onClick={(e) => handleModalList(e, 3, "semana")}
                          >
                            17 a 20 semanas:{" "}
                            {showValuePerWeeks(
                              dataTotalPerTrimester.groupByWeeks,
                              "17 a 20 semanas"
                            )}
                          </div>
                          <div
                            className="container-semana text-center my-2"
                            onClick={(e) => handleModalList(e, 4, "semana")}
                          >
                            21 a 24 semanas:{" "}
                            {showValuePerWeeks(
                              dataTotalPerTrimester.groupByWeeks,
                              "21 a 24 semanas"
                            )}
                          </div>
                        </div>
                      </div>

                      <div>
                        <div
                          className="container-trimestre"
                          onClick={(e) => handleModalList(e, 3, "trimestre")}
                        >
                          <div className="titulo d-flex align-items-center">
                            3º. trimestre{" "}
                            <img
                              src={info}
                              alt="Orientações - 3º. trimestre"
                              title="Orientações - 3º. trimestre"
                              className="info ms-2"
                              onClick={() => handleClick(3)}
                            />
                          </div>
                          <hr className="separador my-4" />
                          <span className="total-trimestre">
                            {showValuePerTrimester(
                              dataTotalPerTrimester.groupByTrimester,
                              "terceiro"
                            )}
                          </span>
                        </div>
                        <div className="mt-4">
                          <div
                            className="container-semana text-center my-2"
                            onClick={(e) => handleModalList(e, 5, "semana")}
                          >
                            25 a 28 semanas:{" "}
                            {showValuePerWeeks(
                              dataTotalPerTrimester.groupByWeeks,
                              "25 a 28 semanas"
                            )}
                          </div>
                          <div
                            className="container-semana text-center my-2"
                            onClick={(e) => handleModalList(e, 6, "semana")}
                          >
                            29 a 32 semanas:{" "}
                            {showValuePerWeeks(
                              dataTotalPerTrimester.groupByWeeks,
                              "29 a 32 semanas"
                            )}
                          </div>
                          <div
                            className="container-semana text-center my-2"
                            onClick={(e) => handleModalList(e, 7, "semana")}
                          >
                            33 a 36 semanas:{" "}
                            {showValuePerWeeks(
                              dataTotalPerTrimester.groupByWeeks,
                              "33 a 36 semanas"
                            )}
                          </div>
                          <div
                            className="container-semana text-center my-2"
                            onClick={(e) => handleModalList(e, 8, "semana")}
                          >
                            37 a 41 semanas:
                            {showValuePerWeeks(
                              dataTotalPerTrimester.groupByWeeks,
                              "37 a 41 semanas"
                            )}
                          </div>
                        </div>
                      </div>
                    </>
                  )}
                </div>
              </div>

              <div className="painel-secundario my-2">
                <h4 className="my-4 text-center">
                  Indicadores de desempenho no Pré-Natal
                </h4>

                <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                  {isLoadingPrenatalIndicators ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Spinner size="sm" type="grow" className="me-2" />
                      Carregando...
                    </div>
                  ) : errorPrenatalIndicators ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Alert color="danger">Erro ao carregar dados.</Alert>
                    </div>
                  ) : (
                    <>
                      {dataPrenatalIndicators?.map(
                        (indicador: any, i: number) => (
                          <Donut key={i} data={indicador} />
                        )
                      )}
                    </>
                  )}
                </div>

                <div className="mt-5">
                  <Button kind="primary" onClick={() => handleClick(4)}>
                    Boas práticas na assistência do Pré-Natal
                  </Button>
                </div>
              </div>

              <div className="painel-secundario">
                <h4 className="mt-5 text-center">
                  Gestantes por antecedentes obstétricos/gerais
                </h4>

                <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                  {isLoadingObstetricsFactors ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Spinner size="sm" type="grow" className="me-2" />
                      Carregando...
                    </div>
                  ) : errorObstetricsFactors ? (
                    <div className="d-flex align-items-center justify-content-center">
                      <Alert color="danger">Erro ao carregar dados.</Alert>
                    </div>
                  ) : (
                    <>
                      {dataObstetricsFactors?.map(
                        (gestante: any, i: number) => (
                          <Pie key={i} data={gestante} />
                        )
                      )}
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
                onClick={() => handleToGestantesList()}
                className="btn btn-secondary my-2"
              >
                Ver todas as gestantes da UBS
              </button>
            </div>
          </div>
        </div>

        {/*  <div className="d-flex flex-column align-items-center mt-5 gap-3">
          {id && (
            <Button onClick={handleToPainelUbs}>
              Voltar para o Painel da UBS
            </Button>
          )}

          <Button onClick={handleToPainelMunicipio}>
            Visualizar dados do painel do Município
          </Button>
        </div> */}
      </div>

      <Footer />
    </div>
  );
}
