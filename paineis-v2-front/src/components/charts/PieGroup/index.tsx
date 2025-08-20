import { content } from "../../../assets/content/content";
import { formatAsPercent } from "../../../utils";
import { Typography } from "../../ui/Typography";
import { Pie } from "../Pie";
import "./style.scss";

const defaultConfig = {
  formatterKind: "perc",
  colors: ["#0069d0", "#84aaff", "#818181"],
  componentStyle: {
    width: "100px",
    minWidth: "100px",
    height: "100px",
  },
  chartConfigOverride: {
    legend: {
      show: false,
    },
  },
  seriesConfigOverride: {
    labelLine: {
      show: false,
    },
    label: {
      show: false,
    },
    emphasis: {
      show: false,
    },
  },
};

export function PieGroup(props: any) {
  return (
    <div>
      <div style={{ display: "flex", flexDirection: "row", gap: "10px" }}>
        {props.data?.map((item: any, index: any) => {
          return (
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                gap: "10px",
                justifyContent: "start",
                alignItems: "center",
              }}
            >
              <Pie
                data={item?.data}
                config={{ ...defaultConfig, ...props.config }}
                key={index}
              />
              <Typography.Details style={{ fontSize: "26px" }}>
                {formatAsPercent(String(Number(item?.value as any) * 100))}
              </Typography.Details>
              <Typography.Details
                style={{ fontSize: "20px", fontWeight: "100" }}
              >
                {content?.[item?.tag] || item?.tag}
              </Typography.Details>
            </div>
          );
        })}
      </div>
    </div>
  );
}
