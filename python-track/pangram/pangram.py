import string


def is_pangram(*sentences):
    for sentence in sentences:

        if len(sentence) == 0:
            return False
        else:
            not_in_sentence = list()
            for letter in string.ascii_lowercase:
                if letter not in sentence.lower():
                    not_in_sentence.append(letter)

            if len(not_in_sentence) == 0:
                print("It's a pangram!")
                return True
            else:
                print("It's not a pangram")
                return False
