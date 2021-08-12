def abbreviate(words):
    acronym = []
    for letter in words.replace("'", "").title():
        if letter.istitle():
            acronym.append(letter)
    return ''.join(acronym)
