# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.


# Estou testando set com objetos de uma classe
# Isso será útil para minha geração de dungeons e mapas procedurais
class Hex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Hex:{str(self.x)}-{str(self.y)}"


hex1 = Hex(0, 0)
hex2 = Hex(1, 2)
hex3 = Hex(2, 1)

hex4 = Hex(3, 6)
hex5 = Hex(10, 2)
hex6 = Hex(3, 6)

#####################################################################
# Aula 126 - Introdução ao tipo set (conjuntos)
#####################################################################
# s1 = set()  # vazio
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = {"Luiz", 1, 2, 3}  # com dados

# print(s1, type(s1))


#####################################################################
# Aula 127 - Peculiaridades do tipo mutável set
#####################################################################
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# s1 = {1, 2, 3}
# print(4 in s1)

#####################################################################
# Aula 128 - Métodos úteis do tipo set
#####################################################################
# add, update, clear, discard

# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add(3)
# s1.add(5)

# s1.update((4, 6))

# print(s1)

# s1.discard(3)

# print(s1)

# s1.clear()
# print(s1)

#####################################################################
# Aula 129 - Operadores úteis do tipo set
#####################################################################
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# union
# s3 = s1 | s2

# intersection
# s3 = s1 & s2

# difference
# s3 = s1 - s2

# simetric difference
s3 = s1 ^ s2

print(s3)

#####################################################################
# Meus testes com classes e objetos
#####################################################################
# s2 = set()
# s2.add(hex1)
# s2.add(hex2)
# s2.add(hex3)
# print(s2)
