import os

def get_current_date():
    result = os.popen("date /t").read().strip()
    return result

current_date = get_current_date()
saldo = 0
limite = 500
extrato = f"Data: {current_date}\n"
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    nova_data = get_current_date()
    if nova_data != current_date:
        current_date = nova_data
        numero_saques = 0
        extrato = f"Data: {current_date}\n"
        print(f"\n== Nova data detectada: {current_date}. Reiniciando transações do dia. ==\n")

    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Operação falhou! Valor inválido.")
            continue

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Operação falhou! Valor inválido.")
            continue

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de R$ 500.00.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato == f"Data: {current_date}\n":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Encerrando o programa...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
