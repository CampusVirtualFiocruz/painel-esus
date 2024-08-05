import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import { Api } from "../../../services/api";
import AsyncDataLoad from "../async-data-load";
import { Typography } from "../../../components/ui/Typography";
import "./style.scss";

type PainelParams = {
  id: string;
};

type TotalAtendimentosResponse = {
  total: number;
};

const TotalAtendimentos = () => {
  const { id } = useParams<PainelParams>();
  const {
    data: dataTotal,
    isLoading,
    error,
  } = useQuery<TotalAtendimentosResponse>(
    ["saude-bucal-total-atendimentos", id],
    async () => {
      const url = "oral-health/total";
      let path = id ? `${url}/${id}` : url;
      const response = await Api.get(path);
      return response.data;
    }
  );

  return (
    <div id="total-atendimentos">
      <AsyncDataLoad {...{ isLoading, error }}>
        <div className="col-12 chart-container total-atd-container">
          <Typography.Subtitle>Total de atendimentos</Typography.Subtitle>
          <div className="total-atd">
            <span className="total-trimestre">
              {dataTotal?.total.toLocaleString("pt-BR")}
            </span>
          </div>
        </div>
      </AsyncDataLoad>
    </div>
  );
};

export default TotalAtendimentos;
