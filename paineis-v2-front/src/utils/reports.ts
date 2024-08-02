export const randomHexColorCode = () => {
  let n = (Math.random() * 0x361949 * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};

export const wait = (milliseconds: number) => {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
};
