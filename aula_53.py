""" 
enumerate - enumera iteráveis (índices)

"""

lista = ["Tony Stark", "Steve Rogers", "Bruce Banner"]

lista.append("Peter Parker")

# lista_enumerada = enumerate(lista)
# print(lista_enumerada)

# pior forma
# for index, item in lista_enumerada:
#     print(index, item)

lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

# forma manual
for item in enumerate(lista):
    indice, valor = item
    print(indice, valor)

print("\n")

# melhor forma
for index, item in enumerate(lista):
    print(index, item)
