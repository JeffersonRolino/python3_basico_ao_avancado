"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel:>10}.")  # padding para esquerda de 10
print(f"{variavel:<10}.")  # padding para direita de 10
print(f"{variavel:^10}.")  # padding centro de 10

print(f"{1000.2312315453634545:0=+10.1f}")

print(f"O Hexadecimal de 10472 é {10472:08x}")

print(f"{variavel!r}")
