"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-se de desempacotamento
# x, y, *resto = 1, 2, 3, 4, 5
# print(x, y, resto)


# def soma(x, y):
#     return x + y


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


# valor_1 = soma(1, 2, 3, 4, 5, 6)
# print(valor_1)

# valor_2 = soma(1, 3, 4, 78, 29, 20, 15)
# print(valor_2)


numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
outra_soma = soma(*numeros)

print(outra_soma)

# print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9)))
