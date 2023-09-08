""" 
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexitentes na lista.

"""
import os

running = True
content = ""
option = None
lista = []

while running:
    os.system("clear")
    print("Selecione sua opção")
    print("1 - Inserir Item")
    print("2 - Apagar Item")
    print("3 - Listar")
    print("0 - Sair")

    print(f"\n{content}\n")

    user_input = input("Digite um número: ")

    try:
        option = int(user_input)
        if option == 0:
            running = False
        elif option == 1:
            item = input("Digite o Item que deseja inserir: ")
            lista.append(item)
            content = f"\t{item} inserido com sucesso..."
        elif option == 2:
            item = input("Digite o item que deseja remover: ")
            if item in lista:
                lista.remove(item)
                content = f"\t{item} removido com sucesso..."
            else:
                content = f"\t{item} não está na lista:\n\t{lista}"

        elif option == 3:
            content = f"\t{lista}"
    except:
        content = "\tEntrada inválida...\n\tPor favor insira um número listado acima..."
