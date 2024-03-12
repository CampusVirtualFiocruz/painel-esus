import ReactECharts from 'echarts-for-react';
import './style.scss';
import { setupBarChart } from './Bar.utils';

export type BarChartProps = { title: string, datasource: {
  labels: Array<string>;
  series: Array<{
    name: string;
    data: Array<number>;
  }>;
}};

const Bar = ({ title, datasource }: BarChartProps) => (
  <div className="bar">
    {title && <div className="vertical ms-1 me-4">{title}</div>}
    {datasource && <ReactECharts
      option={setupBarChart(datasource)}
      style={{
        width: '100%',
        minWidth: '370px',
        height: '484px',
      }}
      opts={{ renderer: 'svg' }}
    />}
  </div>
);

export default Bar;
