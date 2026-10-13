# Sistema de Controle Financeiro Pessoal
saldo = 0.0
historico_transacoes = []

print("--- BEM-VINDO AO SEU CONTROLE FINANCEIRO ---")

while True:
    # 1. Menu de Opções
    print("\nEscolha uma opção:")
    print("1 - Ver Saldo e Histórico")
    print("2 - Adicionar Ganho (Receita)")
    print("3 - Adicionar Gasto (Despesa)")
    print("4 - Sair do Programa")
    
    opcao = input("Digite o número da opção desejada: ")
    
    # 2. Fluxo de Decisão (Regras de Negócio)
    if opcao == "1":
        print(f"\n===== SEU EXTRATO =====")
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("Histórico:")
        if not historico_transacoes:
            print("  Nenhuma transação registrada.")
        else:
            for transacao in historico_transacoes:
                print(f"  - {transacao}")
        print("=======================")
        
    elif opcao == "2":
        valor = float(input("Digite o valor do ganho: R$ "))
        descricao = input("Digite a descrição (ex: Salário, Freelance): ")
        
        saldo += valor
        historico_transacoes.append(f"Ganho: +R$ {valor:.2f} ({descricao})")
        print("Ganho adicionado com sucesso!")
        
    elif opcao == "3":
        valor = float(input("Digite o valor do gasto: R$ "))
        descricao = input("Digite a descrição (ex: Aluguel, Ifood): ")
        
        saldo -= valor
        historico_transacoes.append(f"Gasto: -R$ {valor:.2f} ({descricao})")
        print("Gasto registrado com sucesso!")
        
        # --- BLOCO DE ALERTA CORRIGIDO E ALINHADO ---
        if saldo <= 0:
            print("\n⚠️ ATENÇÃO CRÍTICA: Seu saldo está zerado ou negativo!")
            print(f"Saldo atual: R$ {saldo:.2f}")
            
    elif opcao == "4":
        print("\nObrigado por usar o sistema! Até logo.")
        break
        
    else:
        print("Opção inválida! Escolha um número de 1 a 4.")