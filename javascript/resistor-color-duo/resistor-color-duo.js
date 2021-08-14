export const decodedValue = (colorArray) => {
  const colors = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
  ];

  return Number(
    colorArray
      .slice(0, 2)
      .map((color) => colors.indexOf(color))
      .join("")
  );
};
