"""
Esercizio 1: Analisi Vendite

Scenario: Hai un file vendite_raw.csv con colonne: Prodotto, Quantità, PrezzoUnitario.
Alcuni prezzi sono negativi (errore di sistema).

Obiettivo:
1. Caricare il CSV con Pandas
2. Filtrare via i prezzi errati (<= 0)
3. Calcolare il Totale per ogni riga (Quantità * Prezzo)
4. Salvare il report pulito in un nuovo file JSON
"""

import pandas as pd
from pathlib import Path

# Crea file di test con dati sporchi
def crea_dati_test():
    """Crea un file CSV di test con alcuni prezzi negativi."""
    dati_test = {
        "Prodotto": ["Laptop", "Mouse", "Tastiera", "Monitor", "Webcam", "Cuffie"],
        "Quantità": [2, 5, 3, 1, 4, 2],
        "PrezzoUnitario": [999.99, -29.99, 79.99, 299.99, -49.99, 89.99]
    }
    df_test = pd.DataFrame(dati_test)
    df_test.to_csv("vendite_raw.csv", index=False)
    print("✅ File vendite_raw.csv creato con dati di test\n")


def analizza_vendite():
    """Analizza il file vendite e produce un report pulito."""
    
    # 1. Carica il CSV
    print("📂 Caricamento vendite_raw.csv...")
    df = pd.read_csv("vendite_raw.csv")
    
    print(f"   Righe totali: {len(df)}")
    print(f"   Righe con prezzi negativi: {(df['PrezzoUnitario'] <= 0).sum()}\n")
    
    # 2. Pulizia - Tengo solo prezzi positivi
    print("🧹 Pulizia dati...")
    df_clean = df[df["PrezzoUnitario"] > 0].copy()
    print(f"   Righe valide dopo pulizia: {len(df_clean)}\n")
    
    # 3. Calcolo Totale per ogni riga
    print("💰 Calcolo totali...")
    df_clean["TotaleRiga"] = df_clean["Quantità"] * df_clean["PrezzoUnitario"]
    
    # Mostra il DataFrame pulito
    print("\n📊 Report vendite pulito:")
    print(df_clean.to_string(index=False))
    
    # Calcolo fatturato totale
    fatturato_totale = df_clean["TotaleRiga"].sum()
    print(f"\n💵 Fatturato Totale: €{fatturato_totale:.2f}\n")
    
    # 4. Export in JSON
    print("💾 Salvataggio report in JSON...")
    df_clean.to_json("report_vendite.json", orient="records", indent=4)
    print("✅ Report salvato in report_vendite.json\n")
    
    # Mostra anteprima JSON
    print("📄 Anteprima JSON (primi 2 record):")
    import json
    with open("report_vendite.json", "r") as f:
        data = json.load(f)
        print(json.dumps(data[:2], indent=2))
    
    return df_clean


def main():
    """Funzione principale."""
    print("=" * 60)
    print("ESERCIZIO 1: ANALISI VENDITE")
    print("=" * 60)
    print()
    
    # Crea dati di test se il file non esiste
    if not Path("vendite_raw.csv").exists():
        crea_dati_test()
    
    # Esegui l'analisi
    df_risultato = analizza_vendite()
    
    print("\n" + "=" * 60)
    print("ANALISI COMPLETATA")
    print("=" * 60)
    
    # Cleanup opzionale (commenta se vuoi mantenere i file)
    # Path("vendite_raw.csv").unlink()
    # Path("report_vendite.json").unlink()


if __name__ == "__main__":
    main()
