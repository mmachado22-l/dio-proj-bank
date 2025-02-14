def saque(*, saldo, valor, numero_saques, limite=500, LIMITE_SAQUES=3):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, f"Saque falhou: saldo insuficiente.\n"
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, f"Saque falhou: valor excede o limite.\n"
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, f"Saque falhou: número máximo de saques excedido.\n"
    elif valor > 0:
        saldo -= valor
        extrato = f"Saque: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, f"Saque falhou: valor inválido.\n"

def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Já existe um usuário com este CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Informe o logradouro: ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    sigla_estado = input("Informe a sigla do estado (ex: SP): ")

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade} - {sigla_estado}"

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado.")
        return None

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato_saque = saque(saldo=saldo, valor=valor, numero_saques=numero_saques)
        if "Saque: R$" in extrato_saque:
            numero_saques += 1
        extrato += extrato_saque

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")