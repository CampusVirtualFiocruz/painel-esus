import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { useQuery } from "react-query";
import { Alert, Progress, Spinner } from "reactstrap";
import { Button } from "bold-ui";

import { Api } from "../services/api";
import { Bar } from "../charts/Bar";
import { Donut } from "../charts/Donut";
import { Pie } from "../charts/Pie";
import { capitalize, getNomeUbs } from "../utils";
import { BarSexo } from "../charts/BarSexo";
import { useInfo } from "../context/infoProvider/useInfo";
import { Modal } from "../components/Modal";
import { Typography } from "../components/ui/Typography";
import { ReportFooter } from "../components/ui/ReportFooter";
import ReportWrapper from "../components/ui/ReportWrapper";
import TwoColumnSection from "../components/ui/TwoColumnSection";
import { randomHexColorCode, wait } from "../utils/reports";
import "../styles/diabetesHipertensao.scss";
import Card from "../components/ui/Card";
import RenderSingleValue from "../components/ui/RenderSingleValue";

type TModal = {
  loaded: number;
  tipo?: string;
  cnes?: string | undefined;
};

type PainelParams = {
  id: string;
};

export function Diabetes() {
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
    data: dataTotalDiabetes,
    isLoading: isLoadingTotalDiabetes,
    error: errorTotalDiabetes,
  } = useQuery(
    ["diabetes/total", id],
    async () => {
      const response = await Api.get("diabetes/total");
      const responseData = response.data;

      let total = responseData.data;

      return total;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataDiabetesAgeGroupGender,
    isLoading: isLoadingDiabetesAgeGroupGender,
    error: errorDiabetesAgeGroupGender,
  } = useQuery(
    ["diabetes-age-group-gender", paramRoute],
    async () => {
      let path = id
        ? `diabetes/age-group-gender/${id}`
        : "diabetes/age-group-gender";
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataDiabetes,
    isLoading: isLoadingDiabetes,
    error: errorDiabetes,
  } = useQuery(
    ["diabetes-age-group-location", paramRoute],
    async () => {
      let path = id
        ? `diabetes/age-group-location/${id}`
        : "diabetes/age-group-location";
      const response = await Api.get(path);
      const responseData = response.data;

      return responseData.data;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const {
    data: dataDiabetesIndicators,
    isLoading: isLoadingDiabetesIndicators,
    error: errorDiabetesIndicators,
  } = useQuery(
    ["diabetes-complications", paramRoute],
    async () => {
      let path = id ? `diabetes/complications/${id}` : "diabetes/complications";
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
    data: dataDiabetesFactors,
    isLoading: isLoadingDiabetesFactors,
    error: errorDiabetesFactors,
  } = useQuery(
    ["diabetes-factors-imc", paramRoute],
    async () => {
      let path = id ? `diabetes/imc/${id}` : "diabetes/imc";
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
    ["diabetes-exams", paramRoute],
    async () => {
      let path = id ? `diabetes/exams/${id}` : "diabetes/exams";
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
    ["diabetes-professionals", paramRoute],
    async () => {
      let path = id ? `diabetes/professionals/${id}` : "diabetes/professionals";
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

  let navigate = useNavigate();

  function handleListaNominal() {
    navigate(`/lista-nominal?condicao=Diabetes`);
  }

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
  const title = `${UBS} / Diabetes`;

  return (
    <div id="page-painel-diabetes-hipertensao">
      {showModal && <Modal data={data} setShowModal={setShowModal} />}
      <ReportWrapper title={title}>
        <TwoColumnSection>
          <TwoColumnSection.Col>
            <div>
              <Typography.Subtitle>
                Pessoas com diabetes por faixa etária
              </Typography.Subtitle>
              {isLoadingDiabetes ? (
                <div className="d-flex align-items-center justify-content-center">
                  <Spinner size="sm" type="grow" className="me-2" />
                  Carregando...
                </div>
              ) : errorDiabetes ? (
                <div className="d-flex align-items-center justify-content-center">
                  <Alert color="danger">Erro ao carregar dados.</Alert>
                </div>
              ) : (
                <Bar
                  data={dataDiabetes}
                  titulo="Total de pessoas com diabetes no município"
                />
              )}
            </div>
            <div>
              <Typography.Subtitle>
                Pessoas com diabetes por sexo
              </Typography.Subtitle>
              {isLoadingDiabetesAgeGroupGender ? (
                <div className="d-flex align-items-center justify-content-center">
                  <Spinner size="sm" type="grow" className="me-2" />
                  Carregando...
                </div>
              ) : errorDiabetesAgeGroupGender ? (
                <div className="d-flex align-items-center justify-content-center">
                  <Alert color="danger">Erro ao carregar dados.</Alert>
                </div>
              ) : (
                <BarSexo
                  data={dataDiabetesAgeGroupGender}
                  titulo="Total de pessoas com diabetes no município"
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
                  {dataExamsTable
                    ?.filter(
                      (situacao: any) => situacao?.tipo !== "Aferição de PA"
                    )
                    ?.map((situacao: any, i: number) => (
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
            <div style={{ display: "flex", flexDirection: "row", gap: "10px" }}>
              <Card style={{ flex: 1 }}>
                <RenderSingleValue
                  icon="medkit"
                  title="Total de atendimentos nos últimos 12 meses"
                  value={dataTotalDiabetes?.total_atendimentos}
                />
              </Card>
              <Card style={{ flex: 2 }}>
                <div
                  style={{ display: "flex", flexDirection: "row", gap: "10px" }}
                >
                  <RenderSingleValue
                    icon="people"
                    title="Nº de pessoas com diabetes (CID/CIAP)"
                    value={dataTotalDiabetes?.total_pacientes}
                  />
                  <RenderSingleValue
                    icon="people"
                    title="Nº de pessoas com diabetes (autoreferido)"
                    value={dataTotalDiabetes?.total_auto_referido}
                  />
                </div>
              </Card>
            </div>
            <div>
              <Typography.Subtitle>
                Frequência de complicações relacionadas à diabetes
              </Typography.Subtitle>
              <div style={{ marginBottom: "30px" }} />
              <div className="d-flex flex-wrap flex-xl-nowrap justify-content-center">
                {isLoadingDiabetesIndicators ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorDiabetesIndicators ? (
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
                    {dataDiabetesIndicators?.map(
                      (indicador: any, i: number) => (
                        <Donut key={i} data={indicador} />
                      )
                    )}
                  </div>
                )}
              </div>
              <div className="mt-5" style={{ textAlign: "center" }}>
                <Button kind="primary" onClick={() => handleClick(5)}>
                  Boas práticas na assistência a pessoa com diabetes
                </Button>
              </div>
            </div>
            <div style={{ textAlign: "center" }}>
              <Typography.Subtitle>
                Adultos com diabetes de acordo com o IMC
              </Typography.Subtitle>
              (IMC de pessoas com 20 anos ou mais e menores de 60 anos)
              <br />
              <br />
              <div className="d-flex flex-wrap flex-lg-nowrap">
                {isLoadingDiabetesFactors ? (
                  <div className="d-flex align-items-center justify-content-center">
                    <Spinner size="sm" type="grow" className="me-2" />
                    Carregando...
                  </div>
                ) : errorDiabetesFactors ? (
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
                    {dataDiabetesFactors?.map((diabete: any, i: number) => (
                      <Pie key={i} data={diabete} />
                    ))}
                  </div>
                )}
              </div>
            </div>
            <div className="mt-5" style={{ textAlign: "center" }}>
                <Button kind="primary" onClick={handleListaNominal}>
                Ver a relação das pessoas com diabetes da UBS
                </Button>
            </div>
            <div className="painel-secundario">
              <Typography.Subtitle>
                Estratificação de atendimentos por profissional
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
