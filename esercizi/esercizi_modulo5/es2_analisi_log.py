"""
Esercizio 2: Analisi Log di Sistema

Scenario: Hai un file server.log con righe nel formato:
2024-01-15 10:30:45 INFO User login: mario@email.com
2024-01-15 10:31:22 ERROR Database connection failed
2024-01-15 10:32:01 WARNING High memory usage: 85%

Obiettivo:
1. Leggere il file di log
2. Contare quanti messaggi per ogni livello (INFO, ERROR, WARNING)
3. Salvare gli ERROR in un file separato
"""

from pathlib import Path
from collections import Counter
from datetime import datetime


def crea_log_test():
    """Crea un file di log di test."""
    log_entries = [
        "2024-01-15 10:30:45 INFO User login: mario@email.com",
        "2024-01-15 10:31:22 ERROR Database connection failed",
        "2024-01-15 10:32:01 WARNING High memory usage: 85%",
        "2024-01-15 10:33:15 INFO User logout: mario@email.com",
        "2024-01-15 10:35:42 ERROR Failed to write to disk",
        "2024-01-15 10:36:10 INFO User login: luigi@email.com",
        "2024-01-15 10:37:28 WARNING CPU usage at 90%",
        "2024-01-15 10:38:55 ERROR Connection timeout",
        "2024-01-15 10:40:12 INFO Data backup started",
        "2024-01-15 10:42:30 WARNING Disk space low: 15% remaining",
        "2024-01-15 10:45:18 INFO Data backup completed",
        "2024-01-15 10:47:05 ERROR Authentication failed for user: peach@email.com",
        "2024-01-15 10:50:22 INFO System health check: OK",
        "2024-01-15 10:52:40 WARNING Network latency high: 250ms",
    ]
    
    Path("server.log").write_text("\n".join(log_entries), encoding="utf-8")
    print("✅ File server.log creato con dati di test\n")


def analizza_log():
    """Analizza il file di log e genera statistiche."""
    
    log_path = Path("server.log")
    
    if not log_path.exists():
        print("❌ File server.log non trovato!")
        return
    
    print("📂 Lettura file server.log...")
    
    conteggio = Counter()
    errori = []
    warnings = []
    info = []
    
    # Leggi e analizza il log
    with open(log_path, "r", encoding="utf-8") as f:
        for riga in f:
            parti = riga.split()
            if len(parti) >= 3:
                livello = parti[2]  # INFO, ERROR, WARNING
                conteggio[livello] += 1
                
                # Raccogli i messaggi per livello
                if livello == "ERROR":
                    errori.append(riga)
                elif livello == "WARNING":
                    warnings.append(riga)
                elif livello == "INFO":
                    info.append(riga)
    
    # Mostra statistiche
    print(f"\n📊 Statistiche Log:")
    print("=" * 50)
    totale = sum(conteggio.values())
    
    for livello in ["INFO", "WARNING", "ERROR"]:
        count = conteggio[livello]
        percentuale = (count / totale * 100) if totale > 0 else 0
        
        # Emoji per livello
        emoji = {"INFO": "ℹ️", "WARNING": "⚠️", "ERROR": "❌"}
        
        print(f"{emoji[livello]}  {livello:8} : {count:3} messaggi ({percentuale:5.1f}%)")
    
    print("=" * 50)
    print(f"📈 Totale messaggi: {totale}\n")
    
    # Salva gli errori in un file separato
    if errori:
        print(f"💾 Salvataggio {len(errori)} errori in errori.log...")
        Path("errori.log").write_text("".join(errori), encoding="utf-8")
        print("✅ File errori.log creato\n")
        
        # Mostra gli errori
        print("❌ Errori trovati:")
        print("-" * 50)
        for i, errore in enumerate(errori, 1):
            # Estrai il messaggio di errore (dopo il livello)
            parti = errore.split(maxsplit=3)
            if len(parti) >= 4:
                timestamp = f"{parti[0]} {parti[1]}"
                messaggio = parti[3].strip()
                print(f"{i}. [{timestamp}] {messaggio}")
        print("-" * 50)
    else:
        print("✅ Nessun errore trovato nel log!")
    
    # Salva anche warnings se presenti
    if warnings:
        print(f"\n⚠️  Trovati {len(warnings)} warning - salvati in warnings.log")
        Path("warnings.log").write_text("".join(warnings), encoding="utf-8")
    
    return conteggio, errori


def main():
    """Funzione principale."""
    print("=" * 60)
    print("ESERCIZIO 2: ANALISI LOG DI SISTEMA")
    print("=" * 60)
    print()
    
    # Crea log di test se non esiste
    if not Path("server.log").exists():
        crea_log_test()
    
    # Esegui l'analisi
    conteggio, errori = analizza_log()
    
    print("\n" + "=" * 60)
    print("ANALISI COMPLETATA")
    print("=" * 60)
    
    # Cleanup opzionale (commenta se vuoi mantenere i file)
    # Path("server.log").unlink()
    # Path("errori.log").unlink()
    # if Path("warnings.log").exists():
    #     Path("warnings.log").unlink()


if __name__ == "__main__":
    main()
