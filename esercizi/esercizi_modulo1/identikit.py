"""
Laboratorio 1: Generatore di Identikit

Obiettivo:
- Definire variabili per nome, anno_nascita, città
- Calcolare l'età attuale
- Usare f-string per stampare una frase completa
- BONUS: Verificare se l'età è pari o dispari
"""

# Setup Variabili
nome = "Giulia"
anno_nascita = 1995
anno_corrente = 2026
citta = "Milano"

# Calcolo
eta = anno_corrente - anno_nascita
is_pari = (eta % 2 == 0)

# Output
print(f"Ciao, sono {nome}, ho {eta} anni e vengo da {citta}.")
print(f"La mia età è un numero pari? {is_pari}")
