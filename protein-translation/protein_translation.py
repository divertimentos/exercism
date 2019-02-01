def proteins(strand):
        strand = list(strand)
        codons = list()
        while len(strand) > 0:
                codon = strand[0:3]
                codons.append(codon)
                strand = strand[3:]
                # print(codons)
        print(codons)        

proteins("AAABBBCCC")
