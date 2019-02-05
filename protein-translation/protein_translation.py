def proteins(strand):
    strand = list(strand)
    codons = list()
    sequence = list()
    stop = ["UAA", "UAG", "UGA"]
    translated = set()

    while len(strand) > 0:
        # adiciona a codons os primeiros 3 itens de strand
        codons.append(strand[:3])
        strand = strand[3:]  # remove da lista os primeiros 3 itens

    for base in codons:  # para cada lista na lista codons
        base = "".join(map(str, base))  # transforma base em uma string
        sequence.append(base)  # adiciona a nova string à lista 'sequence'

    # sequence --> ['AUG', 'UUU', 'UCU', 'UAA', 'AUG']

    aminoacids = {
        "Methionine": ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
    }

    for key, value in aminoacids.items():
        for v in value:
            for s in sequence:
                for st in stop:
                    if s == v:
                        translated.add(key)
                    elif st == s:
                        break
    return print(translated)


proteins("AUGUUUUCUUAAAUG")
# proteins("AUGUUUUCU")
