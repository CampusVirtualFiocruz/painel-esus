const Subtitle = ({ children }: { children: string }) => {
  return (
    <center style={{ marginTop: "3rem" }}>
      <h4>
        <b>{children}</b>
      </h4>
    </center>
  );
};

const Typography = { Subtitle };

export { Typography };
