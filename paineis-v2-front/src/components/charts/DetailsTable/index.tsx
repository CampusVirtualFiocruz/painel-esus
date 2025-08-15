import { content } from "../../../assets/content/content";

const DetailsTable = ({ ...props }) => {
  if (!props || !props.data || props.data.length === 0) {
    return <div>Nenhuma informação disponível</div>;
  }

  const foundColumns = props.data.reduce((acc: any, item: any) => {
    if (item) {
      const newSet = new Set(acc);
      Object.keys(item?.value).forEach((key) => {
        newSet.add(key);
      });
      return newSet;
    }
    return acc;
  }, new Set());

  return (
    <div>
      <div className="painel-lateral details-table">
        <div style={{ display: "flex", paddingTop: "30px" }}>
          <div style={{ flex: "150px" }}>
            <div className="tipo p-2 "></div>
          </div>
          {Array.from(foundColumns).map((item: any) => (
            <div style={{ flex: 1 }}>
              <div className="coluna p-2 text-center ">{content?.[ item] || item}</div>
            </div>
          ))}
        </div>
        {props.data.map((item: any, index: any) => (
          <div key={index}>
            <div
              key={index}
              style={{
                display: "flex",
                gap: "14px",
                marginBottom: "10px",
              }}
            >
              <div style={{ flex: "150px" }}>
                <div className="tipo p-2 bordas">{content?.[ item?.tag] || item?.tag}</div>
              </div>
              {Array.from(foundColumns).map((colName: any) => (
                <div style={{ flex: 1 }}>
                  <div className="coluna p-2 text-center bordas">
                    {item?.value?.[colName]}
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DetailsTable;
