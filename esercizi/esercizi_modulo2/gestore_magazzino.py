"""
Esercizio 1: Gestore Magazzino

Obiettivo:
- Usare Liste e Dizionari insieme
- Gestire un magazzino con prodotti e quantità
- Registrare movimenti (vendite, rifornimenti)
"""

# Stato iniziale del magazzino
magazzino = {
    "Laptop": 10,
    "Mouse": 50,
    "Monitor": 5
}

# Lista per registrare i movimenti
movimenti = []

# Simulazione Vendita
prodotto_richiesto = "Mouse"

# Verifica disponibilità e aggiornamento
qta_disponibile = magazzino.get(prodotto_richiesto, 0)

if qta_disponibile > 0:
    magazzino[prodotto_richiesto] = qta_disponibile - 1
    # Log operazione (usando una Tupla per immutabilità dati)
    movimenti.append(("Vendita", prodotto_richiesto, 1))
    print(f"Venduto: {prodotto_richiesto}")
else:
    print(f"Prodotto non disponibile: {prodotto_richiesto}")

# Mostra stato finale
print(f"\nStato Magazzino: {magazzino}")
print(f"Log Movimenti: {movimenti}")
