"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro...
"""


def criar_multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadruplicar = criar_multiplicacao(4)

resultado_1 = duplicar(3)
resultado_2 = triplicar(3)
resultado_3 = quadruplicar(3)

print(resultado_1, resultado_2, resultado_3)
