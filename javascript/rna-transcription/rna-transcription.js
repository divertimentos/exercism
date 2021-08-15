const transcriptionRules = {
  G: "C",
  C: "G",
  T: "A",
  A: "U",
};

export const toRna = (nucleotidesArray) => {
  return nucleotidesArray
    .split("")
    .map((nucleotide) => transcriptionRules[nucleotide])
    .join("");
};
