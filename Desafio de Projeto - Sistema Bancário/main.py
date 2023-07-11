import time

def menu():
    menu = """
----------MENU------------

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Saldo
    [5] - Sair

--------------------------

Digite qual operação deseja realizar:
 =>"""
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso. ===")
    else:
        print("\n@@@ Operação inválida, valor informado não pode ser depositado. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_valor_saque, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite_valor = valor > limite_valor_saque
    excedeu_numero_saque = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")

    elif excedeu_limite_valor:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_numero_saque:
        print("\n@@@ Operação falhou! Número máximo de saque excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print(f"\n=== Saque no valor de R${valor:.2f} efetuado com sucesso ===\n")

    else:
        print("\n@@@ Operação falhou, o valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato):
    extrato_nome = "Extrato"
    print(extrato_nome.center(30, "="))
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo atual é de: R${saldo:.2f}\n")
    print("=".center(30, "="))


saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    time.sleep(2)
    opcao = menu().strip(" ")

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: \n"))

        saldo, extrato = depositar(saldo,valor,extrato)

    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: \n"))

        saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite_valor_saque = limite_valor_saque,
            numero_saques = numero_saques,
            limite_saques = LIMITE_SAQUES,
        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == "4":
        print(f"\nSaldo atual é de: R${saldo:.2f}\n")

    elif opcao == "5":
        print("Saindo do sistema...")
        time.sleep(3)
        print("Obrigado, volte sempre!")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")


