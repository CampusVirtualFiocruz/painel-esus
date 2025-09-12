import ReactECharts from 'echarts-for-react';

// Função para formatar porcentagem com vírgula (padrão brasileiro)
const formatPercentBrazilian = (percent: number): string => {
  return percent.toLocaleString('pt-BR', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
};

export const Zonas = ({ charts }: any) => {
  const nome = 'Zonas Urbana/Rural';
  const dados = [
    {
      value:
        charts?.['tipo-localizacao']?.data?.find(
          ({ tag }: any) => tag === 'urbano'
        )?.value || 0,
      name: 'Zona Urbana',
    },
    {
      value:
        charts?.['tipo-localizacao']?.data?.find(
          ({ tag }: any) => tag === 'rural'
        )?.value || 0,
      name: 'Zona Rural',
    },
    {
      value:
        charts?.['tipo-localizacao']?.data?.find(
          ({ tag }: any) => tag === 'nao_informado'
        )?.value || 0,
      name: 'Não informado',
    },
  ];

  const options = {
    color: ['#0069d0', '#84aaff', '#d3d4dd'],
    tooltip: {
      trigger: 'item',
      formatter(params: any) {
        const value = params.value;
        const percent = params.percent;
        const formattedPercent = formatPercentBrazilian(percent);
        return `${params.name}: ${value} (${formattedPercent}%)`;
      },
    },
    series: [
      {
        name: nome,
        type: 'pie',
        radius: ['30', '52'],
        avoidLabelOverlap: false,
        label: {
          show: false,
          position: 'center',
        },
        emphasis: {
          label: {
            show: true,
            fontSize: '12',
            fontWeight: 'bold',
          },
        },
        labelLine: {
          show: false,
        },
        data: dados,
      },
    ],
  };

  return (
    <ReactECharts
      option={options}
      opts={{ renderer: 'svg' }}
      style={{
        width: '116px',
        height: '116px',
      }}
    />
  );
};
