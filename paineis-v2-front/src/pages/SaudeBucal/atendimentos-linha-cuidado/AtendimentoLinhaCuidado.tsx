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
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
        }}
      >
        {isLoading && <h1>Carregando</h1>}
        {!isLoading &&
          data &&
          data?.map((item: any, index: number) => {
            return (
              <div>
                <Typography.Details> {item.label}</Typography.Details>
                <PieChart
                  key={index}
                  {...new TPieChart(
                    item.label,
                    [
                      { value: item.value, name: "Valor específico" } as any,
                      {
                        value: item.total,
                        name: "Valor total",
                      } as any,
                    ],
                    activeList[index]
                  )}
                />
              </div>
            );
          })}
      </div>
    </AsyncDataLoad>
  );
};

export default AtendimentoLinhaCuidado;
