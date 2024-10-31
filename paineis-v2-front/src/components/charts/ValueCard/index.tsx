import { ValueChart } from "../charts.types";
import Card from "../../ui/Card";
import RenderSingleValue from "../../ui/RenderSingleValue";
import "./style.scss";

export function ValueCard(props: ValueChart) {
  return (
    <>
    <div style={{ display: "flex", flexDirection: "row", gap: "10px", width: "100%", position: "relative" }}>
    <Card style={{ flex: 1 }}>
      <RenderSingleValue
        icon={String(props?.config?.icon) as any}
        title={String(props.config?.description)}
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
