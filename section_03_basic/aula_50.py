"""
Exercício
Exiba os índices da lista

0 Maria
1 Helena
2 Luiz

"""
lista = ["Maria", "Helena", "Luiz"]
lista.append("João")
lista.append("José")

indices = range(len(lista))

for indice in indices:
    print(f"{indice}: {lista[indice]}")
