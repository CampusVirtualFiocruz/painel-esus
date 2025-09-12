import { HTMLProps } from 'react';

const Card = ({
  children,
  ...props
}: { children: React.ReactElement } & HTMLProps<HTMLDivElement>) => {
  return (
    <div
      {...props}
      style={{
        borderRadius: '4px',
        border: '1px solid rgb(211, 212, 221)',
        padding: '1.2rem',
        width: '100%',
        ...props?.style,
      }}
    >
      {children}
    </div>
  );
};

export default Card;
