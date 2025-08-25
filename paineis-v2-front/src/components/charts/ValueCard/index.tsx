import { ValueChart } from "../charts.types";
import Card from "../../ui/Card";
import RenderSingleValue from "../../ui/RenderSingleValue";
import "./style.scss";
import { content } from "../../../assets/content/content";
import { useMemo } from "react";
import { getChartDescription } from "../../../utils/chartTitleUtils";

export function ValueCard(props: ValueChart) {
  
  const desc = useMemo(() => 
    getChartDescription(props.config?.description, props.config?.reportViewType, content),
    [props.config?.description, props.config?.reportViewType]
  );
  
  return (
    <>
    <div style={{ display: "flex", flexDirection: "row", gap: "10px", width: "100%", position: "relative" }}>
    <Card style={{ flex: 1 }}>
      <RenderSingleValue
        icon={String(props?.config?.icon) as any}
        title={desc}
        value={Number(
          props.data
        )?.toLocaleString("pt-BR") + (props.config?.percent ? "%" : "")}
      />
    </Card>
    {props.config?.info && <span
        style={{
          position: "absolute",
          bottom: "-20px",
          right: "0",
          fontSize: "14px"
        }}>
          * {props.config?.info}
      </span>}
  </div>
    </>
  );
}
