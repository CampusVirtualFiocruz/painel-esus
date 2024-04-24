export const setupPieChart = (
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
  series: [
    {
      name: 'pie',
      type: 'pie',
      radius: '80%',
      center: ['50%', '50%'],
      animationDuration: 1000,
      label: {
        show: true,
        position: 'center',
        fontSize: '16',
        fontWeight: 'bold',
      },
      itemStyle: {
        shadowBlur: 10,
        shadowOffsetX: 0,
        shadowColor: 'rgba(0, 0, 0, 0.5)',
      },
      // labelLine: {
      //   show: false,
      // },
      data: input,
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)',
        },
      },
    },
  ],
});
