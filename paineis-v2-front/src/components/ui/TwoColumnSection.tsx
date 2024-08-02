const TwoColumnSection = ({
  children,
}: {
  children: Array<React.ReactElement>;
}) => (
  <div className="container-fluid">
    <div
      className="row gx-5"
      style={{ justifyContent: "center", padding: "50px 0" }}
    >
      {children[0] && <div className="col-12 col-lg-5">{children[0]}</div>}
      {children[1] && <div className="col-12 col-lg-5">{children[1]}</div>}
    </div>
  </div>
);

TwoColumnSection.Col = ({
  children,
}: {
  children: Array<React.ReactElement> | React.ReactElement;
}) => (
  <div style={{ display: "flex", flexDirection: "column", gap: "40px" }}>
    {children}
  </div>
);

export default TwoColumnSection;
