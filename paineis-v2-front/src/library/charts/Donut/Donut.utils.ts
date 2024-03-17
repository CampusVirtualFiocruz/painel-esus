export const setupDonutChart = (
  input: Array<{
    name: string;
    value: number;
  }>
) => ({
  color: ['#78b4d0', '#2775b0'],
  tooltip: {
    trigger: 'item',
    formatter: '({d}%)',
  },
  legend: {
    bottom: 10,
    left: 'center',
    data: ['CityA', 'CityB'],
  },
  label: {
    show: true,
    position: 'center',
    fontSize: '16',
    fontWeight: 'bold',
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: '50%',
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.3)',
        },
      },
      data: input,
    },
  ],
});
