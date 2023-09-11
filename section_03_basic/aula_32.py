"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input("Digite um número inteiro: ")

# try:
#     numero_int = int(numero)
#     if type(numero_int) is int:
#         if numero_int % 2 == 0:
#             print("O número digitado é par.")
#         else:
#             print("O número digitado é ímpar.")
# except:
#     print("O valor digitado não é um número inteiro")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# nome = input("Qual é seu nome? ")
# hora = int(input("Qual é a hora atual? "))

# if hora >= 0 and hora <= 11:
#     print(f"Bom dia {nome}")
# elif hora >= 12 and hora <= 17:
#     print(f"Boa tarde {nome}")
# elif hora >= 18 and hora <= 23:
#     print(f"Boa noite {nome}")
# else:
#     print(f"Hora inválida {hora}.")
#     print(f"Por favor use um número entre 0 e 23")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Qual é seu primeiro nome? ")
numero_de_letras = int(len(nome))

if numero_de_letras <= 4:
    print("Seu nome é curto.")
elif numero_de_letras >= 5 and numero_de_letras <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
