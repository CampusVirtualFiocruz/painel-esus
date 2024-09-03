import { useQuery } from "react-query";
import { useParams } from "react-router-dom";
import ReactECharts from "echarts-for-react";
import { Api } from "../../../services/api";
import AsyncDataLoad from "../async-data-load";
import { STALE_TIME } from "../../../config/stale-time";
import { Typography } from "../../../components/ui/Typography";

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
    color: ["#84aaff", "#0069d0", "#5c7ea0", "#e4e4e4"],
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
        width: 100,
      },
    },
    series: [
      {
        name: "",
        type: "pie",
        radius: "40%",
        center: ["50%", "50%"],
        animationDuration: 800,
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
              color: "#262729",
              fontWeight: "400",
              fontSize: 10,
              align: "center",
            },
            b: {
              color: "#262729",
              fontWeight: "bold",
              fontSize: 22,
              align: "center",
            },
          },
          distanceToLabelLine: -4,
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
    <ReactECharts
      option={options}
      style={{ width: "100%", height: "230px" }}
      opts={{ renderer: "svg" }}
    />
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
      <center>
        <ExodontiaPie {...(exodontiaResponse || [])} />
      </center>
    </AsyncDataLoad>
  );
};

export default Exodontia;
