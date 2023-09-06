"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# #        +01234
# #        -54321
# string = "ABCDE"  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

# #        0    1      2              3    4
# #       -5   -4     -3             -2   -1
# lista = [123, True, "Luiz Otávio", 1.2, []]
# lista[-3] = "Maria"
# print(lista)
# print(lista[2], type(lista[2]))

lista = [10, 20, 30, 40, 50, 60]

##################################
# Adicionando Items na Lista
##################################

# print(lista)

# ultimo_valor = lista.pop()
# print(ultimo_valor)


# lista.append(70)
# lista.append(80)
# lista.append(90)

###################################
# Removendo Items da Lista
###################################

# Removendo Item especifico
# del lista[2]
# print(lista)

# Removendo Item especifico com pop()

# ultimo_valor = lista.pop()
# print(ultimo_valor)
# print(lista)

# Removendo Item especifico com pop()

# valor_especifico = lista.pop(3)
# print(valor_especifico)
# print(lista)


# Deletando o último valor com del -1
# del lista[-1]
# print(lista)

# Limpando a lista
# lista.clear()
# print(lista)

# Inserindo Item no Índice específico

# lista.insert(0, 5)
# print(lista)


###################################
# Concatenando Listas
###################################

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")

lista_c = lista_a + lista_b
print(f"Lista C: {lista_c}")

lista_a.extend(lista_b)
print(f"Lista A extendida com extend(): {lista_a}")
