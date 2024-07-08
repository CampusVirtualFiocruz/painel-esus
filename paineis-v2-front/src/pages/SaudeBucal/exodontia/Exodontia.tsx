import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import ReactECharts from "echarts-for-react";
import { Api } from "../../../services/api";
import AsyncDataLoad from "../async-data-load";
import { STALE_TIME } from "../../../config/stale-time";
import { Typography } from "../../../components/ui/Typography";
import "./style.scss";

type PainelParams = {
  id: string;
};

type ExodontiaResponse = {
  label: string;
  total: number;
  value: number;
};

const ExodontiaPie = (props: ExodontiaResponse[]) => {
  props = Object.values(props);
  const data = props?.map((i: ExodontiaResponse) => ({
    value: i.value,
    name: i.label,
  }));

  const options = {
    color: ["#09406a", "#84aaff", "#78a4d0", "#e4e4e4"],
    tooltip: {
      trigger: "item",
      formatter: "{b0}: {c0}({d}%)",
    },
    title: {
      text: "",
      left: "center",
      top: "0",
      bottom: "auto",
      textStyle: {
        fontSize: 16,
        overflow: "break",
        width: 120,
      },
    },
    series: [
      {
        name: "",
        type: "pie",
        radius: "70%",
        center: ["50%", "50%"],
        animationDuration: 1000,
        avoidLabelOverlap: false,
        label: {
          show: true,
          position: "outside",
          overflow: "break",
          fontSize: "16",
          fontWeight: "bold",
          width: 120,
          // padding: [53, 10, 10, 5],
          formatter: "{b|{d}%} \n\n{a|{b}}",
          rich: {
            a: {
              color: "#6E7079",
              fontWeight: "bold",
              fontSize: 14,
              align: "center",
            },
            b: {
              color: "#6E7079",
              fontWeight: "bold",
              fontSize: 25,
              align: "center",
            },
          },
          distanceToLabelLine: 5,
        },
        emphasis: {
          label: {
            show: true,
            fontSize: "16",
            fontWeight: "bold",
          },
        },
        labelLine: {
          show: false,
        },
        data: data,
      },
    ],
  };
  return (
    <div className="pie-chart">
      <ReactECharts
        option={options}
        style={{
          width: "80vw",
          minWidth: "316px",
          // height: '40vh'
        }}
        opts={{ renderer: "svg" }}
      />
      <div className="data-info d-flex flex-column align-items-center"></div>
    </div>
  );
};
const Exodontia = () => {
  const { id } = useParams<PainelParams>();
  const {
    data: exodontiaResponse,
    isLoading,
    error,
  } = useQuery(
    ["saude-bucal-exodontia", id],
    async () => {
      const url = "oral-health/get-extraction-procedures-proportion";

      let path = id ? `${url}/${id}` : url;
      const response = await Api.get<ExodontiaResponse[]>(path);
      return response.data;
    },
    {
      staleTime: STALE_TIME,
    }
  );
  return (
    <AsyncDataLoad {...{ isLoading, error }}>
      <Typography.Subtitle>
        Proporção de exodontia por procedimento
      </Typography.Subtitle>
      <div className="col-12 dflex">
        {!isLoading && exodontiaResponse && (
          <ExodontiaPie {...exodontiaResponse} />
        )}
      </div>
    </AsyncDataLoad>
  );
};

export default Exodontia;
