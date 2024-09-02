import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import { Api } from "../../../services/api";
import { Typography } from "../../../components/ui/Typography";
import Card from "../../../components/ui/Card";
import AsyncDataLoad from "../async-data-load";
import Medkit from "../../../assets/images/medkit.png";

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
    <Card>
      <AsyncDataLoad {...{ isLoading, error }}>
        <div style={{ display: "flex", width: "100%" }}>
          <Typography.Details style={{ flex: "2" }}>
            Total de atendimentos
            <br />
            nos últimos 12 meses
          </Typography.Details>
          <div
            style={{
              display: "flex",
              flex: "1",
              flexDirection: "row",
              justifyContent: "center",
              alignItems: "center",
              justifyItems: "center",
              gap: "10px",
            }}
          >
            <img
              src={Medkit}
              width="24px"
              alt="Ícone de kit médico de emergência"
            />
            <Typography.Subtitle style={{ width: "initial" }}>
              {dataTotal?.total.toLocaleString("pt-BR")}
            </Typography.Subtitle>
          </div>
        </div>
      </AsyncDataLoad>
    </Card>
  );
};

export default TotalAtendimentos;
