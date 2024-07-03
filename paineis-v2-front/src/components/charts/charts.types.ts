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
};

type LinearChart = {
  data: groupedValuesInput;
  config?: {
    xAxis?: { name?: string };
    yAxis?: { name?: string };
  } & generalConfigs;
};

type PercentualChart = {
  data: valueInput;
  config?: generalConfigs;
};

//
// Tipos finais de gráficos
//
export type BarChart = LinearChart;
export type LineChart = LinearChart;
export type PieChart = PercentualChart;
export type DonutChart = PercentualChart;
