# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# print(pessoa, type(pessoa))

# pessoa_1 = {"nome": "Jefferson"}

# print(pessoa_1, type(pessoa))


# location = dict()

# location["name"] = "Fernando de Noronha"
# location["country"] = "Brasil"

# print(location)

# pessoa = {
#     "nome": "Luiz Otávio",
#     "sobrenome": "Miranda",
#     "idade": 18,
#     "altura": 1.8,
#     "endereços": [
#         {"rua": "tal tal", "número": 123},
#         {"rua": "outra rua", "número": 321},
#     ],
# }

# # print(pessoa["nome"])

# for key in pessoa:
#     print(f"{key}: {pessoa[key]}")


# pessoa = {}

##
##

# pessoa["nome"] = "Jefferson"
# print(pessoa)
# print(pessoa["nome"])

# Chaves dinâmicas

# key = "nome"
# pessoa["sobrenome"] = "Miranda "
# pessoa[key] = "José"

# del pessoa["sobrenome"]

# print(pessoa)

# print(pessoa[key])
# print(pessoa["nome"])

# print(pessoa["sobrenome"])

# If não param exceções
# if pessoa["sobrenome"]:
#     print("Existe")

# print("Esse código não será acessado devido exceção")

# Usando o get
# if pessoa.get("sobrenome") is not None:
#     print(pessoa["sobrenome"])
# else:
#     print("Chave não existe")


# Dicionários só usam o último valor
# pessoa_2 = {
#     "nome": "Luiz Otávio",
#     "sobrenome": "Miranda",
#     "sobrenome": "Miranda",
#     "sobrenome": "Miranda",
# }

# print(len(pessoa_2))

# pessoa = {"nome": "Jefferson", "sobrenome": "Rolino", "idade": 45}


# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())

# print(list(pessoa.keys()))

# for key in pessoa.keys():
#     print(key)


# for value in pessoa.values():
#     print(value)

# for key, value in pessoa.items():
#     print(key, value)

# pessoa.setdefault("idade", None)

# for key, value in pessoa.items():
#     print(key, value)

# import copy

# d1 = {"c1": 1, "c2": 2, "l1": [0, 1, 2]}

# # cópia rasa / shallow copy
# d2 = d1.copy()

# # cópia profunda / deep copy
# d3 = copy.deepcopy(d2)

# d2["c1"] = 1000
# d2["c2"] = "abc"
# d2["l1"][0] = 42

# d3["c1"] = 78
# d3["l1"][1] = 789

# print(d1)
# print(d2)
# print(d3)

p1 = {"nome": "Luiz", "sobrenome": "Miranda"}

# # Metódo Get
# p2 = {
#     # "nome": "Luiz",
#     "sobrenome": "Miranda"
# }

# print(p2.get("nome", "Nome não existe"))

# nome = p1.pop("nome")
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({"nome": "novo valor", "idade": 30})
# print(p1)


# p1.update(nome="novo valor", idade=30)
# print(p1)

# tupla = (("nome", "novo valor"), ("idade", 30))
lista = [["nome", "novo valor"], ["idade", 30]]
p1.update(lista)
print(p1)
