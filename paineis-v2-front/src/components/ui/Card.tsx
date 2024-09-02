const Card = ({ children }: { children: React.ReactElement }) => {
  return (
    <div
      style={{
        borderRadius: "4px",
        border: "1px solid rgb(211, 212, 221)",
        padding: "1.5rem",
        width: "100%",
      }}
    >
      {children}
    </div>
  );
};

export default Card;
