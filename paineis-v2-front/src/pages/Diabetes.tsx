import { useState } from "react";
import { useParams, useNavigate, useSearchParams } from "react-router-dom";
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

const footerNote = `¹ O número de pessoas com Diabetes equivale ao total de indivíduos que tiveram atendimentos individuais com registro do código CID e/ou CIAP correspondente à condição de saúde na Ficha de Atendimento Individual, somado ao conjunto de pessoas com registro autorreferido da condição de saúde na Ficha de Cadastro Individual.`;

export function Diabetes() {
  const { id } = useParams<PainelParams>();
  const [showModal, setShowModal] = useState(false);
  const [data, setData] = useState<TModal>({ loaded: 0 });

  const [params] = useSearchParams();
  const equipe = params.get("equipe");

  let paramRoute = id ? id : "all";
  const search = equipe ? `?equipe=${equipe}` : "";

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
      let path = id ? `diabetes/total/${id}` : "diabetes/total";
      const response = await Api.get(path + search);

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
      const response = await Api.get(path + search);
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
      const response = await Api.get(path + search);
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
      const response = await Api.get(path + search);
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
      const response = await Api.get(path + search);
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
      const response = await Api.get(path + search);
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
      const response = await Api.get(path + search);
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

  return (
    <div id="page-painel-diabetes-hipertensao">
      {showModal && <Modal data={data} setShowModal={setShowModal} />}
      <ReportWrapper
        title={"Diabetes"}
        //subtitle="(Pessoas atendidas nos últimos 12 meses)"
        footerNote={footerNote}
        footer={<ReportFooter chaveListaNominal="Diabetes" equipe={equipe} />}
      >
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
              <div style={{ display: "flex", paddingTop: "30px" }}>
                <div style={{ flex: "150px" }}>
                  <div className="tipo p-2 "></div>
                </div>
                <div style={{ flex: 1 }}>
                  <div className="coluna p-2 text-center ">Sem Solicitação</div>
                </div>
                <div style={{ flex: 1 }}>
                  <div className="coluna p-2 text-center ">
                    Aguardando Resultado
                  </div>
                </div>
                <div style={{ flex: 1 }}>
                  <div className="coluna p-2 text-center ">
                    Resultado Registrado
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
                  {Object.keys(dataExamsTable ?? {})?.map((label) => (
                    <>
                      <div
                        key={label}
                        style={{
                          display: "flex",
                          gap: "14px",
                          marginBottom: "10px",
                        }}
                      >
                        <div style={{ flex: "150px" }}>
                          <div className="tipo p-2 bordas">{label}</div>
                        </div>
                        <div style={{ flex: 1 }}>
                          <div className="coluna p-2 text-center bordas">
                            {dataExamsTable?.[label]?.["sem-solicitacao"]}
                          </div>
                        </div>
                        <div style={{ flex: 1 }}>
                          <div className="coluna p-2 text-center bordas">
                            {dataExamsTable?.[label]?.["aguardando-resultado"]}
                          </div>
                        </div>
                        <div style={{ flex: 1 }}>
                          <div className="coluna p-2 text-center bordas">
                            {dataExamsTable?.[label]?.["resultado-registrado"]}
                          </div>
                        </div>
                      </div>
                    </>
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
                  value={Number(
                    dataTotalDiabetes?.total_atendimentos
                  )?.toLocaleString("pt-BR")}
                />
              </Card>
              <Card style={{ flex: 2 }}>
                <div
                  style={{ display: "flex", flexDirection: "row", gap: "20px" }}
                >
                  <RenderSingleValue
                    icon="people"
                    title="Nº de pessoas com diabetes (CID/CIAP)¹"
                    value={Number(
                      dataTotalDiabetes?.total_pacientes
                    )?.toLocaleString("pt-BR")}
                  />
                  <RenderSingleValue
                    icon="people"
                    title="Nº de pessoas com diabetes (autorreferido)¹"
                    value={Number(
                      dataTotalDiabetes?.total_auto_referido
                    )?.toLocaleString("pt-BR")}
                  />
                </div>
              </Card>
            </div>
            <div>
              <Typography.Subtitle>
                Frequência de complicações relacionadas ao diabetes
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
              {/* <div className="mt-5" style={{ textAlign: "center" }}>
                <Button kind="primary" onClick={() => handleClick(5)}>
                  Boas práticas na assistência a pessoa com diabetes
                </Button>
              </div> */}
            </div>
            <div style={{ textAlign: "center" }}>
              <Typography.Subtitle>
                Adultos com diabetes de acordo com o IMC
              </Typography.Subtitle>
              (IMC de pessoas com idade de 20 anos ou mais e menores de 60 anos)
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
      </ReportWrapper>
    </div>
  );
}
