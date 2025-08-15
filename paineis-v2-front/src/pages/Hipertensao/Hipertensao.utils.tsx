import { Bar, Waffle } from "../../components/charts";
import DetailsTable from "../../components/charts/DetailsTable";
import { PieGroup } from "../../components/charts/PieGroup";

export const reportLeftSections: any = () => [
  {
    row: {
      "por-sexo": {
        Chart: Bar,
        config: {
          overrideTitle: "total-faixa-atendidas",
          colors: ["#84aaff", "#0069d0", "#e4e4e4", "#5c7ea0"],
          componentStyle: {
            height: "500px",
            width: "600px",
            margin: "0 auto",
          },
          yAxis: {
            name: "Total de pessoas",
          },
          xAxis: {
            name: "",
          },
        },
      },
      exames: {
        Chart: DetailsTable,
        config: {
          overrideTitle: "hipertensao-exames",
        }
      },
    },
  },
];

export const reportRightSections: any = () => [
  {
    row: {
      "por-raca-cor": {
        Chart: Waffle,
        config: {
          overrideTitle: "hipertensao-por-raca-cor",
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
          componentStyle: {
            marginTop: "60px",
            paddingBottom: "60px",
          },
        },
      },
      complicacoes: {
        Chart: PieGroup,
        config: {
          overrideTitle: "hipertensao-complicacoes",
          formatterKind: "perc",
          radius: [20, 40],
        },
      },
      imc: {
        Chart: PieGroup,
        subtitle: "(IMC de pessoas com idade de 20 anos ou mais e menores de 60 anos)",
        config: {
          overrideTitle: "hipertensao-imc",
          formatterKind: "perc",
          radius: [0, 50],
        },
      },
    },
  },
];
