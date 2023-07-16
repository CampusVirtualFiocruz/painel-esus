import ReactECharts from 'echarts-for-react'
import './style.scss';

type Faixa = {
    NaN?: number;
    Feminino?: string;
    Masculino?: number;
}

type BarData = {
    data: any;
    titulo: string;
}

export function BarSexo({ data, titulo }: BarData) {
    let sexo = Object.keys(data).map(function (key) {
        return String(key);
    });

    let arrData = Object.entries(data).map(function (obj: any) {
        let objFaixa = obj[1];

        if (!objFaixa.hasOwnProperty('Feminino') || !objFaixa.hasOwnProperty('Masculino')) {
            return {
                'NaN': objFaixa.NaN,
                'Feminino': 0,
                'Masculino': 0
            }
        }

        return objFaixa;
    });
    let dataFeminino = arrData.map((obj: Faixa) => {
        return obj.Feminino;

    });
    let dataMasculino = arrData.map((obj: Faixa) => {
        return obj.Masculino;
    });

    const options = {
        legend: {
            bottom: "0%"
        },
        xAxis: {
            data: sexo,
            axisLine: { onZero: true },
            splitLine: { show: false },
            splitArea: { show: false },
            axisTick: {
                show: false
            },
            axisLabel: {
                show: true,
                fontSize: 16,
                margin: 10,
                rotate: 90
            }
        },
        yAxis: {
            axisLabel: {
                show: true,
                fontSize: 16,
                margin: 6
            },
            splitLine: {
                show: false
            },
            axisLine: {
                show: true,
            },
            axisTick: {
                show: true
            }
        },
        grid: {
            width: "auto",
            left: 50,
            bottom: 150
        },
        series: [
            {
                name: 'Feminino',
                type: 'bar',
                stack: 'one',
                barWidth: '50%',
                itemStyle: {
                    color: '#78b4d0',
                    shadowBlur: 4,
                    shadowColor: 'rgba(0,0,0,0.1)'
                },
                data: dataFeminino
            },
            {
                name: 'Masculino',
                type: 'bar',
                stack: 'one',
                barWidth: '50%',
                itemStyle: {
                    color: '#2775b0',
                    shadowBlur: 5,
                    shadowColor: 'rgba(0,0,0,0.1)'
                },
                data: dataMasculino
            }
        ]
    };

    return (
        <div className='bar'>
            <div className="vertical ms-1 me-4">{titulo}</div>

            <ReactECharts
                option={options}
                style={{
                    width: "100%",
                    minWidth: "370px",
                    height: "484px"
                }}
                opts={{ renderer: 'svg' }}
            />
        </div>
    )
}
