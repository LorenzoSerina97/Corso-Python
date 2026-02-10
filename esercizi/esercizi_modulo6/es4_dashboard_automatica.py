"""
Esercizio 4: Dashboard Automatica

Obiettivo:
Creare una funzione riutilizzabile per generare statistiche dashboard.

Concetti chiave:
- Funzioni riutilizzabili per analisi
- Identificare valori massimi con idxmax()
- Timestamp con datetime.now()
- Restituire Series per output strutturato
- Calcolo metriche aggregate
"""

import pandas as pd
import numpy as np
from datetime import datetime

print("=" * 60)
print("ESERCIZIO 4: Dashboard Automatica")
print("=" * 60)

# Creazione file di test vendite.csv
print("\n📁 Creazione file di test 'vendite.csv'...")

np.random.seed(42)
n_vendite = 50

dati_test = {
    "Vendita_ID": range(1, n_vendite + 1),
    "Cliente_ID": [f"CLI{np.random.randint(1, 21):03d}" for _ in range(n_vendite)],
    "Prodotto": np.random.choice(["Laptop", "Mouse", "Tastiera", "Monitor", "Webcam", "Cuffie"], n_vendite),
    "Città": np.random.choice(["Roma", "Milano", "Napoli", "Torino", "Firenze"], n_vendite),
    "Quantità": np.random.randint(1, 5, n_vendite),
    "Prezzo_Unitario": np.random.choice([999, 25, 75, 299, 89, 45], n_vendite)
}

df_test = pd.DataFrame(dati_test)
df_test["Totale"] = df_test["Quantità"] * df_test["Prezzo_Unitario"]
df_test.to_csv("vendite.csv", index=False)
print(f"✅ File creato con {n_vendite} vendite!\n")

# === INIZIO SOLUZIONE ===

def genera_dashboard(df):
    """
    Genera statistiche per dashboard.
    
    Args:
        df: DataFrame con colonne ['Totale', 'Cliente_ID', 'Prodotto', 'Città']
    
    Returns:
        pd.Series con le statistiche chiave
    """
    
    dashboard = {
        "totale_vendite": df["Totale"].sum(),
        "media_ordine": df["Totale"].mean(),
        "n_ordini": len(df),
        "n_clienti": df["Cliente_ID"].nunique(),
        "prodotto_top": df.groupby("Prodotto")["Totale"].sum().idxmax(),
        "città_top": df.groupby("Città")["Totale"].sum().idxmax(),
        "ultimo_aggiornamento": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    return pd.Series(dashboard)


print("STEP 1: Caricamento dati")
print("-" * 60)
# Utilizzo
df = pd.read_csv("vendite.csv")
print(f"📊 Dati caricati: {len(df)} vendite")
print("\nPrime righe del dataset:")
print(df.head(10))

print("\n" + "STEP 2: Generazione statistiche dashboard")
print("-" * 60)
print("Chiamata funzione genera_dashboard()...\n")

stats = genera_dashboard(df)

print("📊 DASHBOARD STATISTICHE")
print("=" * 60)
print(f"💰 Totale Vendite:     €{stats['totale_vendite']:,.2f}")
print(f"📊 Media per Ordine:   €{stats['media_ordine']:,.2f}")
print(f"📦 Numero Ordini:      {stats['n_ordini']}")
print(f"👥 Clienti Unici:      {stats['n_clienti']}")
print(f"🏆 Prodotto Top:       {stats['prodotto_top']}")
print(f"🌆 Città Top:          {stats['città_top']}")
print(f"🕐 Ultimo Aggiornamento: {stats['ultimo_aggiornamento']}")
print("=" * 60)

print("\n" + "STEP 3: Dettaglio prodotti")
print("-" * 60)
print("Analisi dettagliata per prodotto...\n")

dettaglio_prodotti = df.groupby("Prodotto").agg({
    "Totale": ["sum", "mean", "count"],
    "Quantità": "sum"
})
dettaglio_prodotti.columns = ["Fatturato", "Importo_Medio", "N_Vendite", "Unità_Vendute"]
dettaglio_prodotti = dettaglio_prodotti.sort_values("Fatturato", ascending=False)

print("📊 DETTAGLIO PER PRODOTTO:")
print(dettaglio_prodotti)

print("\n" + "STEP 4: Dettaglio città")
print("-" * 60)
print("Analisi dettagliata per città...\n")

dettaglio_citta = df.groupby("Città").agg({
    "Totale": "sum",
    "Cliente_ID": "nunique",
    "Vendita_ID": "count"
}).rename(columns={
    "Totale": "Fatturato",
    "Cliente_ID": "Clienti_Unici",
    "Vendita_ID": "N_Vendite"
})
dettaglio_citta = dettaglio_citta.sort_values("Fatturato", ascending=False)

print("📊 DETTAGLIO PER CITTÀ:")
print(dettaglio_citta)

print("\n" + "STEP 5: Top clienti")
print("-" * 60)
top_5_clienti = df.groupby("Cliente_ID")["Totale"].sum().sort_values(ascending=False).head(5)

print("\n🏆 TOP 5 CLIENTI:")
for i, (cliente_id, totale) in enumerate(top_5_clienti.items(), 1):
    n_ordini = len(df[df["Cliente_ID"] == cliente_id])
    print(f"{i}. {cliente_id}: €{totale:,.2f} ({n_ordini} ordini)")

print("\n" + "STEP 6: Test riutilizzabilità funzione")
print("-" * 60)
print("Filtriamo solo le vendite di Roma e rigeniamo la dashboard...\n")

df_roma = df[df["Città"] == "Roma"].copy()
stats_roma = genera_dashboard(df_roma)

print("📊 DASHBOARD ROMA")
print("=" * 60)
print(f"💰 Totale Vendite:     €{stats_roma['totale_vendite']:,.2f}")
print(f"📊 Media per Ordine:   €{stats_roma['media_ordine']:,.2f}")
print(f"📦 Numero Ordini:      {stats_roma['n_ordini']}")
print(f"👥 Clienti Unici:      {stats_roma['n_clienti']}")
print(f"🏆 Prodotto Top:       {stats_roma['prodotto_top']}")
print(f"🕐 Ultimo Aggiornamento: {stats_roma['ultimo_aggiornamento']}")
print("=" * 60)

print("\n✅ La funzione è riutilizzabile su qualsiasi sottoinsieme di dati!")

# Cleanup
print("\n🧹 Pulizia file temporanei...")
from pathlib import Path
Path("vendite.csv").unlink()
print("✅ File vendite.csv rimosso")

print("\n" + "=" * 60)
print("ESERCIZIO COMPLETATO!")
print("=" * 60)
print("""
Concetti applicati:
✓ Funzioni riutilizzabili per analisi dati
✓ Identificare massimi con idxmax()
✓ Timestamp con datetime.now()
✓ Restituire pd.Series per output strutturato
✓ Calcolo metriche aggregate multiple

Vantaggi di usare funzioni per analisi:
- Riutilizzabilità (stessa analisi su dati diversi)
- Manutenibilità (logica centralizzata)
- Testing (facile testare una funzione)
- Scalabilità (automazione su più dataset)

Questo pattern è ideale per:
- Report automatici periodici
- Dashboard real-time
- API che servono statistiche
- Monitoraggio KPI aziendali
""")
