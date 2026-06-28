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
