import ReactECharts from 'echarts-for-react'
import { formatAsPercent } from '../../utils';
import './style.scss';

export function Donut({ data }: any) {
    let nome = 'prenatal-indicators';
    let comConsulta = data[1].com_consulta;
    let semConsulta = data[1].sem_consulta;

    let dataGraphic = [
        { value: comConsulta },
        { value: semConsulta }
    ];

    const options = {
        color: ['#78b4d0', '#2775b0'],
        tooltip: {
            trigger: "item",
            formatter: "({d}%)"
        },
        series: [
            {
                name: nome,
                type: 'pie',
                radius: ['30', '52'],
                avoidLabelOverlap: false,
                label: {
                    show: true,
                    position: 'center',
                    fontSize: '16',
                    fontWeight: 'bold'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '16',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: dataGraphic
            }
        ]
    };

    return (
        <div className='donut'>
            <ReactECharts
                option={options}
                style={{
                    width: "116px",
                    height: "116px"
                }}
                opts={{ renderer: 'svg' }}
            />
            <div className='w-50 d-flex flex-column justify-content-center align-items-center'>
                <span className='porcentagem'>{formatAsPercent(comConsulta)}</span>
                <span className='nomeGrafico'>{data[0]}</span>
            </div>
        </div>
    )
}

export interface TPieData {
    value: number,
    name: string
}
export class TDonutChart {
    constructor(public nome: string, public dataGraphic: TPieData[], public colorActive: string = '#5cd2c8') {
        this.nome = nome;
        this.dataGraphic = dataGraphic;
        this.colorActive = colorActive;
    }
}
export function DonutChart({ dataGraphic, nome, colorActive }: TDonutChart) {
    const total = dataGraphic[0].value + dataGraphic[1].value;
    const ativo = (dataGraphic[0].value / total) * 100;


    const options = {
        color: ['#09406a', '#63a0b2', '#81bfc9', '#276082', '#45809a', '#9fdfe1', '#bdfff9'],
        tooltip: {
            trigger: "item",
            formatter: "{b0}: {c0}({d}%)"
        },
        series: [
            {
                name: nome,
                type: 'pie',
                radius: ['35%', '70%'],
                center: ['50%', '50%'],
                avoidLabelOverlap: false,
                label: {
                    show: true,
                    overflow: 'break',
                    fontSize: '14',
                    width: 120,
                    formatter: '{a|{b}} \n {b|{c} ({d}%)}',
                    rich: {
                        a: {
                            color: '#6E7079',
                            fontWeight: 'bold',
                            fontSize: 14,
                            align: 'center',
                            overflow: 'breakAll',
                            padding: [3, 10, 10, 5],
                            lineHeight: 20,
                        },
                        b: {
                            color: '#6E7079',
                            fontWeight: 'bold',
                            fontSize: 25,
                            align: 'center'
                        },
                    }
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '16',
                        fontWeight: 'bold',

                    }
                },
                labelLine: {
                    show: false
                },
                data: dataGraphic
            }
        ]
    };

    return (
        <div className='donut'>
            <ReactECharts
                option={options}
                style={{
                    width: "90vw",
                    minWidth: "316px",
                    height: '50vh'
                }}
                opts={{ renderer: 'svg' }}
            />
            <div className='w-50 d-flex flex-column justify-content-center align-items-center'>
                {/* <span className='porcentagem'>{formatAsPercent(ativo.toString())}</span> */}
                {/* <span className='nomeGrafico'>{data[0]}</span> */}
            </div>
        </div>
    )
}
