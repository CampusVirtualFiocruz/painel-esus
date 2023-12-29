import ReactECharts from 'echarts-for-react'
import { formatAsPercent } from '../../utils'
import './style.scss';

export interface TPieData {
    value: number
}
export class TPieChart {
    constructor(public nome: string, public dataGraphic: TPieData[], public colorActive: string = '#5cd2c8', public bottom = false) {
        this.nome = nome;
        this.dataGraphic = dataGraphic;
        this.colorActive = colorActive;
        this.bottom = bottom

    }
}
export function PieChart({ dataGraphic, nome, colorActive, bottom }: TPieChart) {

    const total = dataGraphic[0].value + dataGraphic[1].value;
    const ativo = (dataGraphic[0].value / total) * 100;

    const options = {
        color: [colorActive, '#e4e4e4'],
        tooltip: {
            trigger: "item",
            formatter: "({d}%)"
        },
        title: {
            text: nome,
            left: 'center',
            top: '0',
            bottom: 'auto',
            padding: 15,
            textStyle: {
                fontSize: 16,
                overflow: 'break',
                width: 200,
            }
        },
        series: [
            {
                name: nome,
                type: "pie",
                radius: "80%",
                center: ["50%", "50%"],
                animationDuration: 5000,
                label: {
                    show: true,
                    position: 'center',
                    fontSize: '16',
                    fontWeight: 'bold'
                },
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: "rgba(0, 0, 0, 0.5)"
                },
                labelLine: {
                    show: false
                },
                data: dataGraphic
            }
        ]
    };
    if (bottom) {
        options.title["top"] = 'auto';
        options.title["bottom"] = '-15';
    }
    return (
        <div className='pie-chart'>
            <ReactECharts
                option={options}
                style={{
                    width: "30vw",
                    minWidth: "316px",
                    height: '30vh'
                }}
                opts={{ renderer: 'svg' }}
            />
            <div className='data-info d-flex flex-column align-items-center'>
                <span className='porcentagem'>{(dataGraphic[0].value) + `(${formatAsPercent(ativo.toString())})`}</span>
            </div>
        </div>
    )
}


export function Pie({ data }: any) {
    let nome = 'obstetrics-factors';
    let comConsulta = data[1].com_consulta;
    let semConsulta = data[1].sem_consulta;
    let limite = data[1]?.limite;

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
                type: "pie",
                radius: "80%",
                center: ["50%", "50%"],
                animationDuration: 5000,
                label: {
                    show: true,
                    position: 'center',
                    fontSize: '16',
                    fontWeight: 'bold'
                },
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: "rgba(0, 0, 0, 0.5)"
                },
                labelLine: {
                    show: false
                },
                data: dataGraphic
            }
        ]
    };

    return (
        <div className='pie'>
            <ReactECharts
                option={options}
                style={{
                    width: "126px",
                    height: "126px"
                }}
                opts={{ renderer: 'svg' }}
            />
            <div className='data-info d-flex flex-column align-items-center'>
                <span className='porcentagem'>{formatAsPercent(comConsulta)}</span>
                <span className='nomeGrafico'>{data[0]}</span>
                <span className='nomeGrafico'>{limite}</span>
            </div>
        </div>
    )
}
