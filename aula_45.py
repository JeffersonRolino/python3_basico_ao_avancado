"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# nome = "Jefferson"
# numeros = range(0, -10, -1)


# for numero in numeros:
#     print(numero)


nome = "José"  # iterável
iterador = iter(nome)  # iterador // O método iter() chama o __iter__()
# iterador = nome.__iter__() # iterador
# print(iterador.__next__())


# For por baixo dos panos
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# Mesma coisa
for letra in nome:
    print(letra)
