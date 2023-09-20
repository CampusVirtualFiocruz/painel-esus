import ReactECharts from 'echarts-for-react';

export function Ibge({ data }: any) {
    const options = {
        color: ['#2775b0', '#78b4d0'],
        series: [
            {
                name: 'População estimada (IBGE)',
                type: 'pie',
                radius: '40px',
                center: ["50%", "50%"],
                data: data,
                label: {
                    position: 'top',
                    show: true,
                    formatter: ['{b}'].join('\n'),
                    fontSize: 16,
                    color: '#FFF',
                    alignTo: 'labelLine',
                    distanceToLabelLine: -24

                },
                emphasis: {
                    itemStyle: {
                        shadowBlur: 5,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };

    return (
        <>
            <ReactECharts
                option={options}
                style={{
                    width: "125px",
                    height: "125px",
                }}
                opts={{ renderer: 'svg' }}
            />
        </>
    );
}
