const Subtitle = ({ children }: { children: string }) => {
  return (
    <div style={{ marginTop: "3rem" }}>
      <h4>
        <b>{children}</b>
      </h4>
    </div>
  );
};

const Typography = { Subtitle };

export { Typography };
