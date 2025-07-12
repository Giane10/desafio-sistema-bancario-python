# --- Início: Funções do Sistema ---

def depositar(saldo, valor, extrato):
    """
    Função para realizar um depósito.
    Recebe o saldo atual, o valor a ser depositado e o extrato.
    Retorna o novo saldo e o novo extrato.
    """
    print("--- DENTRO DA FUNÇÃO DEPOSITAR ---")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor / 100:.2f}\n"
        print(">>> SUCESSO: Saldo e extrato atualizados.")
    else:
        print(">>> ERRO: Valor de depósito inválido.")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Função para realizar um saque.
    Verifica todas as regras de negócio antes de efetuar o saque.
    Retorna o novo saldo, novo extrato e novo número de saques.
    """
    print("--- DENTRO DA FUNÇÃO SACAR ---")
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(">>> ERRO: Saldo insuficiente.")
    elif excedeu_limite:
        print(f">>> ERRO: Limite de R$ {(limite / 100):.2f} excedido.")
    elif excedeu_saques:
        print(">>> ERRO: Número de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor / 100:.2f}\n"
        numero_saques += 1
        print(">>> SUCESSO: Saque realizado.")
    else:
        print(">>> ERRO: Valor de saque inválido.")

    return saldo, extrato, numero_saques


def mostrar_extrato(saldo, extrato):
    """
    Função para exibir o extrato da conta.
    """
    print("--- DENTRO DA FUNÇÃO MOSTRAR_EXTRATO ---")
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {(saldo / 100):.2f}")
    print("==========================================")


# --- Fim: Funções do Sistema ---


# --- Início: Programa Principal ---

# Declaração das variáveis iniciais
saldo = 0
limite = 50000  # R$ 500,00 em centavos
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

print(">>> PROGRAMA INICIADO <<<")

while True:
    print("\n>>> AGUARDANDO OPÇÃO DO USUÁRIO <<<")
    opcao = input(menu).strip().lower()
    print(f">>> USUÁRIO DIGITOU: [{opcao}] <<<")

    if opcao == "d":
        print(">>> OPÇÃO 'd' RECONHECIDA. CHAMANDO FUNÇÃO DEPOSITAR... <<<")
        try:
            valor_str = input("Informe o valor do depósito (ex: 50.25): ")
            valor_centavos = int(float(valor_str) * 100)
            saldo, extrato = depositar(saldo, valor_centavos, extrato)
        except ValueError:
            print(">>> ERRO: Entrada não é um número válido.")

    elif opcao == "s":
        print(">>> OPÇÃO 's' RECONHECIDA. CHAMANDO FUNÇÃO SACAR... <<<")
        try:
            valor_str = input("Informe o valor do saque (ex: 100.00): ")
            valor_centavos = int(float(valor_str) * 100)
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor_centavos,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        except ValueError:
            print(">>> ERRO: Entrada não é um número válido.")

    elif opcao == "e":
        print(">>> OPÇÃO 'e' RECONHECIDA. CHAMANDO FUNÇÃO MOSTRAR_EXTRATO... <<<")
        mostrar_extrato(saldo, extrato)

    elif opcao == "q":
        print(">>> OPÇÃO 'q' RECONHECIDA. ENCERRANDO O PROGRAMA... <<<")
        print("Obrigado por usar nosso sistema. Até logo!")
        break

    else:
        print(">>> OPÇÃO INVÁLIDA. MOSTRANDO O MENU NOVAMENTE. <<<")

# --- Fim: Programa Principal ---
