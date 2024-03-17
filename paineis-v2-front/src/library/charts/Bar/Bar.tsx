import ReactECharts from 'echarts-for-react';
import { setupBarChart } from './Bar.utils';
import './style.scss';

export type BarChartProps = {
  datasource: {
    labels: Array<string>;
    series: Array<{
      name: string;
      value: Array<number>;
    }>;
  };
};

const Bar = ({ datasource }: BarChartProps) =>
  Boolean(datasource) && (
    <div className="bar-chart">
      <ReactECharts
        option={setupBarChart(datasource)}
        style={{
          width: '100%',
          minWidth: '370px',
          height: '484px',
        }}
        opts={{ renderer: 'svg' }}
      />
    </div>
  );

export default Bar;
