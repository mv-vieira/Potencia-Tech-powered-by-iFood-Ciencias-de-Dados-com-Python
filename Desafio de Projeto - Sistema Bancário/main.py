menu = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

"""

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {valor:.2f}\n"
        else:
            print("Operação inválida, valor informado não pode ser depositado")

    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite_valor = valor > limite_valor_saque
        excedeu_numero_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite_valor:
            print("O valor do saque excedeu o máximo permitido por operação.")

        elif excedeu_numero_saque:
            print("Você excedeu o limite de saques diários, tente novamente amanhã.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou, o valor informado é inválido.")

    elif opcao == "3":
        extrato_nome = "Extrato"
        print(extrato_nome.center(30,"-"))
        print("Não foram realizadas movimentações")


