def proteins(strand):
    strand = list(strand)
    codons = list()
    sequence = list()
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

    stop = ["UAA", "UAG", "UGA"]
    

    # print(sequence)

    for key, value in aminoacids.items():
        for i in value:
            if i in sequence:
                print(key)
    

    # for stop_condition in stop:
    #     for key, value in aminoacids.items():
    #         for i in value:
    #             for s in sequence:
    #                 if stop_condition == s:
    #                     print("irá parar")
    #                     break
    #                 if s in i:
    #                     print(key)




    # for key, value in aminoacids.items():
    #     for i in value:
    #         for s in sequence:
    #             if aminoacids.get("STOP") == s:
    #                 print("teste")

                # if i in s:
                #     print(key)
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
