import ReactECharts from "echarts-for-react";
import "./style.scss";

type ResultType = {
  [key: string]: any;
};

type TStackDataValues = {
  name: string;
  type: string;
  color: string;
  data: number[];
};
type TStackData = {
  labels: string[];
  data: TStackDataValues[];
  setRangeData: (srgs: string[]) => void;
};

type TareaStyle = {
  color: string;
  opacity: number;
};

export function StackedArea(props: TStackData) {
  const { labels, data: items } = props;

  const series: {
    name: string;
    type: string;
    stack: string;
    areaStyle: TareaStyle;
    lineStyle: TareaStyle;
    itemStyle: TareaStyle;
    emphasis: any;
    data: number[];
  }[] = [];
  const legends: string[] = [];
  items.forEach((item: TStackDataValues) => {
    legends.push(item.name);
    series.push({
      name: item.name,
      type: "line",
      stack: "Total",
      areaStyle: {
        opacity: 0.8,
        color: item.color,
      },
      lineStyle: {
        opacity: 1,
        color: item.color,
      },
      itemStyle: {
        opacity: 1,
        color: item.color,
      },
      emphasis: {
        focus: "series",
      },
      data: item.data,
    });
  });

  const options = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
        label: {},
      },
    },
    legend: {
      data: legends,
      icon: "rect",
    },
    toolbox: {
      feature: {
        saveAsImage: {},
      },
    },
    dataZoom: [
      {
        show: true,
        realtime: false,
        start: 30,
        end: 70,
        height: 50,
        bottom: 10,
        xAxisIndex: [0, 1],
      },
      {
        height: 40,
        type: "inside",
        realtime: false,
        start: 30,
        end: 70,
        bottom: 80,
        xAxisIndex: [0, 1],
      },
    ],
    grid: {
      left: "3%",
      right: "4%",
      bottom: 100,
      containLabel: true,
    },
    xAxis: [
      {
        type: "category",
        boundaryGap: false,
        data: labels,
      },
    ],
    yAxis: [
      {
        type: "value",
      },
    ],
    series: series,
  };
  let echartRef: any = null;
  let timer: any = null;
  const onEvents = {
    // 'click': (params: any)=> {console.log(params)},
    datazoom: (params: any) => {
      let starttime: string = `0`;
      let endtime: string = `0`;
      try {
        const isntance = echartRef.getEchartsInstance();
        const axis = isntance.getOption().xAxis[0];
        const { startValue, endValue } = isntance.getOption().dataZoom[0];
        starttime = axis.data[startValue];
        endtime = axis.data[endValue];
      } catch (e) {
        starttime = "0";
        endtime = "0";
      }
      clearTimeout(timer);
      // armazenamos o timer novamente
      timer = setTimeout(function () {
        if (
          sessionStorage.getItem("starttime") == starttime &&
          sessionStorage.getItem("endtime") == endtime
        ) {
          starttime = "0";
          endtime = "0";
        }
        sessionStorage.setItem("starttime", starttime.toString());
        sessionStorage.setItem("endtime", endtime.toString());
        props.setRangeData([starttime, endtime]);
      }, 500);
    },
  };
  return (
    <div className="stack">
      <ReactECharts
        option={options}
        ref={(e) => {
          echartRef = e;
        }}
        style={{
          minWidth: "100%",
          width: "200px",
          height: "400px",
        }}
        opts={{ renderer: "svg" }}
        onEvents={onEvents}
      />
    </div>
  );
}
