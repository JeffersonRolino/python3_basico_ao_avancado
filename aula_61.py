"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

user_input = "746.824.890-70"

cpf = ""

for digit in user_input:
    if digit == "." or digit == "-":
        pass
    else:
        cpf += digit

numbers = []

print(cpf)

for digit in range(9):
    numbers.append(int(cpf[digit]) * (10 - digit))

total = 0
for number in numbers:
    total += number

new_total = total * 10


first_digit = 0 if (new_total % 11) > 9 else new_total % 11
print(first_digit)
