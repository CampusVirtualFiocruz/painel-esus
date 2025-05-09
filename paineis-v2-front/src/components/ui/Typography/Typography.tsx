import { HTMLProps } from "react";

const Subtitle = ({
  children,
  ...props
}: { children: any } & HTMLProps<HTMLDivElement>) => (
  <h5
    {...props}
    style={{
      width: "100%",
      textAlign: "center",
      padding: 0,
      margin: 0,
      ...props?.style,
    }}
  >
    <b>{children}</b>
  </h5>
);

const Details = ({
  children,
  ...props
}: { children: any } & HTMLProps<HTMLDivElement>) => (
  <h6
    {...props}
    style={{
      width: "100%",
      textAlign: "center",
      padding: 0,
      margin: 0,
      ...props?.style,
    }}
  >
    <b>{children}</b>
  </h6>
);

const Typography = { Subtitle, Details };

export { Typography };
