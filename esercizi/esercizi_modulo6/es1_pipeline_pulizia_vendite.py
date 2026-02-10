"""
Esercizio 1: Pipeline Pulizia Vendite

Obiettivo:
Creare una pipeline completa per pulire e analizzare dati di vendite grezzi.

Concetti chiave:
- Pulizia stringhe con .str.replace() e .str.strip()
- Conversione tipi con pd.to_numeric() e pd.to_datetime()
- Gestione valori mancanti con dropna()
- Aggregazione con groupby() e agg()
- Export in Excel con to_excel()
"""

import pandas as pd
from pathlib import Path

print("=" * 60)
print("ESERCIZIO 1: Pipeline Pulizia Vendite")
print("=" * 60)

# Creazione file di test raw_data.csv
print("\n📁 Creazione file di test 'raw_data.csv'...")
dati_test = {
    "Prodotto": ["Laptop", "Mouse", "Tastiera", "Monitor", "Webcam", "Cuffie", "Tablet"],
    "Categoria": ["Elettronica", "Accessori", "Accessori", "Elettronica", None, "Accessori", "Elettronica"],
    "Prezzo": ["€ 999.00", "€ 25.50", "€ 75.00", "€ 299.99", "€ 89.00", None, "€ 450.00"],
    "Quantità": [5, 20, 15, 8, 12, 25, 3],
    "Data": ["01/15/2024", "01/16/2024", "01/17/2024", "01/18/2024", "01/19/2024", "01/20/2024", "01/21/2024"]
}
pd.DataFrame(dati_test).to_csv("raw_data.csv", index=False)
print("✅ File creato con successo!\n")

# === INIZIO SOLUZIONE ===

print("STEP 1: Caricamento dati grezzi")
print("-" * 60)
# 1. Carica
df = pd.read_csv("raw_data.csv")
print(f"📊 Righe caricate: {len(df)}")
print(f"📊 Colonne: {list(df.columns)}")
print("\nPrime righe del dataset grezzo:")
print(df.head())

print("\n" + "STEP 2: Pulizia colonna Prezzo")
print("-" * 60)
# 2. Pulizia Prezzo
print("Rimozione simbolo '€' e spazi...")
df["Prezzo"] = df["Prezzo"].str.replace("€", "").str.strip()
print("Conversione in numerico (errori -> NaN)...")
df["Prezzo"] = pd.to_numeric(df["Prezzo"], errors="coerce")
print("✅ Prezzi puliti e convertiti in float")
print(f"Tipo colonna Prezzo: {df['Prezzo'].dtype}")

print("\n" + "STEP 3: Gestione valori mancanti")
print("-" * 60)
print("Valori mancanti per colonna:")
print(df.isnull().sum())
print("\nRimozione righe con NaN in Prezzo o Categoria...")
df = df.dropna(subset=["Prezzo", "Categoria"])
print(f"✅ Righe dopo pulizia: {len(df)}")

print("\n" + "STEP 4: Conversione date")
print("-" * 60)
# 4. Conversione date
print("Conversione da formato americano (MM/DD/YYYY) a datetime...")
df["Data"] = pd.to_datetime(df["Data"], format="%m/%d/%Y")
print("✅ Date convertite")
print(f"Tipo colonna Data: {df['Data'].dtype}")
print(f"Range date: {df['Data'].min()} -> {df['Data'].max()}")

print("\n" + "STEP 5: Calcolo totali e aggregazione")
print("-" * 60)
# 5. Calcolo totale e aggregazione
print("Calcolo colonna Totale = Quantità * Prezzo...")
df["Totale"] = df["Quantità"] * df["Prezzo"]

print("Aggregazione per Categoria...")
report = df.groupby("Categoria")["Totale"].agg(["sum", "mean", "count"])
report.columns = ["Totale_Vendite", "Media_Vendita", "N_Transazioni"]

print("\n📊 REPORT PER CATEGORIA:")
print(report)

print(f"\n💰 Totale complessivo vendite: €{df['Totale'].sum():.2f}")
print(f"📦 Totale prodotti venduti: {df['Quantità'].sum()}")

print("\n" + "STEP 6: Export in Excel")
print("-" * 60)
# 6. Export
report.to_excel("Report_Oggi.xlsx")
print("✅ Report salvato in 'Report_Oggi.xlsx'!")
print("   Puoi aprire il file Excel per visualizzare il report completo.")

# Cleanup
print("\n🧹 Pulizia file temporanei...")
Path("raw_data.csv").unlink()
print("✅ File raw_data.csv rimosso")

print("\n" + "=" * 60)
print("ESERCIZIO COMPLETATO!")
print("=" * 60)
print("""
Concetti applicati:
✓ Pulizia stringhe con .str metodi
✓ Conversione tipi di dato (to_numeric, to_datetime)
✓ Gestione NaN con dropna()
✓ Aggregazione con groupby() e agg()
✓ Export in Excel con to_excel()

NOTA: Il file 'Report_Oggi.xlsx' è stato creato nella directory corrente.
      Ricordati di eliminarlo quando hai finito di visualizzarlo.
""")
