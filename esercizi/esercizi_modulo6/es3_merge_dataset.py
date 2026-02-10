"""
Esercizio 3: Merge di Dataset

Obiettivo:
Unire dati da file diversi per creare un report completo.

Concetti chiave:
- Merge multipli con pd.merge()
- Left join per mantenere tutte le righe principali
- Colonne calcolate derivate
- Aggregazioni su dati uniti
- Normalizzazione dati (evitare duplicazione)
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("ESERCIZIO 3: Merge di Dataset")
print("=" * 60)

# Creazione file di test
print("\n📁 Creazione file di test...")

# Dataset 1: Vendite
vendite_data = {
    "Vendita_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Cliente_ID": [101, 102, 101, 103, 104, 102, 105, 103],
    "Prodotto_ID": [1, 2, 3, 1, 4, 2, 3, 5],
    "Quantità": [2, 1, 3, 1, 2, 2, 1, 4]
}
pd.DataFrame(vendite_data).to_csv("vendite.csv", index=False)
print("✅ vendite.csv creato")

# Dataset 2: Clienti
clienti_data = {
    "Cliente_ID": [101, 102, 103, 104, 105],
    "Nome_Cliente": ["Alice Rossi", "Bob Bianchi", "Charlie Verdi", "Diana Neri", "Eve Gialli"],
    "Città_Cliente": ["Roma", "Milano", "Roma", "Napoli", "Milano"]
}
pd.DataFrame(clienti_data).to_csv("clienti.csv", index=False)
print("✅ clienti.csv creato")

# Dataset 3: Prodotti
prodotti_data = {
    "Prodotto_ID": [1, 2, 3, 4, 5],
    "Nome_Prodotto": ["Laptop", "Mouse", "Tastiera", "Monitor", "Webcam"],
    "Categoria": ["Elettronica", "Accessori", "Accessori", "Elettronica", "Accessori"],
    "Prezzo": [999.00, 25.50, 75.00, 299.00, 89.00]
}
pd.DataFrame(prodotti_data).to_csv("prodotti.csv", index=False)
print("✅ prodotti.csv creato\n")

# === INIZIO SOLUZIONE ===

print("STEP 1: Caricamento dataset separati")
print("-" * 60)
# Carica i dataset
vendite = pd.read_csv("vendite.csv")
clienti = pd.read_csv("clienti.csv")
prodotti = pd.read_csv("prodotti.csv")

print(f"📊 Vendite: {len(vendite)} righe")
print(f"📊 Clienti: {len(clienti)} righe")
print(f"📊 Prodotti: {len(prodotti)} righe")

print("\nDataset VENDITE:")
print(vendite.head())

print("\nDataset CLIENTI:")
print(clienti.head())

print("\nDataset PRODOTTI:")
print(prodotti.head())

print("\n" + "STEP 2: Primo merge (Vendite + Clienti)")
print("-" * 60)
# Unisci vendite con clienti
print("LEFT JOIN: vendite <- clienti (su Cliente_ID)")
df = pd.merge(vendite, clienti, on="Cliente_ID", how="left")
print(f"✅ Merge completato: {len(df)} righe")
print("\nPrime righe dopo il primo merge:")
print(df.head())

print("\n" + "STEP 3: Secondo merge (+ Prodotti)")
print("-" * 60)
# Unisci con prodotti
print("LEFT JOIN: df <- prodotti (su Prodotto_ID)")
df = pd.merge(df, prodotti, on="Prodotto_ID", how="left")
print(f"✅ Merge completato: {len(df)} righe")
print("\nPrime righe dopo il secondo merge:")
print(df.head())

print("\n" + "STEP 4: Calcolo colonne derivate")
print("-" * 60)
# Calcola metriche
print("Calcolo Totale = Quantità * Prezzo...")
df["Totale"] = df["Quantità"] * df["Prezzo"]
print("✅ Colonna Totale aggiunta")

print("\nDataset completo unito:")
print(df)

print("\n" + "STEP 5: Report geografico per città")
print("-" * 60)
# Report per città del cliente
print("Aggregazione per Città_Cliente...")
report_geo = df.groupby("Città_Cliente").agg({
    "Totale": "sum",
    "Cliente_ID": "nunique"
}).rename(columns={
    "Totale": "Fatturato_Totale",
    "Cliente_ID": "N_Clienti"
})

# Ordina per fatturato discendente
report_geo = report_geo.sort_values("Fatturato_Totale", ascending=False)

print("\n📊 REPORT GEOGRAFICO:")
print(report_geo)

print("\n" + "STEP 6: Analisi per categoria prodotto")
print("-" * 60)
report_categoria = df.groupby("Categoria").agg({
    "Totale": ["sum", "mean"],
    "Quantità": "sum"
})
report_categoria.columns = ["Fatturato", "Importo_Medio", "Unità_Vendute"]

print("\n📊 REPORT PER CATEGORIA:")
print(report_categoria)

# Top cliente
print("\n" + "STEP 7: Identificazione top cliente")
print("-" * 60)
top_clienti = df.groupby(["Cliente_ID", "Nome_Cliente"])["Totale"].sum().sort_values(ascending=False)

print("\n🏆 TOP 3 CLIENTI:")
for i, (idx, valore) in enumerate(top_clienti.head(3).items(), 1):
    cliente_id, nome = idx
    print(f"{i}. {nome} (ID: {cliente_id}) - €{valore:.2f}")

# Statistiche finali
print("\n📈 STATISTICHE COMPLESSIVE:")
print(f"   Fatturato totale: €{df['Totale'].sum():.2f}")
print(f"   Transazioni totali: {len(df)}")
print(f"   Clienti unici: {df['Cliente_ID'].nunique()}")
print(f"   Prodotti venduti: {df['Prodotto_ID'].nunique()}")
print(f"   Importo medio per transazione: €{df['Totale'].mean():.2f}")

# Cleanup
print("\n🧹 Pulizia file temporanei...")
from pathlib import Path
Path("vendite.csv").unlink()
Path("clienti.csv").unlink()
Path("prodotti.csv").unlink()
print("✅ File temporanei rimossi")

print("\n" + "=" * 60)
print("ESERCIZIO COMPLETATO!")
print("=" * 60)
print("""
Concetti applicati:
✓ Merge multipli con pd.merge()
✓ Left join (how='left') per mantenere tutte le righe
✓ Join su colonne con nomi identici (on='ColonnaID')
✓ Colonne calcolate da più dataset
✓ Aggregazioni su dati normalizzati

Perché normalizzare i dati?
- Evita duplicazione (es. indirizzo cliente ripetuto in ogni vendita)
- Facilita aggiornamenti (cambi un cliente in un solo posto)
- Riduce errori (inconsistenze nei dati duplicati)
- Migliora performance (meno spazio, query più veloci)

Il pattern vendite-clienti-prodotti è tipico dei database relazionali!
""")
