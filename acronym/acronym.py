def abbreviate(words):
    acronym = list()

    words = words.replace("'", "").title()

    for letter in words:
        if letter.istitle():
            acronym.append(letter)
    words = ''.join(map(str, acronym))
    return words
