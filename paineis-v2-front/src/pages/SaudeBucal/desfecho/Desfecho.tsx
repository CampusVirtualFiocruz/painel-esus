import { useParams } from "react-router-dom";
import { PainelParams } from "../faixa-etaria/FaixaEtaria";
import { useQuery } from "react-query";
import { Api } from "../../../services/api";
import { STALE_TIME } from "../../../config/stale-time";
import "./style.scss";
import { Progress } from "reactstrap";
import AsyncDataLoad from "../async-data-load";
import { Typography } from "../../../components/ui/Typography";

type DesfechResponse = {
  label: string;
  value: number;
  percent: number;
};
const random_hex_color_code = () => {
  let n = (Math.random() * 0x361949 * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};
const Desfecho = () => {
  const { id } = useParams<PainelParams>();
  const {
    data: desfechoResponse,
    isLoading,
    error,
  } = useQuery(
    ["saude-bucal-desfecho", id],
    async () => {
      const url = "oral-health/get-cares-by-outcome";
      const path = id ? `${url}/${id}` : url;
      const response = await Api.get<DesfechResponse[]>(path);
      return response.data;
    },
    {
      staleTime: STALE_TIME,
    }
  );
  return (
    <AsyncDataLoad {...{ isLoading, error }}>
      <div className="col-12">
        <Typography.Subtitle>
          Saúde Bucal por desfecho de atendimento
        </Typography.Subtitle>
        {!isLoading &&
          desfechoResponse &&
          Array.from(desfechoResponse).map(
            (item: DesfechResponse, i: number) => (
              <div key={i} className="d-flex align-items-center mt-2">
                <div className="desfecho d-flex">
                  <div className="container-extratificacao-atendimentos w70 d-flex">
                    <span className="profissao-nome">{item.label}</span>
                  </div>
                  <div className="w30 d-flex hprogess">
                    <Progress
                      value={item.percent}
                      className="w-75 hprogess"
                      barStyle={{ backgroundColor: random_hex_color_code() }}
                    />
                  </div>
                </div>
                <span className="total ms-2 wpercent">{item.percent}%</span>
              </div>
            )
          )}
      </div>
    </AsyncDataLoad>
  );
};

export default Desfecho;
