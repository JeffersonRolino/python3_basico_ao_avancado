""" 
Introdução ao desempacotamento
"""

nome1, *resto = ["Maria", "Helena", "Luiz"]

numeros = [1, 2, 3, 4, 5]

# 2
_, numero, *_ = numeros

print(nome1, resto)
print(numero, _)
