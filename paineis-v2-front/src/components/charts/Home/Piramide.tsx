import ReactECharts from "echarts-for-react";
import { content } from "../../../assets/content/content";
import feminino from "../../../assets/images/feminino.svg";
import masculino from "../../../assets/images/masculino.svg";
import { Typography } from "../../ui/Typography";

type NewData = {
  left: {
    tag: string;
    value: { urbano: number; rural: number; "nao-informado": number };
  }[];
  right: {
    tag: string;
    value: { urbano: number; rural: number; "nao-informado": number };
  }[];
};

export function transformNewDataToOldData(newDataInput: NewData) {
  function buildGenderData(
    arr: NewData["left"] | NewData["right"],
    type: string
  ) {
    const areaUrbana: any = {};
    const areaRural: any = {};
    const nao_informado: any = {};

    arr.forEach((item) => {
      const ageLabel = content?.[item.tag] || item.tag;
      areaUrbana[ageLabel] = {
        value: item.value.urbano,
        label: "Urbano",
        itemStyle: { color: "#0069d0" },
      };
      areaRural[ageLabel] = {
        value: item.value.rural,
        label: "Rural",
        itemStyle: { color: "#84aaff" },
      };
      nao_informado[ageLabel] = {
        value: item.value["nao-informado"],
        label: "Não Informado",
        itemStyle: { color: "#e9ecef" },
      };
    });

    return { type, areaUrbana, areaRural, nao_informado };
  }

  if (!newDataInput || !newDataInput.left || !newDataInput.right) {
    return [];
  }

  return [
    buildGenderData(newDataInput?.left, "Masculino"),
    buildGenderData(newDataInput?.right, "Feminino"),
  ];
}

const PyramidChart = ({ data }: any) => {
  const finalInput = transformNewDataToOldData(data);

  const waterMarkText = "ECHARTS";
  const canvas = document.createElement("canvas");
  const ctx = canvas.getContext("2d");

  canvas.width = canvas.height = 100;

  if (ctx) {
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.globalAlpha = 0.08;
    ctx.font = "18px Microsoft Yahei";
    ctx.translate(50, 50);
    ctx.rotate(-Math.PI / 4);
    ctx.fillText(waterMarkText, 0, 0);
  }

  const options = {
    tooltip: {
      trigger: "item",
      formatter: function (params: any) {
        return `${params.name}<br />${params.marker}${params.data.label}: ${params.value}`;
      },
    },
    legend: {
      orient: "horizontal",
      right: 10,
      top: "center",
      icon: "rect",
    },
    grid: [
      {
        top: 0,
        width: "35%",
        bottom: 0,
        right: "51%",
        containLabel: false,
      },
      {
        top: 0,
        width: "35%",
        bottom: 0,
        left: "51%",
        containLabel: false,
      },
    ],
    xAxis: [
      {
        type: "value",
        splitLine: {
          show: false,
        },
        inverse: true,
      },
      {
        type: "value",
        gridIndex: 1,
        splitLine: {
          show: false,
        },
      },
    ],
    yAxis: [
      {
        gridIndex: 0,
        type: "category",
        data: Object.keys(finalInput[0].areaUrbana),
        inverse: true,
        axisLabel: {
          show: true,
          fontSize: 16,
          margin: 8,
          width: "10%",
        },
        axisLine: {
          show: false,
        },
        axisTick: {
          show: false,
        },
      },
      {
        gridIndex: 1,
        type: "category",
        data: Object.keys(finalInput[0].areaUrbana),
        inverse: true,
        position: "right",
        offset: 0,
        axisLine: {
          show: false,
        },
        axisLabel: {
          margin: 10,
          fontSize: 16,
        },
        axisTick: {
          show: false,
        },
      },
    ],
    series: [
      {
        type: "bar",
        barWidth: "18px",
        stack: "masculino",
        z: 3,
        xAxisIndex: 0,
        yAxisIndex: 0,
        data: Object.keys(finalInput[0].nao_informado).map(function (key) {
          return finalInput[0].nao_informado[key];
        }),
      },
      {
        type: "bar",
        barWidth: "18px",
        stack: "masculino",
        z: 3,
        style: {
          font: "28px sans-serif",
        },
        xAxisIndex: 0,
        yAxisIndex: 0,
        data: Object.keys(finalInput[0].areaUrbana).map(function (key: string) {
          return finalInput[0].areaUrbana[key];
        }),
      },
      {
        type: "bar",
        barWidth: "18px",
        stack: "masculino",
        z: 3,
        xAxisIndex: 0,
        yAxisIndex: 0,
        data: Object.keys(finalInput[0].areaRural).map(function (key) {
          return finalInput[0].areaRural[key];
        }),
      },

      {
        type: "bar",
        barWidth: "18px",
        stack: "feminino",
        z: 3,
        xAxisIndex: 1,
        yAxisIndex: 1,
        data: Object.keys(finalInput[1].nao_informado).map(function (key) {
          return finalInput[1].nao_informado[key];
        }),
      },
      {
        type: "bar",
        barWidth: "18px",
        stack: "feminino",
        z: 3,
        xAxisIndex: 1,
        yAxisIndex: 1,
        data: Object.keys(finalInput[1].areaUrbana).map(function (key) {
          return finalInput[1].areaUrbana[key];
        }),
      },
      {
        type: "bar",
        barWidth: "18px",
        stack: "feminino",
        z: 3,
        xAxisIndex: 1,
        yAxisIndex: 1,
        data: Object.keys(finalInput[1].areaRural).map(function (key) {
          return finalInput[1].areaRural[key];
        }),
      },
    ],
  };

  return (
    <>
      <ReactECharts
        option={options}
        style={{
          width: "100%",
          height: "600px",
        }}
        className="my-5"
        opts={{ renderer: "svg" }}
      />
    </>
  );
};

const Piramide = ({ charts }: any) => (
  <>
    <div className="my-5">
      <Typography.Subtitle>
        Proporção de indivíduos cadastrados por sexo e idade
      </Typography.Subtitle>
    </div>

    <div className="graficoPiramide">
      <div className="w-100 painel-demografico">
        <div className="d-flex justify-content-center">
          <div className="mx-2">
            <img src={masculino} className="img-fluid" alt="Masculino" />
          </div>
          <div className="mx-2">
            <img src={feminino} className="img-fluid" alt="Feminino" />
          </div>
        </div>
        <PyramidChart data={charts?.["piramide-etaria"]?.data} />
      </div>
      <div className="d-flex align-items-center justify-content-between mt-5">
        <div className="d-flex align-items-center mx-3">
          <div className="box-container-light me-2"></div>
          <h5 className="mb-0">Zona Urbana</h5>
        </div>
        <div className="d-flex align-items-center mx-3">
          <div className="box-container-dark me-2"></div>
          <h5 className="mb-0">Zona Rural</h5>
        </div>
        <div className="d-flex align-items-center mx-3">
          <div className="box-container-nonactive me-2"></div>
          <h5 className="mb-0">Não Informado</h5>
        </div>
      </div>
    </div>
  </>
);

export default Piramide;
