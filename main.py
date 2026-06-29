import time
import os


# 1. GRAFOS 
# Brasília
rede_metro_bsb = {
    'Central': ['Galeria'],
    'Galeria': ['Central', '114 Sul'],
    '114 Sul': ['Galeria', 'Terminal Asa Sul'],
    'Terminal Asa Sul': ['114 Sul', 'Shopping'],
    'Shopping': ['Terminal Asa Sul', 'Guará'],
    'Guará': ['Shopping', 'Águas Claras'],
    'Águas Claras': ['Guará', 'Concessionárias', 'Taguatinga Sul'],
    'Concessionárias': ['Águas Claras', 'Praça Do Relógio'],
    'Praça Do Relógio': ['Concessionárias', 'Ceilândia Centro'],
    'Ceilândia Centro': ['Praça Do Relógio', 'Terminal Ceilândia'],
    'Terminal Ceilândia': ['Ceilândia Centro'],
    'Taguatinga Sul': ['Águas Claras', 'Furnas'],
    'Furnas': ['Taguatinga Sul', 'Terminal Samambaia'],
    'Terminal Samambaia': ['Furnas']
}

# São Paulo
rede_metro_sp = {
    'Palmeiras-Barra Funda': ['República'],
    'República': ['Palmeiras-Barra Funda', 'Luz', 'Sé', 'Consolação'],
    'Luz': ['República', 'Sé'],
    'Sé': ['Luz', 'República', 'Brás', 'Paraíso'],
    'Brás': ['Sé', 'Tatuapé'],
    'Tatuapé': ['Brás'],
    'Vila Madalena': ['Consolação'],
    'Consolação': ['Vila Madalena', 'República', 'Pinheiros', 'Paraíso'],
    'Pinheiros': ['Consolação', 'Morumbi'],
    'Morumbi': ['Pinheiros'],
    'Paraíso': ['Sé', 'Consolação', 'Ana Rosa'],
    'Ana Rosa': ['Paraíso', 'Vila Mariana'],
    'Vila Mariana': ['Ana Rosa']
}


# 2. FUNÇÕES VISUAIS E DE BUSCA

def limpar_tela():
    """Limpa o terminal para deixar a visualização mais limpa"""
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar_mapa_bsb():
    print("======================================================")
    print("             MAPA DO METRÔ DE BRASÍLIA                ")
    print("======================================================")
    print("                     [Central]                        ")
    print("                         |                            ")
    print("                     [Galeria]                        ")
    print("                         |                            ")
    print("                     [114 Sul]                        ")
    print("                         |                            ")
    print("                 [Terminal Asa Sul]                   ")
    print("                         |                            ")
    print("                     [Shopping]                       ")
    print("                         |                            ")
    print("                      [Guará]                         ")
    print("                         |                            ")
    print("                   [Águas Claras]                     ")
    print("                    /         \\                      ")
    print("       (Linha Verde)           (Linha Laranja)        ")
    print("     [Concessionárias]        [Taguatinga Sul]        ")
    print("            |                        |                ")
    print("    [Praça Do Relógio]            [Furnas]            ")
    print("            |                        |                ")
    print("    [Ceilândia Centro]      [Terminal Samambaia]      ")
    print("            |                                         ")
    print("   [Terminal Ceilândia]                               ")
    print("======================================================")

def desenhar_mapa_sp():
    print("======================================================")
    print("       MAPA DO METRÔ DE SÃO PAULO (Centro Expandido)  ")
    print("======================================================")
    print("                                                      ")
    print(" [Palmeiras-Barra Funda]             [Vila Madalena]  ")
    print("           |                               |          ")
    print("      [República] ------------------- [Consolação]    ")
    print("       /       \\                           |  \\     ")
    print("    [Luz]-------[Sé]                       |   [Pinheiros] ")
    print("                 | \\                       |        |   ")
    print("                 |  \\------------------ [Paraíso] [Morumbi]")
    print("              [Brás]                       |          ")
    print("                 |                     [Ana Rosa]     ")
    print("             [Tatuapé]                     |          ")
    print("                                     [Vila Mariana]   ")
    print("                                                      ")
    print("======================================================")

def bfs_visual(grafo, inicio, destino):
    """Executa a Busca em Largura (BFS) usando uma FILA"""
    fila = [(inicio, [inicio])]
    visitados = set()

    print(f"\n[SISTEMA] Iniciando Busca em LARGURA (BFS)...")
    time.sleep(1)

    while fila:
        vertice, caminho = fila.pop(0) 

        if vertice not in visitados:
            print(f"🔎 Explorando estação: {vertice}...")
            time.sleep(0.7) 

            if vertice == destino:
                print("\n✅ DESTINO ENCONTRADO!")
                time.sleep(1)
                return caminho
            
            visitados.add(vertice)
            
            vizinhos_nao_visitados = [v for v in grafo[vertice] if v not in visitados]
            if vizinhos_nao_visitados:
                print(f"   -> Ramificando para: {', '.join(vizinhos_nao_visitados)}")
            else:
                print("   -> Fim da linha. Voltando...")
            
            time.sleep(0.5)

            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))
                    
    return None

def dfs_visual(grafo, inicio, destino):
    """Executa a Busca em Profundidade (DFS) usando uma PILHA"""
    pilha = [(inicio, [inicio])]
    visitados = set()

    print(f"\n[SISTEMA] Iniciando Busca em PROFUNDIDADE (DFS)...")
    time.sleep(1)

    while pilha:
        vertice, caminho = pilha.pop() 

        if vertice not in visitados:
            print(f"🔎 Aprofundando na estação: {vertice}...")
            time.sleep(0.7) 

            if vertice == destino:
                print("\n✅ DESTINO ENCONTRADO!")
                time.sleep(1)
                return caminho
            
            visitados.add(vertice)
            
            vizinhos_nao_visitados = [v for v in grafo[vertice] if v not in visitados]
            if vizinhos_nao_visitados:
                print(f"   -> Descendo para: {', '.join(vizinhos_nao_visitados)}")
            else:
                print("   -> Beco sem saída. Fazendo backtracking...")
            
            time.sleep(0.5)

            
            for vizinho in reversed(grafo[vertice]):
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho]))
                    
    return None

# 3. INTERFACE INTERATIVA 

while True:
    limpar_tela()
    print("======================================================")
    print("               SISTEMA DE ROTAS DE METRÔ              ")
    print("======================================================")
    print("1 - Brasília (BSB)")
    print("2 - São Paulo (SP)")
    print("0 - Sair")
    
    opcao_cidade = input("\nEscolha a cidade (0, 1 ou 2): ").strip()
    
    if opcao_cidade == '0':
        print("Saindo do sistema. Até logo!")
        break
    elif opcao_cidade == '1':
        grafo_atual = rede_metro_bsb
        desenhar_mapa = desenhar_mapa_bsb
    elif opcao_cidade == '2':
        grafo_atual = rede_metro_sp
        desenhar_mapa = desenhar_mapa_sp
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)
        continue

    limpar_tela()
    desenhar_mapa()

    estacoes_disponiveis = list(grafo_atual.keys())
    print("\nEstações disponíveis:")
    print(", ".join(estacoes_disponiveis))

    while True:
        origem = input("\n📍 Digite a estação de ORIGEM: ").strip().title()
        if origem in grafo_atual:
            break
        print("❌ Estação inválida. Digite exatamente como está na lista.")

    while True:
        destino = input("🏁 Digite a estação de DESTINO: ").strip().title()
        if destino in grafo_atual:
            break
        print("❌ Estação inválida. Digite exatamente como está na lista.")

    
    print("\n" + "="*54)
    print(" MÉTODOS DE BUSCA DISPONÍVEIS:")
    print(" 1 - Busca em Largura (BFS) - Garante o menor caminho")
    print(" 2 - Busca em Profundidade (DFS) - Explora até o fim")
    print("="*54)
    
    while True:
        opcao_busca = input("Escolha o algoritmo (1 ou 2): ").strip()
        if opcao_busca in ['1', '2']:
            break
        print("❌ Opção inválida. Digite 1 ou 2.")

    print("\n" + "-"*54)


    if opcao_busca == '1':
        rota = bfs_visual(grafo_atual, origem, destino)
    else:
        rota = dfs_visual(grafo_atual, origem, destino)

    
    print("\n======================================================")
    if rota:
        print(" 🚇 ROTA ENCONTRADA:")
        caminho_visual = " ➔ ".join([f"[{estacao}]" for estacao in rota])
        print(f"\n   {caminho_visual}")
        print(f"\n ⏱️ Total de estações percorridas: {len(rota)}")
        
        if opcao_busca == '2':
            print("Nota: A DFS encontra um caminho, não necessariamente o mais curto!")
    else:
        print(" ❌ Não foi possível encontrar uma rota.")
    print("======================================================")
    
    input("\nPressione ENTER para voltar ao menu inicial...")
