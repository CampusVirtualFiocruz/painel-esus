import { Bar, Donut, Waffle } from "../../components/charts";
import { content } from "../../assets/content/content";

export const fixedLegend = [
  {
    color: "#49E8DB",
    title: "Ótimo",
    text: "≥ 50,0%",
    min: 50,
    max: 9999,
  },
  {
    color: "#84aaff",
    title: "Bom",
    text: "Entre ≥37,5% e < 50,0%",
    min: 37.5,
    max: 50,
  },
  {
    color: "#0069D0",
    title: "Suficiente",
    text: "Entre ≥25,0% e < 37,5%",
    min: 25,
    max: 37.5,
  },
  {
    color: "#0A406A",
    title: "Regular",
    text: "< 25,0%",
    min: -1,
    max: 25,
  },
];

export const reportSections: any = (recorte: "atendidos" | "cadastrados") => [
  {
    row: {
      "pessoas-por-sexo": {
        Chart: Bar,
        config: {
          overrideTitle: recorte === "atendidos" ? "total-faixa-atendidas" : "total-faixa-cadastradas",
          colors: ["#84aaff", "#0069d0", "#e4e4e4", "#5c7ea0"],
          componentStyle: {
            height: "500px",
          },
          yAxis: {
            name: recorte === "atendidos" ? content?.["total-atendidas"] : content?.["total-cadastradas"],
          },
          xAxis: {
            name: "",
          },
        },
      },
      "distribuicao-pessoas-raca-cor": {
        Chart: Waffle,
        config: {
          overrideTitle: recorte === "atendidos" ? "distribuicao-atendidas" : "distribuicao-cadastradas",
          formatterKind: "perc",
          radiusStart: "0%",
          sort: [
            "Branca",
            "Preta",
            "Amarela",
            "Parda",
            "Indígena",
            "Não informado",
          ],
        },
      },
    },
  },
];

export const realizedProceduresCharts: any = [
  {
    firstRow: {
      "primeira-consulta-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 80],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "realizou-exodontia": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 80],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "realizou-preventivo-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 80],
          componentStyle: {
            height: "250px",
          },
          sort: ["Realizado", "Não Realizado"],
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
    secondRow: {
      "realizou-tra-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [50, 80],
          componentStyle: {
            height: "250px",
          },
          sort: ["Realizado", "Não Realizado"],
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "realizou-escovacao-supervisionada": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [50, 80],
          componentStyle: {
            height: "250px",
          },
          sort: ["Realizado", "Não Realizado"],
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
  },
];

export const getColorizedCharts = (reportData: any) => {
  const colorizedProceduresCharts: any = [{ firstRow: {}, secondRow: {} }];

  const colorizeContent = (input: string) => (key: string) => {
    let newChartColor;

    const localData = reportData?.data?.[key]?.data;

    let hasHighlightConfig =
      localData &&
      Array.isArray(localData) &&
      localData?.[1]?.tag === "realizado";

    let percentage: any;

    if (hasHighlightConfig) {
      const mainValue = localData?.[1]?.value;
      const total = mainValue + localData?.[0]?.value;
      percentage = (mainValue / total) * 100;
    }

    fixedLegend.forEach(({ color, min, max }) => {
      const shouldHighlight = percentage >= min && percentage < max;
      if (shouldHighlight) {
        newChartColor = color;
      }
    });

    colorizedProceduresCharts[0][input][key] =
      realizedProceduresCharts[0][input][key];
    colorizedProceduresCharts[0][input][key].config.colors = [
      newChartColor,
      "#E4E4E4",
    ];
  };

  const colorize = (input: any) => {
    Object.keys(realizedProceduresCharts?.[0]?.[input]).forEach(
      colorizeContent(input)
    );
  };

  colorize("firstRow");
  colorize("secondRow");

  return colorizedProceduresCharts;
};
