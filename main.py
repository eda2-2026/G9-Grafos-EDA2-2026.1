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
