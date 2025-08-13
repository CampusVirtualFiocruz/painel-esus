import { Waffle as Nivo } from "@nivo/waffle";
import { memo } from "react";
import { FaUser } from "react-icons/fa";
import { content } from "../../../assets/content/content";
import { formatAsPercent } from "../../../utils";
import { DonutChart } from "../charts.types";

const colors = [
   "#0B5B98",
   "#0A406A",
   "#49E8DB",
   "#6595FF",
   "#0B5B98",
   "#D3D4DD",
]

const Waffle = (props: DonutChart) => {
  let waffleData = props.data.reduce(
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

  if(props?.config?.sort){
    const suggestionOrder = props?.config?.sort;
    const sortedDataList = waffleData?.sort((a: any, b: any) => {
      return (
        suggestionOrder?.findIndex((s: any) => s === a?.label) -
        suggestionOrder?.findIndex((s: any) => s === b?.label)
      );
    });
    waffleData = sortedDataList;
  }

  const total = waffleData.reduce(
    (prev, curr: { value: number }) => (curr?.value ?? 0) + prev,
    0
  );

  const cloneWaffleInfo:any = JSON.parse(JSON.stringify(waffleData));

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", ...(props?.config?.componentStyle || {}) }}>
      <Nivo
        width={600}
        height={300}
        data={cloneWaffleInfo}
        total={total}
        rows={10}
        columns={20}
        padding={2}
        colors={colors}
        borderRadius={0}
        borderColor={"#ffffff"}
        motionStagger={2}
        fillDirection="bottom"
        emptyColor={"#ffffff"}
      />
      <div
        style={{
          width: "100%",
          display: "flex",
          height: "30px",
          marginTop: "40px",
        }}
      >
        {cloneWaffleInfo.map(({ id, label, value }: any, dataIndex: any) => (
          <div key={id} style={{ width: "100%", textAlign: "center" }}>
            <div
              style={{
                width: "100%",
                display: "flex",
                justifyContent: "center",
              }}
            >
              <FaUser size="26px" color={colors?.[dataIndex]} />
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
