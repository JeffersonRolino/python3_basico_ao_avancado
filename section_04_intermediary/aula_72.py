# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar


def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total


value_1 = multiply(3, 5, 10)
print(value_1)


def is_odd_or_even(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    return f"The number {number} is odd."


number = is_odd_or_even(7)
print(number)
