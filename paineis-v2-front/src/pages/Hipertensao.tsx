import { useState } from "react";
import { useParams } from "react-router-dom";
import { useQuery } from "react-query";
import { Alert, Progress, Spinner } from "reactstrap";
import { Button } from "bold-ui";

import { Modal } from "../components/Modal";
import { Typography } from "../components/ui/Typography";
import info from "../assets/images/people.svg";
import "../styles/diabetesHipertensao.scss";
import { Api } from "../services/api";
import { Bar } from "../charts/Bar";
import { Donut } from "../charts/Donut";
import { Pie } from "../charts/Pie";
import { capitalize, getNomeUbs } from "../utils";
import { BarSexo } from "../charts/BarSexo";
import { useInfo } from "../context/infoProvider/useInfo";
import { randomHexColorCode, wait } from "../utils/reports";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import TwoColumnSection from "../components/ui/TwoColumnSection";

type TModal = {
  loaded: number;
  tipo?: string;
  cnes?: string | undefined;
};

type PainelParams = {
  id: string;
};

export function Hipertensao() {
  const { id } = useParams<PainelParams>();
  const [showModal, setShowModal] = useState(false);
  const [data, setData] = useState<TModal>({ loaded: 0 });
  const { cityInformation } = useInfo();

  let paramRoute = id ? id : "all";

  const getData = async (idModal: number, tipo?: string) => {
    await wait(100);
    setData({ loaded: idModal, tipo, cnes: id });
  };

  const {
    data: dataTotalHipertensao,
    isLoading: isLoadingTotalHipertensao,
    error: errorTotalHipertensao,
  } = useQuery(
    ["arterial-hypertension/total", id],
    async () => {
      let path = id
        ? `arterial-hypertension/total/${id}`
        : "arterial-hypertension/total";
      const response = await Api.get(path);
      const responseData = response.data;

      let total = responseData.data;

      return total;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataHipertensao,
    isLoading: isLoadingHipertensao,
    error: errorHipertensao,
  } = useQuery(
    ["arterial-hypertension-age-group-location", paramRoute],
    async () => {
      let path = id
        ? `arterial-hypertension/age-group-location/${id}`
        : "arterial-hypertension/age-group-location";
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataHipertensaoAgeGroupGender,
    isLoading: isLoadingHipertensaoAgeGroupGender,
    error: errorHipertensaoAgeGroupGender,
  } = useQuery(
    ["arterial-hypertension-age-group-gender", paramRoute],
    async () => {
      let path = id
        ? `arterial-hypertension/age-group-gender/${id}`
        : "arterial-hypertension/age-group-gender";
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataHipertensaoIndicators,
    isLoading: isLoadingHipertensaoIndicators,
    error: errorHipertensaoIndicators,
  } = useQuery(
    ["arterial-hypertension-complications", paramRoute],
    async () => {
      let path = id
        ? `arterial-hypertension/complications/${id}`
        : "arterial-hypertension/complications";
      const response = await Api.get(path);
      const responseData = response.data;

      const arrData = responseData.data.map((item: any, i: number) => {
        let obj = Object.entries(item);
        return [obj[0][0], obj[0][1]];
      });

      return arrData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataHipertensaoFactors,
    isLoading: isLoadingHipertensaoFactors,
    error: errorHipertensaoFactors,
  } = useQuery(
    ["arterial-hypertension-imc", paramRoute],
    async () => {
      let path = id
        ? `arterial-hypertension/imc/${id}`
        : "arterial-hypertension/imc";
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataExamsTable,
    isLoading: isLoadingExamsTable,
    error: errorExamsTable,
  } = useQuery(
    ["arterial-hypertension-exams", paramRoute],
    async () => {
      let path = id
        ? `arterial-hypertension/exams/${id}`
        : "arterial-hypertension/exams";
      const response = await Api.get(path);
      const data = response.data;

      return data.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataProfessionals,
    isLoading: isLoadingProfessionals,
    error: errorProfessionals,
  } = useQuery(
    ["arterial-hypertension-professionals", paramRoute],
    async () => {
      let path = id
        ? `arterial-hypertension/professionals/${id}`
        : "arterial-hypertension/professionals";
      const response = await Api.get(path);
      const data = response.data;

      return data.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const handleClick = (idModal: number) => {
    setData({ loaded: 0 });
    setShowModal(true);
    getData(idModal);
  };

  const { city } = useInfo();

  const { data: dataUbs, isLoading: isLoadingUbs } = useQuery(
    "ubs",
    async () => {
      const response = await Api.get<any>("get-units");
      const data = response.data;

      const listData: any[] = data.data.map((ubs: any) => {
        return {
          label: ubs.no_unidade_saude,
          value: ubs.co_seq_dim_unidade_saude,
          id: ubs.co_seq_dim_unidade_saude,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const nomeUbs = !isLoadingUbs && id ? getNomeUbs(dataUbs, id) : city;
  const UBS = id ? (!isLoadingUbs ? nomeUbs : "Carregando...") : nomeUbs;
  const title = `${UBS} / Hipertensão`;

  return (
    <div id="page-painel-diabetes-hipertensao">
      {showModal && <Modal data={data} setShowModal={setShowModal} />}
      <ReportWrapper title={title}>
        <TwoColumnSection>
          <TwoColumnSection.Col>
            <div className="painel-lateral">
              <Typography.Subtitle>
                Pessoas com hipertensão por faixa etária
              </Typography.Subtitle>
              {isLoadingHipertensao ? (
                <div className="d-flex align-items-center justify-content-center">
                  <Spinner size="sm" type="grow" className="me-2" />
                  Carregando...
                </div>
              ) : errorHipertensao ? (
                <div className="d-flex align-items-center justify-content-center">
                  <Alert color="danger">Erro ao carregar dados.</Alert>
                </div>
              ) : (
                <Bar
                  data={dataHipertensao}
                  titulo="Total de pessoas com hipertensão no município"
                />
              )}
            </div>
            <div className="painel-lateral">
              <Typography.Subtitle>
                Pessoas com hipertensão por sexo
              </Typography.Subtitle>
              {isLoadingHipertensaoAgeGroupGender ? (
                <div className="d-flex align-items-center justify-content-center">
                  <Spinner size="sm" type="grow" className="me-2" />
                  Carregando...
                </div>
              ) : errorHipertensaoAgeGroupGender ? (
                <div className="d-flex align-items-center justify-content-center">
                  <Alert color="danger">Erro ao carregar dados.</Alert>
                </div>
              ) : (
                <BarSexo
                  data={dataHipertensaoAgeGroupGender}
                  titulo="Total de pessoas com hipertensão no município"
                />
              )}
            </div>
            <div className="painel-lateral situacao-exames">
              <Typography.Subtitle>
                Situação dos exames nos últimos 12 meses
              </Typography.Subtitle>
              <div className="row gx-4 my-3">
                <div className="col-5 col-lg-6"></div>
                <div className="col col-lg-3">
                  <div className="tipo p-2 text-center">
                    Solicitação pendente
                  </div>
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
          </TwoColumnSection.Col>
          <TwoColumnSection.Col>
            <div className="painel-lateral">
              <Typography.Subtitle>
                Total de atendimento nos últimos 12 meses
              </Typography.Subtitle>
              <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                <div>
                  <div
                    className="container-atendimentos"
                    style={{ width: "221px" }}
                  >
                    <span className="total-trimestre">
                      {isLoadingTotalHipertensao ? (
                        <div className="d-flex align-items-center justify-content-center">
                          <Spinner size="sm" type="grow" className="me-2" />0
                        </div>
                      ) : errorTotalHipertensao ? (
                        <div className="d-flex align-items-center justify-content-center">
                          <Alert color="danger">Erro ao carregar dados.</Alert>
                        </div>
                      ) : (
                        dataTotalHipertensao.total_atendimentos
                      )}
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <div className="row">
              <div className="col-6">
                <div className="painel-lateral">
                  <div className="mt-5 mb-4">
                    <Typography.Subtitle>
                      Nº de pessoas com Hipertensão <br /> (CID/CIAP)
                    </Typography.Subtitle>
                  </div>
                  <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                    <div>
                      <div className="container-atendimentos">
                        <div className="titulo d-flex align-items-center">
                          <img
                            src={info}
                            alt="Total de atendimento nos últimos 12 meses"
                            className="info mx-2"
                          />
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
                          ) : (
                            dataTotalHipertensao.total_pacientes
                          )}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-6">
                <div className="painel-lateral">
                  <div className="mt-5 mb-4">
                    <Typography.Subtitle>
                      Nº de pessoas com Hipertensão <br /> (autoreferido)
                    </Typography.Subtitle>
                  </div>
                  <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                    <div>
                      <div className="container-atendimentos">
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
                          ) : (
                            dataTotalHipertensao.total_auto_referido
                          )}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="painel-secundario my-2">
              <Typography.Subtitle>
                Frequência de complicações relacionadas à hipertensão
              </Typography.Subtitle>
              <div className="d-flex flex-wrap flex-xl-nowrap justify-content-center">
                {isLoadingHipertensaoIndicators ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorHipertensaoIndicators ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Alert color="danger">Erro ao carregar dados.</Alert>
                  </div>
                ) : (
                  <div
                    style={{
                      display: "flex",
                      flexDirection: "row",
                      justifyContent: "space-between",
                      alignItems: "start",
                      flexGrow: 0,
                    }}
                  >
                    {dataHipertensaoIndicators?.map(
                      (indicador: any, i: number) => (
                        <Donut key={i} data={indicador} />
                      )
                    )}
                  </div>
                )}
              </div>
              <div className="mt-5">
                <Button kind="primary" onClick={() => handleClick(6)}>
                  Boas práticas na assistência a pessoas com hipertensão
                </Button>
              </div>
            </div>
            <div className="painel-secundario">
              <Typography.Subtitle>
                Adultos com hipertensão de acordo com o IMC
              </Typography.Subtitle>
              (IMC de pessoas com 20 anos ou mais e menores de 60 anos)
              <br />
              <br />
              <div className="d-flex flex-wrap flex-lg-nowrap justify-content-center">
                {isLoadingHipertensaoFactors ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorHipertensaoFactors ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Alert color="danger">Erro ao carregar dados.</Alert>
                  </div>
                ) : (
                  <div
                    style={{
                      display: "flex",
                      flexDirection: "row",
                      justifyContent: "space-between",
                      alignItems: "start",
                      flexGrow: 0,
                    }}
                  >
                    {dataHipertensaoFactors?.map((diabete: any, i: number) => (
                      <Pie key={i} data={diabete} />
                    ))}
                  </div>
                )}
              </div>
            </div>
            <div className="painel-secundario">
              <Typography.Subtitle>
                Extratificação de atendimentos por profissional
              </Typography.Subtitle>
              <div className="w-100">
                {isLoadingProfessionals ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorProfessionals ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Alert color="danger">Erro ao carregar dados.</Alert>
                  </div>
                ) : (
                  <>
                    {dataProfessionals?.map((item: any, i: number) => (
                      <div key={i} className="d-flex align-items-center mt-2">
                        <div className="container-extratificacao-atendimentos">
                          <span className="profissao-nome">
                            {capitalize(
                              item.profissao.split("-").join(" "),
                              true
                            )}
                          </span>
                          <Progress
                            value={item.total}
                            className="w-75"
                            barStyle={{
                              backgroundColor: randomHexColorCode(),
                            }}
                          />
                        </div>
                        <span className="total ms-2">{item.total}%</span>
                      </div>
                    ))}
                  </>
                )}
              </div>
            </div>
          </TwoColumnSection.Col>
        </TwoColumnSection>

        <ReportFooter />
      </ReportWrapper>
    </div>
  );
}
