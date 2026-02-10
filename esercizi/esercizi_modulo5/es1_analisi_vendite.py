"""
Esercizio 1: Analisi Vendite

Scenario: Hai un file vendite_raw.csv con colonne: Prodotto, Quantità, PrezzoUnitario.
Alcuni prezzi sono negativi (errore di sistema).

Obiettivo:
1. Caricare il CSV
2. Filtrare via i prezzi errati (<= 0)
3. Calcolare il Totale per ogni riga (Quantità * Prezzo)
4. Salvare il report pulito in un nuovo file JSON
"""

import csv
import json
from pathlib import Path


def crea_dati_test():
    """Crea un file CSV di test con alcuni prezzi negativi."""
    dati_test = [
        ["Prodotto", "Quantità", "PrezzoUnitario"],
        ["Laptop", "2", "999.99"],
        ["Mouse", "5", "-29.99"],
        ["Tastiera", "3", "79.99"],
        ["Monitor", "1", "299.99"],
        ["Webcam", "4", "-49.99"],
        ["Cuffie", "2", "89.99"]
    ]
    
    with open("vendite_raw.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(dati_test)
    
    print("✅ File vendite_raw.csv creato con dati di test\n")


def analizza_vendite():
    """Analizza il file vendite e produce un report pulito."""
    
    # 1. Carico e processo
    vendite_pulite = []
    fatturato_totale = 0
    
    print("📂 Caricamento vendite_raw.csv...")
    
    with open("vendite_raw.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        righe_totali = 0
        righe_negative = 0
        
        for riga in reader:
            righe_totali += 1
            prezzo = float(riga["PrezzoUnitario"])
            
            # 2. Filtra prezzi errati
            if prezzo > 0:
                quantita = int(riga["Quantità"])
                
                # 3. Calcola totale
                totale = quantita * prezzo
                
                vendite_pulite.append({
                    "Prodotto": riga["Prodotto"],
                    "Quantità": quantita,
                    "PrezzoUnitario": prezzo,
                    "Totale": totale
                })
                
                fatturato_totale += totale
            else:
                righe_negative += 1
    
    print(f"   Righe totali: {righe_totali}")
    print(f"   Righe con prezzi negativi: {righe_negative}")
    print(f"   Righe valide dopo pulizia: {len(vendite_pulite)}\n")
    
    print(f"📊 Fatturato Totale: €{fatturato_totale:.2f}")
    print(f"   Vendite valide: {len(vendite_pulite)}\n")
    
    # Mostra le vendite pulite
    print("📋 Report vendite pulito:")
    print("=" * 70)
    for vendita in vendite_pulite:
        print(f"{vendita['Prodotto']:12} - Qta: {vendita['Quantità']:2} - "
              f"Prezzo: €{vendita['PrezzoUnitario']:7.2f} - "
              f"Totale: €{vendita['Totale']:7.2f}")
    print("=" * 70)
    print()
    
    # 4. Export in JSON
    print("💾 Salvataggio report in JSON...")
    with open("report_vendite.json", "w", encoding="utf-8") as f:
        json.dump(vendite_pulite, f, indent=4, ensure_ascii=False)
    
    print("✅ Report salvato in report_vendite.json\n")
    
    # Mostra anteprima JSON
    print("📄 Anteprima JSON (primi 2 record):")
    print(json.dumps(vendite_pulite[:2], indent=2, ensure_ascii=False))
    
    return vendite_pulite


def main():
    """Funzione principale."""
    print("=" * 70)
    print("ESERCIZIO 1: ANALISI VENDITE")
    print("=" * 70)
    print()
    
    # Crea dati di test se il file non esiste
    if not Path("vendite_raw.csv").exists():
        crea_dati_test()
    
    # Esegui l'analisi
    vendite = analizza_vendite()
    
    print("\n" + "=" * 70)
    print("ANALISI COMPLETATA")
    print("=" * 70)
    
    # Cleanup opzionale (commenta se vuoi mantenere i file)
    # Path("vendite_raw.csv").unlink()
    # Path("report_vendite.json").unlink()


if __name__ == "__main__":
    main()
