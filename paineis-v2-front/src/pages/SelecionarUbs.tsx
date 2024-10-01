import { useNavigate } from "react-router-dom";
import { Spinner } from "reactstrap";
import { useQuery } from "react-query";

import { CSSProperties, useEffect } from "react";
import Select, { StylesConfig } from "react-select";

import { Api } from "../services/api";

import { Header } from "../components/Header";
import { Footer } from "../components/Footer";

import "../styles/selecionarubs.scss";
import variables from "../styles/_exports.module.scss";
import { Button } from "bold-ui";
import { getUBS, userCanSelectUBS } from "../App";

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
  width: "320px",
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

export function SelecionarUbs() {
  let navigate = useNavigate();

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

  const canSelect = userCanSelectUBS();

  useEffect(() => {
    if (!canSelect) {
      const selectedUBS = getUBS();
      navigate(`/painel/${Number(String(selectedUBS))}`);
    }
  }, [canSelect]);

  function handleToPainel() {
    navigate("/painelx");
  }

  const onChangeSelection = (e: any) => {
    navigate(`/painel/${e.value}`);
  };

  if (!canSelect) {
    return null;
  }

  return (
    <div id="page-selecionar-ubs">
      <Header />
      <div className="contentWrapper">
        <div className="container-titulo mb-3">
          <h2>Visualizar dados:</h2>
        </div>
        <div className="container-escolher-ubs d-flex flex-column flex-md-row align-items-center">
          <div className="container-municipio mb-4 mb-md-0">
            <Button
              onClick={handleToPainel}
              type="button"
              kind="primary"
              size="medium"
            >
              Município
            </Button>
          </div>

          <div className="container-combo-ubs ms-md-4">
            {isLoading ? (
              <div className="combo-ubs d-flex align-items-center justify-content-center">
                <Spinner size="sm" /> Carregando lista de UBS's
              </div>
            ) : error ? (
              <div className="combo-ubs d-flex align-items-center justify-content-center">
                Falha ao carregar lista de UBS's
              </div>
            ) : (
              <Select
                isClearable
                placeholder="Selecione UBS"
                noOptionsMessage={() => "Nenhuma UBS encontrada"}
                options={data}
                styles={selectStyle}
                onChange={onChangeSelection}
              />
            )}
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}
