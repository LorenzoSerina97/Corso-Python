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
    """Analizza il file di log secondo la soluzione delle slide."""
    
    log_path = Path("server.log")
    conteggio = Counter()
    errori = []
    
    print("📂 Lettura file server.log...\n")
    
    with open(log_path, "r", encoding="utf-8") as f:
        for riga in f:
            parti = riga.split()
            if len(parti) >= 3:
                livello = parti[2]  # INFO, ERROR, WARNING
                conteggio[livello] += 1
                if livello == "ERROR":
                    errori.append(riga)
    
    print("Conteggio per livello:")
    for livello, count in conteggio.items():
        print(f"  {livello}: {count}")
    
    # Salva errori
    print(f"\n💾 Salvati {len(errori)} errori in errori.log")
    Path("errori.log").write_text("".join(errori), encoding="utf-8")
    
    # Mostra gli errori
    if errori:
        print("\n❌ Errori trovati:")
        print("-" * 70)
        for errore in errori:
            print(f"  {errore.strip()}")
        print("-" * 70)
    
    return conteggio, errori


def main():
    """Funzione principale."""
    print("=" * 70)
    print("ESERCIZIO 2: ANALISI LOG DI SISTEMA")
    print("=" * 70)
    print()
    
    # Crea log di test se non esiste
    if not Path("server.log").exists():
        crea_log_test()
    
    # Esegui l'analisi
    conteggio, errori = analizza_log()
    
    print("\n" + "=" * 70)
    print("ANALISI COMPLETATA")
    print("=" * 70)
    
    # Cleanup opzionale (commenta se vuoi mantenere i file)
    # Path("server.log").unlink()
    # Path("errori.log").unlink()


if __name__ == "__main__":
    main()
