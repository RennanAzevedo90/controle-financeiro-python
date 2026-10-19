import os

# Sistema de Controle Financeiro Pessoal - Versão Avançada
saldo = 0.0
historico_transacoes = []

# Mapeia a pasta automática do script
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_salvamento = os.path.join(pasta_atual, "historico.txt")

# --- NOVO: LER O ARQUIVO AO INICIAR O PROGRAMA ---
# Verifica se o arquivo já existe antes de tentar abrir
if os.path.exists(caminho_salvamento):
    print("Carregando dados salvos anteriormente...")
    with open(caminho_salvamento, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip() # Remove quebras de linha invisíveis
            if linha:
                historico_transacoes.append(linha)
                
                # RECONSTRUÇÃO DO SALDO: Descobre o valor dentro do texto
                # Procura por "+R$ " ou "-R$ " e extrai o número
                partes = linha.split("$ ")
                if len(partes) > 1:
                    valor_texto = partes[1].replace(",", ".") # Garante ponto decimal
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
    print("4 - Sair do Programa")

    opcao = input("Digite o número da opção desejada: ")

    # Fluxo de Decisão
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

    elif opcao == "4":
        print("\nObrigado por usar o Controle Financeiro. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")

