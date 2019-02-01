def proteins(strand):
        strand = list(strand)
        codons = list()
        sequence = list()
        while len(strand) > 0:
                codons.append(strand[:3])  # adiciona a codons os primeiros 3 itens de strand
                strand = strand[3:]  # remove da lista os primeiros 3 itens
        
        for base in codons:  # para cada lista na lista codons
                base = "".join(map(str, base))  # transforma base em uma string
                sequence.append(base)  # adiciona a nova string à lista 'sequence'

        # print(sequence)

        aminoacids = {
                "Methionine": ["AUG"],
                "Phenylalanine": ["UUU", "UUC"],
                "Leucine": ["UUA", "UUG"],
                "Serine": ["UCU", "UCC", "UCA", "UCG"],
                "Cysteine": ["UGU", "UGC"],
                "Tryptophan": ["UGG"],
                "STOP": ["UAA", "UAG", "UGA"],
        }

        

        # print(sequence)
        
        # for s in sequence:
        #         print(type(s))

        # for k, v in aminoacids.items():
        #         print(type(v))

        # for s in sequence:
        #         for k, v in aminoacids.items():
        #                 for i in v:
        #                         if i == s:
        #                                 print(k)
proteins("AUGUUUUCUUAAAUG")
