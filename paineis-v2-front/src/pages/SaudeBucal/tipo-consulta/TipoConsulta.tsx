import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import { Api } from "../../../services/api";
import { DonutChart, TDonutChart } from "../../../charts/Donut";
import { STALE_TIME } from "../../../config/stale-time";
import { Typography } from "../../../components/ui/Typography";
import { PainelParams } from "../faixa-etaria/FaixaEtaria";
import AsyncDataLoad from "../async-data-load";

type TipoAtentimentoResponse = {
  label: string;
  value: number;
  total: number;
};

const TipoConsulta = () => {
  const { id } = useParams<PainelParams>();
  const {
    data: tipoResponse,
    isLoading,
    error,
  } = useQuery(
    ["saude-bucal-tipo-consulta", id],
    async () => {
      const url = "oral-health/cares-by-type-of-services";
      let path = id ? `${url}/${id}` : url;
      const response = await Api.get<TipoAtentimentoResponse[]>(path);
      const res = response.data?.map((item: TipoAtentimentoResponse) => ({
        value: item.value,
        name: item.label,
      }));
      return res;
    },
    {
      staleTime: STALE_TIME,
    }
  );
  return (
    <AsyncDataLoad {...{ isLoading, error }}>
      <div className="col-12 chart-container total-atd-container">
        <Typography.Subtitle>
          Cuidado em saude bucal por tipo de consulta
        </Typography.Subtitle>
        <DonutChart {...new TDonutChart("", tipoResponse || [], "#5cd2c8")} />
      </div>
    </AsyncDataLoad>
  );
};

export default TipoConsulta;
