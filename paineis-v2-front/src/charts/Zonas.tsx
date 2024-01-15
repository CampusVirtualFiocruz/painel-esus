import { useRef } from "react";
import ReactECharts from 'echarts-for-react';

export function Zonas({ data }: any) {
    const inputEl = useRef(null);
    let nome = 'Zonas Urbana/Rural';
    let dados = [
        { value: data?.urbano ?? 0, name: 'Zona Urbana' },
        { value: data?.rural ?? 0, name: 'Zona Rural' }
    ];

    function onChartClick(params: any) {
        return;
    }

    const options = {
        color: ['#2775b0', '#78b4d0'],
        series: [
            {
                name: nome,
                type: 'pie',
                radius: ['30', '52'],
                avoidLabelOverlap: false,
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '12',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: dados
            }
        ]
    };

    return (
        <>
            <ReactECharts
                ref={inputEl}
                option={options}
                style={{
                    width: "116px",
                    height: "116px"
                }}
                opts={{ renderer: 'svg' }}
                onEvents={{ 'click': onChartClick }}
            />
        </>
    )
}
