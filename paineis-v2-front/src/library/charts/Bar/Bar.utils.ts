export const styleOptions = [
  {
    color: '#78b4d0',
    shadowBlur: 4,
    shadowColor: 'rgba(0,0,0,0.1)',
  },
  {
    color: '#2775b0',
    shadowBlur: 5,
    shadowColor: 'rgba(0,0,0,0.1)',
  },
];

export const setupBarChart = ({
  labels,
  series,
}: {
  labels: Array<string>;
  series: Array<{
    name: string;
    data: Array<number>;
  }>;
}) => ({
  xAxis: {
    type: 'category',
    data: labels,
    axisLine: { onZero: true },
    splitLine: { show: false },
    splitArea: { show: false },
    axisTick: {
      show: false,
    },
    axisLabel: {
      show: true,
      fontSize: 16,
      margin: 10,
      rotate: 90,
    },
  },
  yAxis: {
    type: 'value',
    axisLabel: {
      show: true,
      fontSize: 16,
      margin: 6,
    },
    splitLine: {
      show: false,
    },
    axisLine: {
      show: true,
    },
    axisTick: {
      show: true,
    },
  },
  legend: {
    bottom: '0%',
  },
  grid: {
    width: 'auto',
    left: 50,
    bottom: 150,
  },
  series: series.map((s, i) => ({
    name: s.name,
    data: s.data,
    type: 'bar',
    stack: 'one',
    barWidth: '50%',
    itemStyle: styleOptions[i % 2],
  })),
});
