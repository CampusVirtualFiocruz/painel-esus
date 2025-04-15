import { Waffle as Nivo } from "@nivo/waffle";
import { memo } from "react";
import { DonutChart } from "../charts.types";
import { content } from "../../../assets/content/content";
import { FaUser } from "react-icons/fa";
import { formatAsPercent } from "../../../utils";

const colors = [
  "#0B5B98",
  "#0A406A",
  "#49E8DB",
  "#6595FF",
  "#0B5B98",
  "#D3D4DD",
];

const Waffle = (props: DonutChart) => {
  const data = props.data.reduce(
    (prev, curr) =>
      [
        ...prev,
        {
          id: curr?.tag,
          value: curr?.value ?? 0,
          label: content?.[curr?.tag] || curr?.tag,
        } as any,
      ] as any,
    []
  );

  const total = data.reduce(
    (prev, curr: { value: number }) => (curr?.value ?? 0) + prev,
    0
  );

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto" }}>
      <Nivo
        width={600}
        height={300}
        data={data}
        total={total}
        rows={10}
        columns={20}
        padding={2}
        colors={colors}
        borderRadius={0}
        borderColor={"#ffffff"}
        motionStagger={2}
      />
      <div
        style={{
          width: "100%",
          display: "flex",
          height: "30px",
          marginTop: "40px",
        }}
      >
        {data.map(({ id, label, value }, dataIndex) => (
          <div key={id} style={{ width: "100%", textAlign: "center" }}>
            <div
              style={{
                width: "100%",
                display: "flex",
                justifyContent: "center",
              }}
            >
              <FaUser size="26px" color={colors?.[dataIndex % data?.length]} />
            </div>
            <h4 style={{ paddingTop: "8px" }}>
              <b>{formatAsPercent(String((value / total) * 100))}</b>
            </h4>
            <span style={{ padding: "4px", fontSize: "16px", paddingTop: 0 }}>
              {label}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default memo(Waffle);
