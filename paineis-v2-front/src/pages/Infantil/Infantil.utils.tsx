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
          },
          yAxis: {
            name:content?.["infantil-total-criancas-cadastradas"],
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
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
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
            height: "250px",
          },
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          colors: ["to-be-defined", "#E4E4E4"],
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
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≤ 8,0%",
              window: [{ min: -99999, max: 8 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "> 8% e ≤ 10%",
              window: [{ min: 8.0001, max: 10 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "> 10% e ≤ 12%",
              window: [{ min: 10.0001, max: 12 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "> 12%",
              window: [{ min: 12.0001, max: 999999 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
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
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-uma-visita-31-dia-6-meses": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-uma-consulta-12-meses": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-uma-consulta-12-24-meses": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-marcos-desenvolvimento-avaliados": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
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
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "infantil-nota-consumo-alimentar-avaliado": {
        Chart: Donut,
        config: {
          halfDonut: true,
          formatterKind: "perc",
          radius: [0, 60],
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 50,0%",
              window: [{ min: 50, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 37,5% e < 50%",
              window: [{ min: 37.5, max: 50 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 25% e < 37,5%",
              window: [{ min: 25, max: 37.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 25%",
              window: [{ min: -1, max: 25 }],
            },
          ],
          componentStyle: {
            height: "250px",
          },
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
  },
];
