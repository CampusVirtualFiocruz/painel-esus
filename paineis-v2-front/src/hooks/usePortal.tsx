import React from "react";

const usePortal = (el: any) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null,
  });

  const createPortal = React.useCallback((el: any) => {
    const Portal = ({ children }: any) => ReactDOM.createPortal(children, el);

    const remove = () => ReactDOM.unmountComponentAtNode(el);

    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) {
      portal.remove();
    }
    const newPortal: any = createPortal(el);
    setPortal(newPortal);

    return () => {
      newPortal.remove(el);
    };
  }, [el]);

  return portal.render;
};

export default usePortal;
