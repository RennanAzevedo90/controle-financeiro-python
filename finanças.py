import os

# Sistema de Controle Financeiro Pessoal - Versão Estatísticas Alinhada
saldo = 0.0
historico_transacoes = []

# Mapeia a pasta automática do script
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_salvamento = os.path.join(pasta_atual, "historico.txt")

# LER O ARQUIVO AO INICIAR O PROGRAMA
if os.path.exists(caminho_salvamento):
    print("Carregando dados salvos anteriormente...")
    with open(caminho_salvamento, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                historico_transacoes.append(linha)
                
                # Reconstrução segura do saldo
                if "$ " in linha:
                    partes = linha.split("$ ")
                    if len(partes) > 1:
                        valor_texto = partes[1].replace(",", ".")
                        valor_float = float(valor_texto)
                        
                        if "[GANHO]" in linha:
                            saldo = saldo + valor_float
                        elif "[GASTO]" in linha:
                            saldo = saldo - valor_float

print("--- BEM-VINDO AO SEU CONTROLE FINANCEIRO ---")

while True:
    # Menu de Opções
    print("\nEscolha uma opção:")
    print("1 - Ver Saldo e Histórico")
    print("2 - Adicionar Ganho (Receita)")
    print("3 - Adicionar Gasto (Despesa)")
    print("4 - Ver Estatísticas Detalhadas")
    print("5 - Sair do Programa")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        print(f"\n----- SEU EXTRATO -----")
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("Histórico de Movimentações:")
        if not historico_transacoes:
            print("Nenhuma transação registrada.")
        else:
            for transacao in historico_transacoes:
                print(transacao)

    elif opcao == "2":
        valor = float(input("Digite o valor do ganho (R$): "))
        descricao = input("Digite uma descrição (ex: Salário): ")
        saldo = saldo + valor
        
        linha = f"[GANHO] {descricao}: +R$ {valor:.2f}"
        historico_transacoes.append(linha)
        
        with open(caminho_salvamento, "a", encoding="utf-8") as arquivo:
            arquivo.write(linha + "\n")
            
        print("Ganho adicionado com sucesso e salvo no arquivo!")

    elif opcao == "3":
        valor = float(input("Digite o valor do gasto (R$): "))
        descricao = input("Digite uma descrição (ex: Mercado): ")
        saldo = saldo - valor
        
        linha = f"[GASTO] {descricao}: -R$ {valor:.2f}"
        historico_transacoes.append(linha)
        
        with open(caminho_salvamento, "a", encoding="utf-8") as arquivo:
            arquivo.write(linha + "\n")
            
        print("Gasto adicionado com sucesso e salvo no arquivo!")

    # --- OPÇÃO 4: PROCESSAMENTO DO RELATÓRIO ---
    elif opcao == "4":
        print("\n----- ESTATÍSTICAS DETALHADAS -----")
        total_ganhos = 0.0
        total_gastos = 0.0
        maior_gasto = 0.0
        
        for transacao in historico_transacoes:
            if "$ " in transacao:
                partes = transacao.split("$ ")
                if len(partes) > 1:
                    valor_float = float(partes[1].replace(",", "."))
                    
                    if "[GANHO]" in transacao:
                        total_ganhos = total_ganhos + valor_float
                    elif "[GASTO]" in transacao:
                        total_gastos = total_gastos + valor_float
                        if valor_float > maior_gasto:
                            maior_gasto = valor_float
                            
        print(f"Faturamento Total (Ganhos): R$ {total_ganhos:.2f}")
        print(f"Custo Total (Despesas): R$ {total_gastos:.2f}")
        print(f"Maior despesa registrada: R$ {maior_gasto:.2f}")

    elif opcao == "5":
        print("\nObrigado por usar o Controle Financeiro. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")

