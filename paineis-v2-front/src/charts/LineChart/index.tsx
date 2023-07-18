import ReactECharts from 'echarts-for-react'
import { formatAsPercent } from '../../utils'
import './style.scss';

type ResultType = {
    [key: string]: any
};

type TStackDataValues = {
    name: string;
    type: string;
    color: string;
    data: number[]
};
type TStackData = {
    labels: string[];
    data: TStackDataValues[],
    setRangeData: (srgs: string[]) => void
}

type TareaStyle = {
    color: string;
    opacity: number;
};

export function LineChart(props: TStackData) {
    const { labels, data: items } = props;
    const series: {
        name: string,
        type: string,
        stack: string,
        data: number[]
    }[] = []
    const legends: string[] = [];
    items.forEach((item: TStackDataValues) => {
        legends.push(item.name)


        series.push({
            name: item.name,
            type: 'line',
            stack: 'Total',
            data: item.data
        });
    })
    const options = {
        title: {
            text: ''
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: legends,
            bottom: 5
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '10%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: labels
        },
        yAxis: {
            type: 'value'
        },
        series: series
    };
    let echartRef: any = null;
    return (
        <div className='stack'>
            <ReactECharts
                option={options}
                ref={(e) => { echartRef = e; }}
                style={{
                    minWidth: "200px",
                    width: "100%",
                    height: "400px"
                }}
                opts={{ renderer: 'svg' }}
            />
        </div>
    );
}