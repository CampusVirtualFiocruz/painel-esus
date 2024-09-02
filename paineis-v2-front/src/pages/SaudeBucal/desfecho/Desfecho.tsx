import { useParams } from "react-router-dom";
import { Progress } from "reactstrap";
import { useQuery } from "react-query";

import AsyncDataLoad from "../async-data-load";
import { PainelParams } from "../faixa-etaria/FaixaEtaria";
import { Api } from "../../../services/api";
import { STALE_TIME } from "../../../config/stale-time";
import { Typography } from "../../../components/ui/Typography";
import { randomHexColorCode } from "../../../utils/reports";
import "./style.scss";

type DesfechResponse = {
  label: string;
  value: number;
  percent: number;
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

  const defaultColors = ["#0069d0", "#84aaff", "#5c7ea0"];

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
                  <span className="profissao-nome">{item.label}</span>
                  <Progress
                    value={item.percent}
                    className="w-75"
                    barStyle={{
                      backgroundColor:
                        i > defaultColors.length
                          ? randomHexColorCode()
                          : defaultColors[i],
                    }}
                  />
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
