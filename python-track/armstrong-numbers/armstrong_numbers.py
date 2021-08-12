def is_armstrong(number):
    
    # Creates a list which contains the 'number' digits:
    numbers_list = [int(x) for x in str(number)]
    
    
    length = len(numbers_list)
    raised_numbers = list()

    
    # Puts each 'numbers_list' digit, raised, in a list:
    for digit in numbers_list:
        raised_numbers.append(digit**length)

    # Sums each raised digit:
    result = sum(raised_numbers)
    
    # Tests if the result is an Armstrong number:
    if result == number:
        print(f"{number} é um número de Armstrong!")
        return True
    else:
        print(f"{number} não é um número de Armstrong!")
        return False
