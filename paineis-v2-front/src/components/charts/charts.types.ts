//
// Tipos de suporte
//
export type groupedValuesInput = Array<{
  value: {
    [tag: string]: number;
  };
  tag: string;
}>;

type valueInput = Array<{
  value: Number;
  tag: string;
}>;

type generalConfigs = {
  isDisabledResponse?: boolean;
  isErrorResponse?: boolean;
  isIsDevelopmentResponse?: boolean;
  colors?: Array<string>;
  formatterKind?: string;
};

type LinearChart = {
  data: groupedValuesInput;
  config?: {
    xAxis?: { name?: string };
    yAxis?: { name?: string };
    hideLegend?: boolean;
  } & generalConfigs;
};

type PercentualChart = {
  data: valueInput;
  config?: generalConfigs & {
    radiusStart?: number
  };
};


type Value = {
  data: number;
  config?: {
    description: string;
    info?: string;
    percent?: boolean;
    icon?: React.ReactElement;
  } & generalConfigs;
};

//
// Tipos finais de gráficos
//

export type BarChart = LinearChart;
export type LineChart = LinearChart;

export type PieChart = PercentualChart;
export type DonutChart = PercentualChart;
export type TreemapShallowChart = PercentualChart;

export type ValueChart = Value;
