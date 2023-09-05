"""
Iterando strings com while
"""

nome = "Jefferson"  # Iteráveis

index = 0
nova_string = ""
while index < len(nome):
    letra = nome[index]
    nova_string += f"*{letra}"
    index += 1

nova_string += "*"
print(nova_string)
