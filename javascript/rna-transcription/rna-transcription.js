const Dna2Rna = {
  G: "C",
  C: "G",
  T: "A",
  A: "U",
};

export const toRna = (nucleotidesArray) => {
  let result = "";
  for (let i = 0; i < nucleotidesArray.length; i++) {
    result += Dna2Rna[nucleotidesArray[i]];
  }
  return result;
};
