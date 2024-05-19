//
// Tipos de suporte
//
type groupedValuesInput = Array<{
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
  config?: generalConfigs;
};

type PercentualChart = {
  data: valueInput;
  config?: generalConfigs;
};

//
// Tipos finais de gráficos
//
type BarChart = LinearChart;
type LineChart = LinearChart;
type PieChart = PercentualChart;
type DonutChart = PercentualChart;
