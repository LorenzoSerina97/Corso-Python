"""
Esercizio 4: Analizzatore di Numeri

Obiettivo:
- Funzione che analizza una lista di numeri
- Restituisce statistiche complete in un dizionario
- Usa list comprehension per filtrare pari/dispari
"""


def analizza_numeri(numeri):
    """
    Analizza una lista di numeri e restituisce statistiche.

    Args:
        numeri: Lista di numeri da analizzare.

    Returns:
        Dizionario con statistiche o None se lista vuota.
    """
    if not numeri:
        return None

    return {
        "conteggio": len(numeri),
        "somma": sum(numeri),
        "media": sum(numeri) / len(numeri),
        "minimo": min(numeri),
        "massimo": max(numeri),
        "pari": [n for n in numeri if n % 2 == 0],
        "dispari": [n for n in numeri if n % 2 != 0]
    }


# Test della funzione
print("=== ANALIZZATORE DI NUMERI ===\n")

dati = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Dati: {dati}\n")

stats = analizza_numeri(dati)

if stats:
    print("Statistiche:")
    for chiave, valore in stats.items():
        print(f"  {chiave.capitalize()}: {valore}")
else:
    print("Lista vuota!")

# Test con altri dati
print("\n" + "="*40 + "\n")
dati2 = [15, 22, 8, 33, 41, 7, 19, 28]
print(f"Dati: {dati2}\n")

stats2 = analizza_numeri(dati2)
if stats2:
    print("Statistiche:")
    for chiave, valore in stats2.items():
        print(f"  {chiave.capitalize()}: {valore}")
