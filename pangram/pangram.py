import string

def is_pangram(*sentences):
    for sentence in sentences:
        if sentence == "":  # sentence_empty
            return False
        
        
        else:  # Se sentence não for vazia
            for char in sentence:
                if "x" not in sentence:  # missing_character_x
                    return False

                if char not in string.ascii_letters:  # another_missing_character
                    return False  # Não é um pangram

                else: # É um pangram
                    if sentence.islower():  # perfect_lower_case_pangram
                        return True
                    
                    if string.punctuation in sentence:
                        return True

is_pangram()
is_pangram('abcdefghijklmnopqrstuvwxyz')