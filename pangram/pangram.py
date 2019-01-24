import string


def is_pangram(*sentences):
    for sentence in sentences:

        if len(sentence) == 0:  # se sentence for vazia
            return False

        not_in_sentence = list()
        for letter in string.ascii_lowercase:
            # se uma letra do alfabeto não estiver na sentença:
            if letter not in sentence.lower():
                not_in_sentence.append(letter)  # adiciona a letra à lista

        if len(not_in_sentence) == 0:  # se não houver letra de fora do alfabeto
            print("It's a pangram!")
            return True
        else:
            print("It's not a pangram")
            return False
