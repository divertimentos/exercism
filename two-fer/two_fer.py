def two_fer(*names):
    
    if len(names) == 0:  # se chamar a função sem nenhum argumento
        name = "you"
        return f"One for {name}, one for me."
    else:  # Se houver pelo menos um argumento:
        for name in names:  # "*names" é uma lista
            if name == "Alice":
                return f"One for {name}, one for me."
            elif name == "Bob":
                return f"One for {name}, one for me."
            else:
                raise Exception("Nome inválido")
two_fer()
two_fer("Alice")
two_fer("Bob")
# two_fer("Chris")