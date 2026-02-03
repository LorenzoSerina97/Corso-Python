"""
Esercizio 4: Report Vendite per Categoria

Obiettivo: Creare un report aggregato per categoria prodotto.

Il programma:
1. Crea un DataFrame con dati di vendita
2. Raggruppa per categoria
3. Calcola statistiche aggregate (totale, media, conteggio)
4. Salva il report in Excel
"""

import pandas as pd
from pathlib import Path


def crea_dati_vendite():
    """Crea un DataFrame con dati di vendita di esempio."""
    
    print("📊 Creazione dataset vendite...")
    
    dati = {
        "Prodotto": ["Laptop", "Mouse", "Laptop", "Tastiera", "Mouse", 
                     "Monitor", "Webcam", "Tastiera", "Cuffie", "Mouse"],
        "Categoria": ["Elettronica", "Accessori", "Elettronica", "Accessori", "Accessori",
                      "Elettronica", "Accessori", "Accessori", "Accessori", "Accessori"],
        "Vendite": [1200, 25, 1100, 80, 30, 450, 75, 85, 120, 28]
    }
    
    df = pd.DataFrame(dati)
    
    print(f"✅ Dataset creato: {len(df)} transazioni\n")
    
    # Mostra i dati grezzi
    print("📋 Dati grezzi:")
    print("=" * 60)
    print(df.to_string(index=False))
    print("=" * 60)
    print()
    
    return df


def genera_report_categoria(df):
    """Genera report aggregato per categoria."""
    
    print("📈 Generazione report per categoria...\n")
    
    # Raggruppa per categoria e calcola statistiche
    report = df.groupby("Categoria").agg({
        "Vendite": ["sum", "mean", "count"]
    }).round(2)
    
    # Rinomina le colonne per maggiore chiarezza
    report.columns = ["Totale", "Media", "N_Vendite"]
    
    # Ordina per totale vendite (decrescente)
    report = report.sort_values("Totale", ascending=False)
    
    # Mostra il report
    print("📊 REPORT VENDITE PER CATEGORIA")
    print("=" * 60)
    print(report.to_string())
    print("=" * 60)
    print()
    
    # Statistiche aggiuntive
    print("💡 Insights:")
    categoria_top = report["Totale"].idxmax()
    vendite_top = report.loc[categoria_top, "Totale"]
    print(f"   🏆 Categoria top: {categoria_top} (€{vendite_top:.2f})")
    
    categoria_media_alta = report["Media"].idxmax()
    media_alta = report.loc[categoria_media_alta, "Media"]
    print(f"   📊 Media vendita più alta: {categoria_media_alta} (€{media_alta:.2f})")
    
    totale_generale = report["Totale"].sum()
    print(f"   💰 Fatturato totale: €{totale_generale:.2f}")
    print()
    
    return report


def salva_report_excel(report):
    """Salva il report in un file Excel."""
    
    filename = "report_categorie.xlsx"
    
    print(f"💾 Salvataggio report in {filename}...")
    
    try:
        # Salva in Excel
        report.to_excel(filename)
        
        # Verifica
        file_size = Path(filename).stat().st_size
        print(f"✅ Report salvato ({file_size} bytes)\n")
        
        # Verifica caricamento
        print("🔍 Verifica integrità file Excel...")
        df_verificato = pd.read_excel(filename, index_col=0)
        print(f"✅ File Excel valido")
        print(f"   Categorie: {len(df_verificato)}")
        print(f"   Colonne: {list(df_verificato.columns)}\n")
        
        return True
        
    except Exception as e:
        print(f"❌ Errore durante il salvataggio: {e}")
        return False


def analisi_dettagliata(df):
    """Analisi dettagliata per prodotto."""
    
    print("🔍 ANALISI DETTAGLIATA PER PRODOTTO")
    print("=" * 60)
    
    # Raggruppa per prodotto
    per_prodotto = df.groupby("Prodotto").agg({
        "Vendite": ["sum", "count"]
    }).round(2)
    
    per_prodotto.columns = ["Totale_Vendite", "N_Transazioni"]
    per_prodotto = per_prodotto.sort_values("Totale_Vendite", ascending=False)
    
    print(per_prodotto.to_string())
    print("=" * 60)
    print()
    
    # Top 3 prodotti
    print("🏆 Top 3 Prodotti:")
    for i, (prodotto, row) in enumerate(per_prodotto.head(3).iterrows(), 1):
        print(f"   {i}. {prodotto}: €{row['Totale_Vendite']:.2f} "
              f"({int(row['N_Transazioni'])} transazioni)")
    print()


def main():
    """Funzione principale."""
    print("=" * 60)
    print("ESERCIZIO 4: REPORT VENDITE PER CATEGORIA")
    print("=" * 60)
    print()
    
    # 1. Crea dati di vendita
    df = crea_dati_vendite()
    
    # 2. Genera report per categoria
    report = genera_report_categoria(df)
    
    # 3. Salva in Excel
    successo = salva_report_excel(report)
    
    if successo:
        # 4. Analisi dettagliata bonus
        analisi_dettagliata(df)
        
        print("=" * 60)
        print("REPORT COMPLETATO CON SUCCESSO")
        print("=" * 60)
        print(f"\n📄 File creato: report_categorie.xlsx")
        print("📊 Categorie analizzate:", len(report))
    else:
        print("\n❌ Errore nella generazione del report")
    
    # Cleanup opzionale (commenta se vuoi mantenere il file)
    # if Path("report_categorie.xlsx").exists():
    #     Path("report_categorie.xlsx").unlink()


if __name__ == "__main__":
    main()
