primeiro_valor = int(input("Digite um valor: "))
segundo_valor = int(input("Digite outro valor: "))

if primeiro_valor > segundo_valor:
    print(
        f"O Primeiro Valor {primeiro_valor} é maior "
        f"do que Segundo Valor {segundo_valor}"
    )
elif segundo_valor > primeiro_valor:
    print(
        f"O Segundo Valor {segundo_valor} é maior "
        f"do que o Primeiro valor {primeiro_valor}"
    )
else:
    print("Os valores são iguais...")
