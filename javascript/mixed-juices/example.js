const limes = [
  "small",
  "large",
  "large",
  "medium",
  "small",
  "large",
  "large",
  "medium",
];

const limesToCut = (wedgesNeeded, limes) => {
  let wedges = 0;
  while (wedges <= wedgesNeeded) {
    console.log("Wedges:", wedges);
    switch () {
      case "small":
        wedges += 6;

      case "medium":
        wedges += 8;

      case "large":
        wedges += 10;
    }
  }
  return wedges;
};

console.log(limesToCut(25, limes));
