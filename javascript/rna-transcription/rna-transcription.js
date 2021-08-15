export const toRna = (nucleotides) => {
  const transcriptionSchema = {
    G: "C",
    C: "G",
    T: "A",
    A: "U",
  };

  const result = nucleotides
    .split("")
    .map((item) => transcriptionSchema[item])
    .join("");
  return result;
};
