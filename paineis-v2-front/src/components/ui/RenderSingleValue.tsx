import { Typography } from "./Typography";
import People from "../../assets/images/people.svg";
import Medkit from "../../assets/images/medkit.png";
import Paper from "../../assets/images/paper.png";
import PaperDark from "../../assets/images/paperdark.png";

const IconOptions = {
  people: People,
  medkit: Medkit,
  paper: Paper,
  paperdark: PaperDark,
};

const RenderSingleValue = ({
  title,
  value,
  icon,
}: {
  title: string;
  value: string;
  icon: keyof typeof IconOptions;
}) => {
  return (
    <div>
      <Typography.Details style={{ fontSize: "14px" }}>
        {title}
      </Typography.Details>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "center",
          marginTop: "20px",
        }}
      >
        <img
          src={IconOptions[icon]}
          alt="Total de atendimento nos últimos 12 meses"
          width={"30px"}
        />
        <Typography.Details
          style={{
            width: "initial",
            display: "inline-block",
            fontSize: "26px",
            paddingLeft: "10px",
          }}
        >
          {value || "..."}
        </Typography.Details>
      </div>
    </div>
  );
};

export default RenderSingleValue;
