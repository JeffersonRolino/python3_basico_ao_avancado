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


pessoa = {}

##
##

# pessoa["nome"] = "Jefferson"
# print(pessoa)
# print(pessoa["nome"])

# Chaves dinâmicas

key = "nome"
pessoa["sobrenome"] = "Miranda "
pessoa[key] = "José"

# del pessoa["sobrenome"]

print(pessoa)

print(pessoa[key])
print(pessoa["nome"])

# print(pessoa["sobrenome"])

# If não param exceções
# if pessoa["sobrenome"]:
#     print("Existe")

# print("Esse código não será acessado devido exceção")

# Usando o get
if pessoa.get("sobrenome") is not None:
    print(pessoa["sobrenome"])
else:
    print("Chave não existe")
