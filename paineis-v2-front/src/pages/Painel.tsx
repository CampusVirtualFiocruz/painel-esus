import { CSSProperties, useState, useEffect } from "react";
import Select, { StylesConfig } from "react-select";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { useQuery } from "react-query";
import { Spinner } from "reactstrap";
import { Button } from "bold-ui";

import { Header } from "../components/Header";
import { Footer } from "../components/Footer";
import { formataNumero, getNomeUbs, somaIndicador } from "../utils";
import { Condicao } from "../charts/Condicao";
import Piramide from "../charts/Piramide";
import { Zonas } from "../charts/Zonas";
import { Api } from "../services/api";

import masculino from "../assets/images/masculino.svg";
import feminino from "../assets/images/feminino.svg";
import homem from "../assets/images/homem.svg";
import mulher from "../assets/images/mulher.svg";
import diabetes from "../assets/images/menu/diabetes.png";
import hipertensao from "../assets/images/menu/hipertensao.png";
import children from "../assets/images/menu/children.png";
import old from "../assets/images/menu/old.png";
import quality from "../assets/images/menu/quality.png";

import { useInfo } from "../context/infoProvider/useInfo";

import "../styles/painel.scss";
import { MdInfoOutline } from "react-icons/md";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "../components/ui/Tooltip";
import { Typography } from "../components/ui/Typography";
import Card from "../components/ui/Card";
import { userCanSelectUBS } from "../App";

type PainelParams = {
  id: string;
};
type Indicator = {
  rural: number;
  urbano: number;
};

type TypeUbs = {
  label: string;
  value: number | string;
  qtd?: number;
};

const customControlStyles: CSSProperties = {
  width: "320px",
  height: "40px",
};

type IsMulti = false;

const selectStyle: StylesConfig<TypeUbs, IsMulti> = {
  control: (provided, state) => {
    return {
      ...provided,
      ...customControlStyles,
    };
  },
  option: (provided, state) => ({
    ...provided,
    padding: 10,
  }),
  clearIndicator: () => ({
    color: "#343131",
  }),
  dropdownIndicator: () => ({
    color: "#343131",
  }),
};

interface IPainel {
  ibgePopulation: number;
  ageGroups: {};
  gender: {
    feminino: number;
    masculino: number;
  };
  indicators: {
    diabetes: Indicator;
    gestantes: Indicator;
    hipertensao: Indicator;
    crianca: Indicator;
    idosa: Indicator;
    qualidade: Indicator;
  };
  locationArea: {
    rural: number;
    urbano: number;
    nao_definido: number;
  };
  total: number;
}

type ResponseData = {
  data: IPainel;
};

type Lista = {
  co_seq_dim_unidade_saude: number;
  no_unidade_saude: string;
  nu_cnes: number;
  qtd?: number;
};

type ResponseDataListUbs = {
  data: Lista[];
};

export function Painel() {
  let navigate = useNavigate();
  const { id } = useParams<PainelParams>();
  const [params] = useSearchParams();
  const equipe = params.get("equipe");
  const { cityInformation } = useInfo();
  const [dadosPainel, setDadosPainel] = useState<IPainel>();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getDados = async () => {
      let rota = id
        ? `get-demographic-info/${id}${equipe ? `?equipe=${equipe}` : ""}`
        : `get-demographic-info${equipe ? `?equipe=${equipe}` : ""}`;

      try {
        const response = await Api.get<ResponseData>(rota);
        const { data } = response.data;

        setDadosPainel(data);
        setLoading(false);
      } catch (error) {
        /* alert("Ocorreu um erro ao buscar informações demográficas"); */
        setLoading(false);
      }
    };

    getDados();

    return () => {
    };
  }, [id]);

  const {
    data: dataUbs,
    isLoading: isLoadingUbs,
    error: errorUbs,
  } = useQuery(
    "ubs",
    async () => {
      const response = await Api.get<ResponseDataListUbs>("get-units");
      const data = response.data;
      const listData: TypeUbs[] = data.data.map((ubs) => {
        return {
          label: ubs.no_unidade_saude,
          value: ubs.co_seq_dim_unidade_saude,
          qtd: ubs.qtd,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  const nomeUbs = id && !isLoadingUbs ? getNomeUbs(dataUbs, id) : "-";

  function handleToPainelMunicipio() {
    setLoading(true);
    navigate("/painelx");
  }

  const onChangeSelection = (e: any) => {
    setLoading(true);
    navigate(`/painel/${e.value}`);
  };

  const openReport = (
    report: "diabetes" | "hipertensao" | "infantil" | "qualidade" | "idosa"
  ) => {
    if (id !== undefined) {
      navigate(`/diabetes/${id}${equipe ? `?equipe=${equipe}` : ""}`);
    } else {
      navigate(`/diabetes${equipe ? `?equipe=${equipe}` : ""}`);
    }
  };

  function handleToDiabetes() {
    if (id !== undefined) {
      navigate(`/diabetes/${id}${equipe ? `?equipe=${equipe}` : ""}`);
    } else {
      navigate(`/diabetes${equipe ? `?equipe=${equipe}` : ""}`);
    }
  }

  function handleToHipertensao() {
    if (id !== undefined) {
      navigate(`/hipertensao/${id}${equipe ? `?equipe=${equipe}` : ""}`);
    } else {
      navigate(`/hipertensao${equipe ? `?equipe=${equipe}` : ""}`);
    }
  }

  function handleToInfantil() {
    if (id !== undefined) {
      navigate(`/infantil/${id}${equipe ? `?equipe=${equipe}` : ""}`);
    } else {
      navigate(`/infantil${equipe ? `?equipe=${equipe}` : ""}`);
    }
  }

  function handleToQualidade() {
    if (id !== undefined) {
      navigate(`/qualidade/${id}${equipe ? `?equipe=${equipe}` : ""}`);
    } else {
      navigate(`/qualidade${equipe ? `?equipe=${equipe}` : ""}`);
    }
  }

  function handleToIdosa() {
    if (id !== undefined) {
      navigate(`/idosaV2/${id}${equipe ? `?equipe=${equipe}` : ""}`);
    } else {
      navigate(`/idosaV2${equipe ? `?equipe=${equipe}` : ""}`);
    }
  }

  return (
    <div id="page-painel">
      <Header />

      {loading ? (
        <div className="contentWrapperLoading">
          <Spinner color="#343131" />
        </div>
      ) : (
        <div className="contentWrapper">
          <hr className="linha my-4" />

          <h2>
            {id
              ? !isLoadingUbs
                ? nomeUbs
                : "Carregando..."
              : cityInformation?.municipio + " - " + cityInformation?.uf}
          </h2>

          <div
            className="container container-cards-principal"
            style={{ overflow: "visible" }}
          >
            <div className="row align-items-start">
              <div className="col-xl-3">
                <div className="container-card d-flex flex-column flex-md-row align-items-center justify-content-center my-2 py-2 px-4">
                  <div className="w-50 d-flex flex-column align-items-center justify-content-center">
                    <h4 className="text-center">Cidadãos Cadastrados</h4>
                    <span>{formataNumero(dadosPainel?.total)}</span>
                  </div>
                  <div className="w-50 d-flex flex-column align-items-center justify-content-center">
                    <Tooltip>
                      <TooltipContent className="Tooltip">
                        <div>
                          Informação extraída da Relação da População Municipal
                          enviada ao TCU em 2023,
                          <br /> pelo IBGE. (clique para acessar o portal do
                          IBGE)
                        </div>
                      </TooltipContent>
                      <a
                        target="_blank"
                        href="https://www.ibge.gov.br/estatisticas/sociais/populacao/37734-relacao-da-populacao-dos-municipios-para-publicacao-no-dou.html?=&t=resultados"
                        rel="noreferrer"
                      >
                        <h4 className="text-center">
                          <TooltipTrigger>
                            População Apurada&nbsp;
                            <MdInfoOutline
                              style={{
                                cursor: "pointer",
                                color: "#ffffff",
                                height: 20,
                                width: 20,
                              }}
                            />
                          </TooltipTrigger>
                        </h4>
                      </a>
                    </Tooltip>
                    <span>{formataNumero(dadosPainel?.ibgePopulation)}</span>
                  </div>
                </div>
              </div>

              <div className="col-xl-6" style={{ overflow: "visible" }}>
                <Card
                  className="container-card-alt"
                  style={{ padding: 0, marginTop: "8px" }}
                >
                  <div className="d-flex flex-column flex-md-row align-items-center justify-content-center my-2">
                    <div className="me-2">
                      <Zonas data={dadosPainel?.locationArea} />
                    </div>
                    <div>
                      <Tooltip>
                        <Typography.Details>
                          <TooltipTrigger>
                            Tipo de localização&nbsp;
                            <MdInfoOutline
                              style={{
                                cursor: "pointer",
                                color: "#222222",
                                height: 20,
                                width: 20,
                              }}
                            />
                          </TooltipTrigger>
                          <TooltipContent className="Tooltip">
                            "Não informado" refere-se aos cadastros realizados
                            em
                            <br />
                            Ficha de Cadastro Individual sem associação com uma
                            <br />
                            Ficha de Cadastro Domiciliar e Territorial.
                          </TooltipContent>
                        </Typography.Details>
                      </Tooltip>
                      <div
                        className="d-flex flex-column flex-md-row align-items-center justify-content-center my-2"
                        style={{ gap: "15px" }}
                      >
                        <div className="container-dados-zona">
                          <div className="d-flex align-items-center mb-2">
                            <div className="box-container-light me-2"></div>
                            <h4>Zona Urbana</h4>
                          </div>
                          <span>
                            {formataNumero(dadosPainel?.locationArea.urbano)}
                          </span>
                        </div>
                        <div className="container-dados-zona">
                          <div className="d-flex align-items-center mb-2">
                            <div className="box-container-dark me-2"></div>
                            <h4>Zona Rural</h4>
                          </div>
                          <span>
                            {formataNumero(dadosPainel?.locationArea.rural)}
                          </span>
                        </div>
                        <div className="container-dados-zona">
                          <div className="d-flex align-items-center mb-2">
                            <div className="box-container-nonactive me-2"></div>
                            <h4>Não informado</h4>
                          </div>
                          <span>
                            {formataNumero(
                              dadosPainel?.locationArea.nao_definido
                            )}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </Card>
              </div>
              <div className="col-xl-3">
                <div className="container-card d-flex align-items-center justify-content-center my-2 py-1">
                  <div className="d-flex flex-column align-items-center ms-2 me-4">
                    <img
                      className="my-2 force-white"
                      src={homem}
                      alt="Homem"
                      width={60}
                    />
                    <span>{formataNumero(dadosPainel?.gender.masculino)}</span>
                  </div>

                  <div className="d-flex flex-column align-items-center ms-4 me-2">
                    <img
                      className="my-2 force-white"
                      src={mulher}
                      alt="Mulher"
                      width={60}
                    />
                    <span>{formataNumero(dadosPainel?.gender.feminino)}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="my-5">
            <Typography.Subtitle>
              Proporção de indivíduos cadastrados por sexo e idade
            </Typography.Subtitle>
          </div>
          {dadosPainel !== undefined &&
          dadosPainel.ageGroups &&
          Object.keys(dadosPainel.ageGroups).length !== 4 ? (
            <div className="graficoPiramide">
              <div className="w-100 painel-demografico">
                <div className="d-flex justify-content-center">
                  <div className="mx-2">
                    <img
                      src={masculino}
                      className="img-fluid"
                      alt="Masculino"
                    />
                  </div>
                  <div className="mx-2">
                    <img src={feminino} className="img-fluid" alt="Feminino" />
                  </div>
                </div>
                <Piramide data={dadosPainel.ageGroups} />
              </div>
              <div className="d-flex align-items-center justify-content-between mt-5">
                <div className="d-flex align-items-center mx-3">
                  <div className="box-container-light me-2"></div>
                  <h5 className="mb-0">Zona Urbana</h5>
                </div>
                <div className="d-flex align-items-center mx-3">
                  <div className="box-container-dark me-2"></div>
                  <h5 className="mb-0">Zona Rural</h5>
                </div>
                <div className="d-flex align-items-center mx-3">
                  <div className="box-container-nonactive me-2"></div>
                  <h5 className="mb-0">Não Informado</h5>
                </div>
              </div>
            </div>
          ) : (
            <h6 className="text-danger">
              Sem dados de proporção de indivíduos cadastrados.
            </h6>
          )}
          <div style={{ marginTop: "60px", marginBottom: "20px" }}>
            <Typography.Subtitle>Relatórios Temáticos</Typography.Subtitle>
          </div>
          <div className="container">
            <div className="row container-cards-condicoes">
              <div className="card-condicao p-2" onClick={handleToDiabetes}>
                <span className="nome-condicao">Diabetes</span>
                <h4>{somaIndicador(dadosPainel?.indicators?.diabetes)}</h4>
                <div className="d-flex align-items-center">
                  <img src={diabetes} alt="Diabetes" className="mx-2" />
                  <Condicao data={dadosPainel?.indicators?.diabetes} />
                </div>
              </div>
              <div className="card-condicao p-2" onClick={handleToHipertensao}>
                <span className="nome-condicao">Hipertensão</span>
                <h4>{somaIndicador(dadosPainel?.indicators?.hipertensao)}</h4>
                <div className="d-flex align-items-center">
                  <img src={hipertensao} alt="Hipertensão" className="mx-2" />
                  <Condicao data={dadosPainel?.indicators?.hipertensao} />
                </div>
              </div>
              {/* {Boolean(dadosPainel?.indicators?.crianca) && (
                <div className="card-condicao p-2" onClick={handleToInfantil}>
                  <span className="nome-condicao">
                    Desenvolvimento Infantil
                  </span>
                  <h4>{somaIndicador(dadosPainel?.indicators?.crianca)}</h4>
                  <div className="d-flex align-items-center">
                    <img
                      width={"30%"}
                      src={children}
                      alt="Desenvolvimento Infantil"
                      className="mx-2"
                    />
                    <Condicao data={dadosPainel?.indicators?.crianca} />
                  </div>
                </div>
              )} */}
            </div>
            <div
              className="row container-cards-condicoes"
              style={{ marginTop: "20px" }}
            >
              {Boolean(dadosPainel?.indicators?.qualidade) && (
                <div className="card-condicao p-2" onClick={handleToQualidade}>
                  <span className="nome-condicao">Qualidade de Cadastros</span>
                  <h4>{somaIndicador(dadosPainel?.indicators?.qualidade)}</h4>
                  <div className="d-flex align-items-center">
                    <img src={quality} alt="Qualidade" className="mx-2" />
                    <Condicao data={dadosPainel?.indicators?.qualidade} />
                  </div>
                </div>
              )}
              {Boolean(dadosPainel?.indicators?.idosa) && (
                // <div className="card-condicao p-2" onClick={handleToIdosa}>
                //   <span className="nome-condicao">Cuidado da Pessoa Idosa</span>
                //   <h4>{somaIndicador(dadosPainel?.indicators?.idosa)}</h4>
                //   <div className="d-flex align-items-center">
                //     <img
                //       width={"30%"}
                //       src={old}
                //       alt="Pessoa Idosa"
                //       className="mx-2"
                //     />
                //     <Condicao data={dadosPainel?.indicators?.idosa} />
                //   </div>
                // </div>
                <div
                    className="card-condicao p-2"
                    style={{ visibility: 'hidden' }}
                ></div>
              )}
             {/*  {Boolean(dadosPainel?.indicators?.saudeBucal) && (
                <div className="card-condicao p-2" onClick={handleToIdosa}>
                  <span className="nome-condicao">Cuidado da Pessoa Idosa</span>
                  <h4>{somaIndicador(dadosPainel?.indicators?.idosa)}</h4>
                  <div className="d-flex align-items-center">
                    <img
                      width={"30%"}
                      src={old}
                      alt="Pessoa Idosa"
                      className="mx-2"
                    />
                    <Condicao data={dadosPainel?.indicators?.idosa} />
                  </div>
                </div>
              )} */}
            </div>
            <div className="d-flex my-5 justify-content-center">
              <div className="container-areas d-flex align-items-center me-4">
                <div className="box-container-light me-2"></div>
                <h4>Zona Urbana</h4>
              </div>
              <div className="container-areas d-flex align-items-center ms-4">
                <div className="box-container-dark me-2"></div>
                <h4>Zona Rural</h4>
              </div>
              <div className="container-areas d-flex align-items-center ms-4">
                <div className="box-container-nonactive me-2"></div>
                <h4>Não Informado</h4>
              </div>
            </div>
          </div>
          <div className="my-5">
            {id ? (
              <Button onClick={handleToPainelMunicipio}>
                Visualizar dados do painel do Município
              </Button>
            ) : (
              <>
                {isLoadingUbs ? (
                  <div className="combo-ubs d-flex align-items-center justify-content-center">
                    <Spinner size="sm me-1" /> Carregando lista de UBS's
                  </div>
                ) : errorUbs ? (
                  <div className="combo-ubs d-flex align-items-center justify-content-center">
                    Falha ao carregar lista de UBS's
                  </div>
                ) : (
                  <Select
                    isClearable
                    placeholder="Selecione UBS"
                    noOptionsMessage={() => "Nenhuma UBS encontrada"}
                    options={dataUbs}
                    styles={selectStyle}
                    onChange={onChangeSelection}
                  />
                )}
              </>
            )}
          </div>
        </div>
      )}
      <Footer />
    </div>
  );
}
