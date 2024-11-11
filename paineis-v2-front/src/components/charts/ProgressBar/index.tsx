import { content } from "../../../assets/content/content";
import { DonutChart } from "../charts.types";
import { Progress } from "reactstrap";
import "./style.scss";
import { randomHexColorCode } from "../../../utils/reports";

const defaultColors = ["#09406a", "#2775b0", "#0069d0", "#84aaff", "#175693", "#78b4d0", "#09406a", "#2775b0", "#0069d0", "#84aaff", "#175693", "#78b4d0","#09406a", "#2775b0", "#0069d0", "#84aaff", "#175693", "#78b4d0"];

export function ProgressBar(props: DonutChart) {

  console.log({props})

  return (
    <div style={{ marginTop: "60px" }}>
      {(props.data || []).map((i, index) => <div key={i.tag} className="d-flex align-items-center mt-2">
                <div className="desfecho d-flex" style={{ borderColor: "#bbbbbb" }}>
                  <span style={{ flex: "1", paddingBottom: "16px", width: "50%" }}>{i.tag}</span>
                  <div style={{ flex: "1" }}>
                  <Progress
                    value={Number(i.value)}
                    barStyle={{
                      backgroundColor:
                      index > defaultColors.length
                          ? randomHexColorCode()
                          : defaultColors[index],
                    }}
                  />
                </div>
                </div>
                <span className="total ms-2 wpercent">{Number(i.value)}%</span>
              </div>)}
    </div>
  );
}
