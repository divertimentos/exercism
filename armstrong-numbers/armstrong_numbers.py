def is_armstrong(number):
    numbers_list = [int(x) for x in str(number)]
    length = len(numbers_list)
    powered_numbers = list()

    for digit in numbers_list:
        powered_numbers.append(digit**length)

    result = sum(powered_numbers)
    if result == number:
        print(f"{number} é um número de Armstrong!")
        return True
    else:
        print(f"{number} não é um número de Armstrong!")
        return False
