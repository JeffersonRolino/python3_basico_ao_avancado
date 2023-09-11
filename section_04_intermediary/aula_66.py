"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    print(f"{x=} {y=} {z=} | x + y + z = {x + y + z}")


soma(2, 1, 5)
soma(y=2, x=1, z=5)
