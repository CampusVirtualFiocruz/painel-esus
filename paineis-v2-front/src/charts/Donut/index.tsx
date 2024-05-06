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

export interface TPieData{
    value: number,
    name: string
}
export class TDonutChart{
    constructor(public nome:string, public dataGraphic: TPieData[], public colorActive: string = '#5cd2c8'){
        this.nome = nome;
        this.dataGraphic = dataGraphic;
        this.colorActive = colorActive;
    }
}
export function DonutChart({dataGraphic, nome, colorActive}: TDonutChart) {
    const total = dataGraphic[0].value + dataGraphic[1].value;
    const ativo = (dataGraphic[0].value / total)*100;
    

    const options = {
        color: [colorActive,'#09406a'],
        tooltip: {
            trigger: "item",
            formatter: "{b0}: {c0}({d}%)"
        },
        series: [
            {
                name: nome,
                type: 'pie',
                radius: ['60%', '90%'],
                avoidLabelOverlap: false,
                label: {
                    show: true,
                    overflow: 'break',
                    fontSize: '16',
                    fontWeight: 'bold',
                    width: 110
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
                    width: "100%",
                    minWidth: "316px",
                    height: '216px'
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
