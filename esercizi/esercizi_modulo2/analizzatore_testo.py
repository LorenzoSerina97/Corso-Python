"""
Esercizio 2: Analizzatore di Testo

Obiettivo:
- Usare Set e Dizionari per analizzare un testo
- Contare la frequenza di ogni parola
- Trovare parole uniche
- Trovare parole in comune tra due testi
"""

# Testi di esempio
testo1 = "il gatto e il cane giocano nel giardino"
testo2 = "il cane corre nel parco"


def conta_parole(testo):
    """Conta la frequenza di ogni parola nel testo."""
    parole = testo.lower().split()
    frequenza = {}
    for parola in parole:
        frequenza[parola] = frequenza.get(parola, 0) + 1
    return frequenza


# Parole uniche per ogni testo (usando set)
parole1 = set(testo1.split())
parole2 = set(testo2.split())

# Analisi
print("=== ANALISI TESTO 1 ===")
print(f"Frequenza parole: {conta_parole(testo1)}")
print(f"Parole uniche: {parole1}")

print("\n=== CONFRONTO TRA TESTI ===")
print(f"Parole in comune: {parole1 & parole2}")
print(f"Solo in testo1: {parole1 - parole2}")
print(f"Solo in testo2: {parole2 - parole1}")
