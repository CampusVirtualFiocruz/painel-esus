import ReactECharts from 'echarts-for-react';

export function Ibge({ data }: any) {
  const options = {
    color: ['#0069d0', '#84aaff'],
    tooltip: {
      trigger: 'item',
    },
    series: [
      {
        name: 'População estimada (IBGE)',
        type: 'pie',
        radius: '40px',
        center: ['50%', '50%'],
        data,
        label: {
          position: 'top',
          show: true,
          formatter: ['{b}'].join('\n'),
          fontSize: 16,
          color: '#FFF',
          alignTo: 'labelLine',
          distanceToLabelLine: -24,
        },
        emphasis: {
          itemStyle: {},
        },
      },
    ],
  };

  return (
    <>
      <ReactECharts
        option={options}
        style={{
          width: '125px',
          height: '125px',
        }}
        opts={{ renderer: 'svg' }}
      />
    </>
  );
}
