import { Bar, Donut, Waffle } from "../../components/charts";
import { content } from "../../assets/content/content";

export const reportSections: any = (recorte: "atendidas" | "cadastradas") => [
  {
    row: {
      "pessoas-por-sexo": {
        Chart: Bar,
        config: {
          overrideTitle:
            recorte === "atendidas"
              ? "total-faixa-atendidas"
              : "total-faixa-cadastradas",
          colors: ["#84aaff", "#0069d0", "#e4e4e4", "#5c7ea0"],
          componentStyle: {
            height: "500px",
          },
          yAxis: {
            name:
              recorte === "atendidas"
                ? content?.["total-atendidas"]
                : content?.["total-cadastradas"],
          },
          xAxis: {
            name: "",
          },
        },
      },
      "distribuicao-pessoas-raca-cor": {
        Chart: Waffle,
        config: {
          overrideTitle:
            recorte === "atendidas"
              ? "distribuicao-atendidas"
              : "distribuicao-cadastradas",
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
      "primeira-consulta-odonto": {
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
      "concluido-tratamento": {
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
      "realizou-exodontia": {
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
      "realizou-preventivo-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [40, 60],
          componentStyle: {
            height: "250px",
          },
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 75% e ≤ 85%",
              window: [{ min: 75, max: 85 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 60% e < 75% ou > 85% e ≤ 90%",
              window: [
                { min: 60, max: 75 },
                { min: 85.0001, max: 90 },
              ],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 40% e < 60% ou > 90% e ≤ 95%",
              window: [
                { min: 40, max: 60 },
                { min: 90.0001, max: 95 },
              ],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 40% ou > 95%",
              window: [
                { min: -1, max: 40 },
                { min: 95.0001, max: 999999 },
              ],
            },
          ],
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
      "realizou-tra-odonto": {
        Chart: Donut,
        config: {
          formatterKind: "perc",
          radius: [40, 60],
          componentStyle: {
            height: "250px",
          },
          sort: ["Realizado", "Não Realizado"],
          rangedLegend: [
            {
              color: "#49E8DB",
              title: "Ótimo",
              text: "≥ 6%",
              window: [{ min: 6, max: 9999 }],
            },
            {
              color: "#84aaff",
              title: "Bom",
              text: "≥ 4,5% e < 6%",
              window: [{ min: 4.5, max: 6 }],
            },
            {
              color: "#0069D0",
              title: "Suficiente",
              text: "≥ 3% e < 4,5%",
              window: [{ min: 3, max: 4.5 }],
            },
            {
              color: "#0A406A",
              title: "Regular",
              text: "< 3%",
              window: [{ min: -1, max: 3 }],
            },
          ],
          colors: ["to-be-defined", "#E4E4E4"],
          yAxis: {
            name: content?.["total-cadastros"],
          },
        },
      },
    },
  },
];
