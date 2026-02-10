"""
Esercizio 3: API e Salvataggio

Scenario: Scaricare dati da un'API pubblica e salvarli.

Obiettivo:
1. Scaricare la lista utenti da https://jsonplaceholder.typicode.com/users
2. Estrarre nome, email e città
3. Salvare in CSV usando il modulo csv
"""

import requests
import csv


def main():
    """Funzione principale."""
    print("=" * 70)
    print("ESERCIZIO 3: API E SALVATAGGIO")
    print("=" * 70)
    print()
    
    # 1. Scarica dati
    url = "https://jsonplaceholder.typicode.com/users"
    
    print(f"🌐 Connessione a: {url}")
    print("⏳ Download in corso...\n")
    
    response = requests.get(url)
    
    if response.ok:
        print(f"✅ Risposta ricevuta (Status: {response.status_code})")
        utenti = response.json()
        print(f"📊 Utenti scaricati: {len(utenti)}\n")
        
        # 2. Estrai campi
        print("🔍 Estrazione dati rilevanti...")
        dati_estratti = []
        for u in utenti:
            dati_estratti.append({
                "nome": u["name"],
                "email": u["email"],
                "città": u["address"]["city"]
            })
        
        print(f"✅ Estratti {len(dati_estratti)} record\n")
        
        # Mostra anteprima
        print("📋 Anteprima dati (primi 3 utenti):")
        print("=" * 70)
        for i, utente in enumerate(dati_estratti[:3], 1):
            print(f"{i}. {utente['nome']:25} | {utente['email']:30} | {utente['città']}")
        print("=" * 70)
        print()
        
        # 3. Salva in CSV
        print("💾 Salvataggio in utenti.csv...")
        with open("utenti.csv", "w", newline="", encoding="utf-8") as f:
            fieldnames = ["nome", "email", "città"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(dati_estratti)
        
        print(f"✅ Salvati {len(dati_estratti)} utenti")
        
        print("\n" + "=" * 70)
        print("OPERAZIONE COMPLETATA CON SUCCESSO")
        print("=" * 70)
        print(f"\n📄 File creato: utenti.csv")
        print(f"📊 Record salvati: {len(dati_estratti)}")
        
    else:
        print(f"❌ Errore: {response.status_code}")
    
    # Cleanup opzionale (commenta se vuoi mantenere il file)
    # from pathlib import Path
    # Path("utenti.csv").unlink()


if __name__ == "__main__":
    main()
