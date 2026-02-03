"""
Esercizio 3: API e Salvataggio

Scenario: Scaricare dati da un'API pubblica e salvarli.

Obiettivo:
1. Scaricare la lista utenti da https://jsonplaceholder.typicode.com/users
2. Estrarre nome, email e città
3. Salvare in CSV
"""

import requests
import pandas as pd
from pathlib import Path


def scarica_utenti_api():
    """Scarica gli utenti dall'API JSONPlaceholder."""
    
    url = "https://jsonplaceholder.typicode.com/users"
    
    print(f"🌐 Connessione a: {url}")
    print("⏳ Download in corso...\n")
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.ok:
            print(f"✅ Risposta ricevuta (Status: {response.status_code})")
            utenti = response.json()
            print(f"📊 Utenti scaricati: {len(utenti)}\n")
            return utenti
        else:
            print(f"❌ Errore HTTP: {response.status_code}")
            return None
    
    except requests.exceptions.Timeout:
        print("❌ Errore: Timeout della connessione")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Errore di rete: {e}")
        return None


def estrai_dati(utenti):
    """Estrae nome, email e città da ogni utente."""
    
    print("🔍 Estrazione dati rilevanti...")
    
    dati_estratti = []
    
    for u in utenti:
        dati_estratti.append({
            "nome": u["name"],
            "email": u["email"],
            "città": u["address"]["city"]
        })
    
    print(f"✅ Estratti {len(dati_estratti)} record\n")
    
    return dati_estratti


def salva_csv(dati):
    """Salva i dati in un file CSV usando Pandas."""
    
    print("💾 Creazione DataFrame...")
    df = pd.DataFrame(dati)
    
    # Mostra anteprima
    print("\n📋 Anteprima dati (prime 5 righe):")
    print("=" * 70)
    print(df.head().to_string(index=False))
    print("=" * 70)
    
    # Statistiche
    print(f"\n📊 Statistiche:")
    print(f"   Totale utenti: {len(df)}")
    print(f"   Città uniche: {df['città'].nunique()}")
    print(f"\n🏙️  Distribuzione per città:")
    citta_count = df['città'].value_counts()
    for citta, count in citta_count.items():
        print(f"   {citta}: {count} utenti")
    
    # Salva CSV
    filename = "utenti.csv"
    print(f"\n💾 Salvataggio in {filename}...")
    df.to_csv(filename, index=False, encoding="utf-8")
    
    # Verifica dimensione file
    file_size = Path(filename).stat().st_size
    print(f"✅ File salvato ({file_size} bytes)\n")
    
    return df


def verifica_csv():
    """Verifica che il CSV sia stato creato correttamente."""
    
    filename = "utenti.csv"
    
    if not Path(filename).exists():
        print(f"❌ File {filename} non trovato!")
        return False
    
    print(f"🔍 Verifica integrità {filename}...")
    
    # Ricarica il CSV
    df_verificato = pd.read_csv(filename)
    
    print(f"✅ CSV caricato correttamente")
    print(f"   Righe: {len(df_verificato)}")
    print(f"   Colonne: {list(df_verificato.columns)}")
    
    return True


def main():
    """Funzione principale."""
    print("=" * 70)
    print("ESERCIZIO 3: API E SALVATAGGIO")
    print("=" * 70)
    print()
    
    # 1. Scarica dati dall'API
    utenti = scarica_utenti_api()
    
    if utenti is None:
        print("\n❌ Impossibile procedere senza dati")
        return
    
    # 2. Estrai campi rilevanti
    dati_estratti = estrai_dati(utenti)
    
    # 3. Salva in CSV
    df = salva_csv(dati_estratti)
    
    # Verifica
    verifica_csv()
    
    print("\n" + "=" * 70)
    print("OPERAZIONE COMPLETATA CON SUCCESSO")
    print("=" * 70)
    print(f"\n📄 File creato: utenti.csv")
    print(f"📊 Record salvati: {len(df)}")
    
    # Cleanup opzionale (commenta se vuoi mantenere il file)
    # Path("utenti.csv").unlink()


if __name__ == "__main__":
    main()
