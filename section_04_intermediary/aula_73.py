"""
Higher Order Functions
Funções de primeira Classe
"""


def greetings(msg, nome):
    return f"{msg} {nome}"


def execution(function, *args):
    return function(*args)


# greetings_2 = greetings

# print(greetings_2("Good day!"))


print(execution(greetings, "Bom dia", "Jefferson"))

print(execution(greetings, "Boa noite", "Maria"))
