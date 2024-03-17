import ReactECharts from 'echarts-for-react';
import { setupDonutChart } from './Donut.utils';
import './style.scss';

export type DonutChartProps = {
  datasource: Array<{
    name: string;
    value: number;
  }>;
};

const Donut = ({ datasource }: DonutChartProps) =>
  Boolean(datasource) && (
    <div className="donut">
      <ReactECharts
        option={setupDonutChart(datasource)}
        style={{
          width: '300px',
          height: '300px',
        }}
        opts={{ renderer: 'svg' }}
      />
    </div>
  );

export default Donut;
