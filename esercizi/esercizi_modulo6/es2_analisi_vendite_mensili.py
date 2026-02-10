"""
Esercizio 2: Analisi Vendite Mensili

Obiettivo:
Creare un report che mostri l'andamento delle vendite per mese.

Concetti chiave:
- Estrazione periodo da datetime con .dt.to_period()
- Aggregazioni multiple con dizionario in agg()
- Conteggio valori unici con nunique()
- Rinominare colonne con rename()
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("=" * 60)
print("ESERCIZIO 2: Analisi Vendite Mensili")
print("=" * 60)

# Creazione file di test vendite_annuali.csv
print("\n📁 Creazione file di test 'vendite_annuali.csv'...")

# Genera dati per 12 mesi (2023)
np.random.seed(42)
date_base = datetime(2023, 1, 1)
n_records = 200

dati_test = {
    "Data": [date_base + timedelta(days=np.random.randint(0, 365)) for _ in range(n_records)],
    "Ordine_ID": [f"ORD{i:04d}" for i in range(1, n_records + 1)],
    "Cliente_ID": [f"CLI{np.random.randint(1, 51):03d}" for _ in range(n_records)],
    "Importo": np.random.uniform(20, 500, n_records).round(2)
}

pd.DataFrame(dati_test).to_csv("vendite_annuali.csv", index=False)
print("✅ File creato con 200 transazioni per l'anno 2023!\n")

# === INIZIO SOLUZIONE ===

print("STEP 1: Caricamento e preparazione dati")
print("-" * 60)
# Carica dati
df = pd.read_csv("vendite_annuali.csv")
print(f"📊 Righe caricate: {len(df)}")
print(f"📊 Periodo: {df['Data'].min()} - {df['Data'].max()}")

# Conversione date
df["Data"] = pd.to_datetime(df["Data"])
print("✅ Colonna Data convertita in datetime")

print("\nPrime righe del dataset:")
print(df.head())

print("\n" + "STEP 2: Estrazione mese e anno")
print("-" * 60)
# Estrai mese e anno
df["Anno_Mese"] = df["Data"].dt.to_period("M")
print("✅ Colonna Anno_Mese creata con .dt.to_period('M')")
print(f"Esempio valori: {df['Anno_Mese'].head(3).tolist()}")

print("\n" + "STEP 3: Aggregazione mensile")
print("-" * 60)
print("Raggruppamento per mese con aggregazioni multiple...")
# Aggregazione mensile
report_mensile = df.groupby("Anno_Mese").agg({
    "Importo": "sum",
    "Ordine_ID": "nunique",
    "Cliente_ID": "nunique"
}).rename(columns={
    "Importo": "Fatturato",
    "Ordine_ID": "N_Ordini",
    "Cliente_ID": "Clienti_Unici"
})

print("\n📊 REPORT VENDITE MENSILI:")
print(report_mensile)

print("\n" + "STEP 4: Statistiche aggiuntive")
print("-" * 60)
# Calcola metriche aggiuntive
report_mensile["Importo_Medio"] = (report_mensile["Fatturato"] / report_mensile["N_Ordini"]).round(2)

print("Report completo con importo medio per ordine:")
print(report_mensile)

# Identifica il mese migliore
mese_migliore = report_mensile["Fatturato"].idxmax()
fatturato_max = report_mensile["Fatturato"].max()

print(f"\n🏆 MESE MIGLIORE: {mese_migliore}")
print(f"   Fatturato: €{fatturato_max:.2f}")
print(f"   N. Ordini: {report_mensile.loc[mese_migliore, 'N_Ordini']}")
print(f"   Clienti Unici: {report_mensile.loc[mese_migliore, 'Clienti_Unici']}")

# Statistiche annuali
print("\n📈 STATISTICHE ANNUALI:")
print(f"   Fatturato totale: €{report_mensile['Fatturato'].sum():.2f}")
print(f"   Media mensile: €{report_mensile['Fatturato'].mean():.2f}")
print(f"   Ordini totali: {report_mensile['N_Ordini'].sum()}")
print(f"   Clienti unici totali: {df['Cliente_ID'].nunique()}")

# Cleanup
print("\n🧹 Pulizia file temporanei...")
from pathlib import Path
Path("vendite_annuali.csv").unlink()
print("✅ File vendite_annuali.csv rimosso")

print("\n" + "=" * 60)
print("ESERCIZIO COMPLETATO!")
print("=" * 60)
print("""
Concetti applicati:
✓ Estrazione periodo con .dt.to_period('M')
✓ Aggregazioni multiple con dizionario
✓ Conteggio valori unici con nunique()
✓ Rinominare colonne con rename()
✓ Identificare massimi con idxmax()

La funzione .dt.to_period() è perfetta per analisi temporali perché:
- Raggruppa automaticamente date per periodo (M=mese, Q=trimestre, Y=anno)
- Crea indici che Pandas gestisce in modo efficiente
- Ideale per time series e report periodici
""")
