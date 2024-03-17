import ReactECharts from 'echarts-for-react';
import { setupPieChart } from './Pie.utils';
import './style.scss';

export type PieChartProps = {
  datasource: Array<{
    name: string;
    value: number;
  }>;
};

const Pie = ({ datasource }: PieChartProps) =>
  Boolean(datasource) && (
    <div className="pie">
      <ReactECharts
        option={setupPieChart(datasource)}
        style={{
          width: '200px',
          height: '200px',
        }}
        opts={{ renderer: 'svg' }}
      />
    </div>
  );

export default Pie;
