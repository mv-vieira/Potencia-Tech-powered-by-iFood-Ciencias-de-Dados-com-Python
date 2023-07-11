import time

def menu():
    menu = """
----------MENU------------

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Saldo
    [5] - Criar Novo Usuário
    [6] - Criar Conta
    [7] - Listar Contas
    [8] - Sair do Sistema

--------------------------

Digite qual operação deseja realizar:
 =>"""
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\tDepósito: R${valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso. ===")
    else:
        print("\n@@@ Operação inválida, valor informado não pode ser depositado. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_valor_saque, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite_valor = valor > limite_valor_saque
    excedeu_numero_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")

    elif excedeu_limite_valor:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_numero_saque:
        print("\n@@@ Operação falhou! Número máximo de saque excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"\tSaque: R${valor:.2f}\n"
        numero_saques += 1
        print(f"\n=== Saque no valor de R${valor:.2f} efetuado com sucesso ===\n")

    else:
        print("\n@@@ Operação falhou, o valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato):
    extrato_nome = "Extrato"
    print(extrato_nome.center(30, "="))
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\tSaldo atual é de: R${saldo:.2f}\n")
    print("=".center(30, "="))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n@@@ Já existe um usuário com esse CPF. @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (ex: rua, nr, bairro - cidade/sigla estado): ")

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento":data_nascimento,
            "cpf":cpf,
            "endereco":endereco,
        }
    )
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia":agencia,
            "numero_conta": numero_conta,
            "usuario":usuario
        }
    print("\n@@@ Usuário não encontrado, impossível realizar a criação de conta. @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
    """
        print("="*100)
        print(linha)
def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite_valor_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:

        time.sleep(2)
        opcao = menu().strip(" ")

        if opcao == "1":
            valor = float(input("Digite o valor que deseja depositar: \n"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Digite o valor que deseja sacar: \n"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_valor_saque=limite_valor_saque,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            print(f"\nSaldo atual é de: R${saldo:.2f}\n")

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "6":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "7":
            listar_contas(contas)

        elif opcao == "8":
            print("Saindo do sistema...")
            time.sleep(2)
            print("Obrigado por utilizar nossos serviços!")
            break
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

main()



