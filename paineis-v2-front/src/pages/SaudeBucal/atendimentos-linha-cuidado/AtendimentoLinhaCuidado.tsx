import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import { Api } from "../../../services/api";
import { PieChart, TPieChart } from "../../../charts/Pie";
import { Typography } from "../../../components/ui/Typography";
import AsyncDataLoad from "../async-data-load";

type PainelParams = {
  id: string;
};

type LinhaCuidadoResponse = {
  label: string;
  total: number;
  value: number;
};

const AtendimentoLinhaCuidado = () => {
  const { id } = useParams<PainelParams>();
  const { data, isLoading, error } = useQuery<LinhaCuidadoResponse[]>(
    ["saude-bucal-linha-cuidade", id],
    async () => {
      const url = "oral-health/cares-by-line-of-services";
      const path = id ? `${url}/${id}` : url;
      const response = await Api.get(path);
      return response.data;
    }
  );
  const activeList = ["#84aaff", "#0069d0"];

  return (
    <AsyncDataLoad {...{ isLoading, error }}>
      <Typography.Subtitle>
        Atendimentos por linha de cuidado
      </Typography.Subtitle>
      <div
        className="chart-container"
        style={{
          display: "flex",
          justifyContent: "space-evenly",
          alignItems: "center",
        }}
      >
        {isLoading && <h1>Carregando</h1>}
        {!isLoading &&
          data &&
          data?.map((item: any, index: number) => {
            return (
              <PieChart
                key={index}
                {...new TPieChart(
                  item.label,
                  [{ value: item.value }, { value: item.total }],
                  activeList[index]
                )}
              />
            );
          })}
      </div>
    </AsyncDataLoad>
  );
};

export default AtendimentoLinhaCuidado;
