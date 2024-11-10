import { useNavigate } from "react-router-dom";
import { Spinner } from "reactstrap";
import { useQuery } from "react-query";

import { CSSProperties, useEffect, useState } from "react";
import Select, { StylesConfig } from "react-select";

import { Api } from "../services/api";

import { Header } from "../components/Header";
// import { Header } from "../components/HeaderV2";
import { Footer } from "../components/Footer";

import "../styles/selecionarubs.scss";
import "../styles/selecionarvisualizacao.scss";
import variables from "../styles/_exports.module.scss";
import { Button } from "bold-ui";
import { getUBS, userCanSelectUBS } from "../App";

import iconeEquipe from "../assets/images/visualizacao/Icone_Equipe.svg";
import iconeMunicipio from "../assets/images/visualizacao/Icone_Municipio.svg";
import iconeUbs from "../assets/images/visualizacao/Icone_UBS.svg";

type Lista = {
  co_seq_dim_unidade_saude: number;
  no_unidade_saude: string;
  nu_cnes: number;
};

type ResponseData = {
  data: Lista[];
};

type TypeUbs = {
  label: string;
  value: number | string;
};

const customControlStyles: CSSProperties = {
  backgroundColor: variables["--primary-color"],
  width: "250px",
  height: "40px",
  color: variables["--text-color"],
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
    color: state.isSelected ? "#FFFFFF" : "",
    backgroundColor: state.isSelected ? "#343131" : "",
    padding: 16,
  }),
  clearIndicator: () => ({
    color: "#343131",
  }),
  dropdownIndicator: () => ({
    color: "#343131",
  }),
};

export function SelecionarVisualizacao() {
  let navigate = useNavigate();
  const [currentUbs, setCurrentUbs] = useState<any>();
  const [currentTeam, setCurrentTeam] = useState<any>();

  const { data, isLoading, error } = useQuery(
    "ubs",
    async () => {
      const response = await Api.get<ResponseData>("get-units");
      const data = response.data;
      const listData: TypeUbs[] = data.data.map((ubs) => {
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

  const { data: teamsData } = useQuery(
    "get-teams/"+currentUbs,
    async () => {
      const response = await Api.get<ResponseData>("get-teams/"+currentUbs);
      const data = response.data;
      const listData: TypeUbs[] = data.data.map((i: any) => {
        return {
          ...i,
          label: i.nome_equipe + " (" + i.codigo_equipe + ")",
          value: i.codigo_equipe,
        };
      });

      return listData;
    },
    {
      staleTime: 1000 * 60 * 10, //10 minutos
    }
  );

  console.log({ teamsData })

  const canSelect = userCanSelectUBS();

  useEffect(() => {
    if (!canSelect) {
      const selectedUBS = getUBS();
      if (selectedUBS) {
        navigate(`/painel/${Number(String(selectedUBS))}`);
      }
    }
  }, [canSelect]);

  function handleToPainel() {
    navigate("/painelx");
  }

  function handleToPainelWithTeam() {
    navigate(`/painel/${currentUbs}?equipe=${currentTeam}`);
  }

  const onChangeSelection = (e: any) => {
    setCurrentUbs(e.value);
  };

  const handleToPainelWithUbs = () => {
    navigate(`/painel/${currentUbs}`);
  };

  const onChangeTeamSelection = (e: any) => {
    setCurrentTeam(e.value);
  };

  return (
    <div id="page-selecionar-ubs">
      <Header />
      <div className="contentWrapper">
        <div className="container-titulo mb-5">
          <h2>Visualizar dados por:</h2>
        </div>
        <div className="container-escolher d-flex flex-column flex-md-row">
          <div className="container-municipio mb-4 mb-md-0">
            <div className="container-icone">
              <img
                className="icone-municipio"
                src={iconeMunicipio}
                alt="Ícone de Município"
              />
              <Button
                onClick={handleToPainel}
                type="button"
                kind="primary"
                size="small"
              >
                Município
              </Button>
            </div>
          </div>

          <div className="container-combo-ubs ms-md-4">
            <div className="container-icone">
              <img className="icone-ubs" src={iconeUbs} alt="Ícone de UBS" />
              {isLoading ? (
                <div className="combo-ubs d-flex align-items-center justify-content-center">
                  <Spinner size="sm" /> Carregando lista de UBS's
                </div>
              ) : error ? (
                <div className="combo-ubs d-flex align-items-center justify-content-center">
                  Falha ao carregar lista de UBS's
                </div>
              ) : (
                <>
                  <Select
                    isClearable
                    placeholder="UBS"
                    noOptionsMessage={() => "Nenhuma UBS encontrada"}
                    options={data}
                    styles={selectStyle}
                    onChange={onChangeSelection}
                  />
                  { currentUbs && <Button
                    onClick={handleToPainelWithUbs}
                    type="button"
                    kind="primary"
                    size="small"
                    style={{ marginTop: "10px" }}
                  >
                    Acessar UBS
                  </Button>}
                </>
              )}
            </div>
          </div>

        <div className="container-combo-ubs ms-md-4"
                style={{
                  opacity: !currentUbs ? 0.6 : 1
                }}>
            <div className="container-icone">
              <img
                className="icone-equipe"
                src={iconeEquipe}
                alt="Ícone de Equipe"
              />
              {isLoading ? (
                <div className="combo-ubs d-flex align-items-center justify-content-center">
                  <Spinner size="sm" /> Carregando lista de equipes
                </div>
              ) : error ? (
                <div className="combo-ubs d-flex align-items-center justify-content-center">
                  Falha ao carregar lista de equipes
                </div>
              ) : (
                <>
                <Select
                  isClearable
                  placeholder={"Equipe"}
                  noOptionsMessage={() => "Nenhuma equipe encontrada"}
                  options={teamsData}
                  styles={selectStyle}
                  onChange={onChangeTeamSelection}
                  isDisabled={!currentUbs}
                />
                {!currentUbs ?<p style={{ fontSize: "12px" }}>
                 Selecione uma ubs para continuar
                </p>: null}
                  { currentTeam && <Button
                    onClick={handleToPainelWithTeam}
                    type="button"
                    kind="primary"
                    size="small"
                    style={{ marginTop: "10px" }}
                  >
                    Acessar Equipe
                  </Button>}
                </>
              )}
            </div>
          </div> 
        </div>
      </div>
      <Footer />
    </div>
  );
}
