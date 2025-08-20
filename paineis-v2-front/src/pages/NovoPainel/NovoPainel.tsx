import { Button } from "bold-ui";
import { CSSProperties, useState } from "react";
import { useQuery } from "react-query";
import { useNavigate, useParams } from "react-router-dom";
import Select, { StylesConfig } from "react-select";
import Piramide from "../../components/charts/Home/Piramide";
import ReportCardSelector from "../../components/charts/Home/ReportCardSelector";
import TopIndicatorsContent from "../../components/charts/Home/TopIndicatorsContent";
import ReportWrapper from "../../components/ui/ReportWrapper";
import useReportDataHome from "../../hooks/sections/home/useReportDataHome";
import { Api } from "../../services/api";
import { ReportBasicParams, navigateHome } from "../../utils";

type IsMulti = false;

const customControlStyles: CSSProperties = {
  width: "320px",
  height: "40px",
};

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

type Lista = {
  co_seq_dim_unidade_saude: number;
  no_unidade_saude: string;
  nu_cnes: number;
  qtd?: number;
};

type TypeUbs = {
  label: string;
  value: number | string;
  qtd?: number;
};

const NovoPainel = () => {
  const { id } = useParams<ReportBasicParams>();

  let navigate = useNavigate();
  const squadId = "456";
  const ubsId = "456";
  const [loading, setLoading] = useState(true);

  type ResponseDataListUbs = {
    data: Lista[];
  };

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

  const reportData = useReportDataHome({
    ubsId,
    squadId,
  });

  const onChangeSelection = (e: any) => {
    navigateHome(navigate, `/${e.value}`);
  };

  return (
    <ReportWrapper title={""}>
      <div id="novo-painel">
        <div className="contentWrapper">
          <TopIndicatorsContent charts={reportData.data} />
          <Piramide charts={reportData.data} />
          <ReportCardSelector charts={reportData.data} />
          <div className="my-5">
            {id ? (
              <Button kind="primary" onClick={() => navigateHome(navigate)}>
                Visualizar dados do painel do Município
              </Button>
            ) : (
              <>
                {isLoadingUbs ? (
                  <div className="combo-ubs d-flex align-items-center justify-content-center">
                    Carregando lista de UBS's...
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
      </div>
    </ReportWrapper>
  );
};

export default NovoPainel;
