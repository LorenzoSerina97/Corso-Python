"""
Esercizio 4: Report Vendite per Categoria

Obiettivo: Creare un report aggregato per categoria prodotto usando dizionari e CSV.

Il programma:
1. Definisce dati di vendita
2. Raggruppa per categoria usando defaultdict
3. Calcola statistiche aggregate (totale, media, conteggio)
4. Salva il report in CSV
"""

import csv
from collections import defaultdict


def main():
    """Funzione principale."""
    print("=" * 70)
    print("ESERCIZIO 4: REPORT VENDITE PER CATEGORIA")
    print("=" * 70)
    print()
    
    # Dati di esempio
    vendite = [
        {"Prodotto": "Laptop", "Categoria": "Elettronica", "Vendite": 1200},
        {"Prodotto": "Mouse", "Categoria": "Accessori", "Vendite": 25},
        {"Prodotto": "Laptop", "Categoria": "Elettronica", "Vendite": 1100},
        {"Prodotto": "Tastiera", "Categoria": "Accessori", "Vendite": 80},
        {"Prodotto": "Mouse", "Categoria": "Accessori", "Vendite": 30}
    ]
    
    print("📊 Dati vendite:")
    print("=" * 70)
    for v in vendite:
        print(f"{v['Prodotto']:12} - {v['Categoria']:15} - €{v['Vendite']}")
    print("=" * 70)
    print()
    
    # Aggregazione per categoria
    print("📈 Aggregazione per categoria...\n")
    report = defaultdict(lambda: {"totale": 0, "count": 0})
    
    for vendita in vendite:
        cat = vendita["Categoria"]
        report[cat]["totale"] += vendita["Vendite"]
        report[cat]["count"] += 1
    
    # Calcola medie e prepara output
    report_finale = []
    for categoria, dati in report.items():
        report_finale.append({
            "Categoria": categoria,
            "Totale": dati["totale"],
            "Media": round(dati["totale"] / dati["count"], 2),
            "N_Vendite": dati["count"]
        })
    
    # Stampa il report
    print("📊 REPORT VENDITE PER CATEGORIA:")
    print("=" * 70)
    for r in report_finale:
        print(f"{r['Categoria']:15} | Totale={r['Totale']:5} | "
              f"Media={r['Media']:7.2f} | N={r['N_Vendite']}")
    print("=" * 70)
    print()
    
    # Salva in CSV
    print("💾 Salvataggio report in CSV...")
    with open("report_categorie.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Categoria", "Totale", "Media", "N_Vendite"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_finale)
    
    print("✅ Report salvato in report_categorie.csv")
    
    # Verifica
    print("\n🔍 Verifica file CSV...")
    with open("report_categorie.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        righe = list(reader)
        print(f"✅ File valido - {len(righe)} categorie nel report")
    
    print("\n" + "=" * 70)
    print("REPORT COMPLETATO CON SUCCESSO")
    print("=" * 70)
    print(f"\n📄 File creato: report_categorie.csv")
    print(f"📊 Categorie analizzate: {len(report_finale)}")
    
    # Cleanup opzionale (commenta se vuoi mantenere il file)
    # from pathlib import Path
    # Path("report_categorie.csv").unlink()


if __name__ == "__main__":
    main()
