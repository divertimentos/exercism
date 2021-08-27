const nucleotides = {
  G: "C",
  C: "G",
  T: "A",
  A: "U",
};

export const toRna = (string) => {
  return string.replace(/[GCTA]/g, (matched) => nucleotides[matched]);
};
