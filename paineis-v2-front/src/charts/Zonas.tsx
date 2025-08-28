import ReactECharts from "echarts-for-react";

export const Zonas = ({ charts }: any) => {
  let nome = "Zonas Urbana/Rural";
  let dados = [
    {
      value:
        charts?.["tipo-localizacao"]?.data?.find(
          ({ tag }: any) => tag === "urbano"
        )?.value || 0,
      name: "Zona Urbana",
    },
    {
      value:
        charts?.["tipo-localizacao"]?.data?.find(
          ({ tag }: any) => tag === "rural"
        )?.value || 0,
      name: "Zona Rural",
    },
    {
      value:
        charts?.["tipo-localizacao"]?.data?.find(
          ({ tag }: any) => tag === "nao_informado"
        )?.value || 0,
      name: "Não informado",
    },
  ];

  const options = {
    color: ["#0069d0", "#84aaff", "#d3d4dd"],
    tooltip: {
      trigger: "item",
    },
    series: [
      {
        name: nome,
        type: "pie",
        radius: ["30", "52"],
        avoidLabelOverlap: false,
        label: {
          show: false,
          position: "center",
        },
        emphasis: {
          label: {
            show: true,
            fontSize: "12",
            fontWeight: "bold",
          },
        },
        labelLine: {
          show: false,
        },
        data: dados,
      },
    ],
  };

  return (
    <ReactECharts
      option={options}
      opts={{ renderer: "svg" }}
      style={{
        width: "116px",
        height: "116px",
      }}
    />
  );
};
