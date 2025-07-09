//
// Tipos de suporte
//

import { ReportViewTypeEnum } from "../../utils/viewTypeEnum";

export type groupedValuesInput = Array<{
  value: {
    [tag: string]: number;
  };
  tag: string;
}>;

type valueInput = Array<{
  value: Number;
  tag: string;
  percent?: Number;
}>;

type MultipleGroupedValuesInput = {
  [tag: string]: {
    [section: string]: number;
  };
};

type generalConfigs = {
  isDisabledResponse?: boolean;
  isErrorResponse?: boolean;
  isIsDevelopmentResponse?: boolean;
  colors?: Array<string>;
  formatterKind?: string;
  componentStyle?: object;
  reportViewType?: ReportViewTypeEnum.EQUIPE | ReportViewTypeEnum.UBS |  ReportViewTypeEnum.MUNICIPIO;
};

type LinearChart = {
  data: groupedValuesInput;
  config?: {
    xAxis?: { name?: string; sort: any };
    yAxis?: { name?: string };
    hideLegend?: boolean;
    invertAxis?: boolean;
  } & generalConfigs;
};

type PercentualChart = {
  data: valueInput;
  config?: generalConfigs & {
    radiusStart?: number | string;
  };
};

type PercentualGroupChart = {
  data: Array<{ tag?: string; value?: number; data?: valueInput }>;
  config?: generalConfigs & {
    radiusStart?: number;
    highlightTag?: string;
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

type Pyramid = {
  data: {
    left: groupedValuesInput;
    right: groupedValuesInput;
  };
  config?: generalConfigs;
};

//
// Tipos finais de gráficos
//

export type BarChart = LinearChart;
export type LineChart = LinearChart;

export type PieChart = PercentualChart;
export type ProgressListChart = PercentualChart;
export type DonutChart = PercentualChart & {
  config?: generalConfigs & {
    subtitle?: string;
    radius?: number | string;
    radiusStart?: number | string;
    halfDonut?: boolean;
    roseType?: string;
    sort?: any;
    rangedLegend?: Array<any>
  };
};
export type DonutGroupChart = PercentualGroupChart;
export type TreemapShallowChart = PercentualChart;
export type WaffleChart = PercentualChart;

export type ValueChart = Value;
export type TableGroup = MultipleGroupedValuesInput;

export type PyramidChart = Pyramid;
