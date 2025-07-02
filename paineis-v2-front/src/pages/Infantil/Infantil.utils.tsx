import { Bar, Donut, Waffle } from "../../components/charts";
import { content } from "../../assets/content/content";

export const reportSections: any = () => [
  {
    row: {
      "infantil-criancas-faixa-etaria-sexo": {
        Chart: Bar,
        config: {
          colors: ["#84aaff", "#0069d0", "#e4e4e4", "#5c7ea0"],
          componentStyle: {
            height: "500px",
           width: "600px",
           margin: "0 auto"
          },
          yAxis: {
            name: content?.["infantil-total-criancas-cadastradas"],
          },
          xAxis: {
            name: "",
          },
        },
      },
      "infantil-distribuicao-criancas-raca-cor": {
        Chart: Waffle,
        config: {
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

export const reportCharts: any = [
  {
    firstRow: {
      "infantil-primeira-consulta-8-dia": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "250px",
          },
          colors: ["#0069d1", "#e5e5e5", "#818181"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-nove-consultas-2-anos": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 60],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "250px",
          },
          sort: ["Realizado", "Não Realizado"],
          colors: ["#023e6a", "#e5e5e5", "#818181"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-registro-peso-altura": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "250px",
          },
          colors: ["#47e9dc", "#e5e5e5", "#818181"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
    secondRow: {
      "infantil-uma-visita-30-dias": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [30, 60],
          colors: ["#6596ff", "#e5e5e5", "#818181"],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "250px",
          },
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-uma-visita-31-dia-6-meses": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [30, 60],
          colors: ["#023e6a", "#e5e5e5", "#818181"],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "250px",
          },
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
    thirdRow: {
      "infantil-uma-consulta-12-meses": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [30, 60],
          sort: ["Realizado", "Não Realizado"],
          colors: ["#47e9dc", "#e5e5e5", "#818181"],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "250px",
          },
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-uma-consulta-12-24-meses": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [30, 60],
          colors: ["#0069d1", "#e5e5e5", "#818181"],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            height: "250px",
          },
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
    fourthRow: {
      "infantil-marcos-desenvolvimento-avaliados": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          halfDonut: true,
          radius: [30, 60],
          colors: ["#6596ff", "#e5e5e5", "#818181"],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            marginBottom: "-120px",
          },
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-consumo-alimentar-avaliado": {
        Chart: Donut,
        config: {
          halfDonut: true,
          formatterKind: "perc",
          radius: [30, 60],
          colors: ["#023e6a", "#e5e5e5", "#818181"],
          sort: ["Realizado", "Não Realizado"],
          componentStyle: {
            width: "400px",
            minWidth: "400px",
            marginBottom: "-120px",
          },
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
  },
];
