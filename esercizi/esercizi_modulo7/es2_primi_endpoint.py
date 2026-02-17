"""
Esercizio 2: Primi Endpoint FastAPI

Obiettivo:
Creare un'applicazione FastAPI con endpoint GET di base
che restituiscono dati statici in formato JSON.

Concetti chiave:
- Creazione app FastAPI
- Decoratore @app.get() per definire endpoint
- Restituzione automatica di dict/list come JSON
- Avvio server con uvicorn

Come eseguire:
    uvicorn es2_primi_endpoint:app --reload

Come testare:
    Apri nel browser: http://127.0.0.1:8000/
    Oppure: http://127.0.0.1:8000/docs (Swagger UI)
"""

from fastapi import FastAPI

app = FastAPI(
    title="Esercizio 2 - Primi Endpoint",
    description="Il mio primo server FastAPI con endpoint GET"
)

# === Dati statici (simulano un mini-database) ===
menu = [
    {"id": 1, "piatto": "Margherita", "prezzo": 8.0},
    {"id": 2, "piatto": "Diavola", "prezzo": 10.0},
    {"id": 3, "piatto": "Quattro Formaggi", "prezzo": 11.0},
]


# === ESERCIZIO 2.1: Primi Endpoint ===

# 1. Endpoint root
@app.get("/")
def read_root():
    """Restituisce informazioni sull'applicazione."""
    return {"app": "Il Mio Primo Server", "versione": "1.0"}


# 2. Endpoint info
@app.get("/info")
def get_info():
    """Restituisce informazioni sull'autore."""
    return {"autore": "Il tuo nome", "linguaggio": "Python"}


# 3. Endpoint saluto
@app.get("/saluto")
def get_saluto():
    """Restituisce un messaggio di saluto."""
    return {"messaggio": "Ciao dal server FastAPI!"}


# === ESERCIZIO 2.2: Endpoint con Dati Statici ===

# 1. Lista completa del menu
@app.get("/menu")
def get_menu():
    """Restituisce la lista completa del menu."""
    return menu


# 2. Conteggio piatti
@app.get("/menu/count")
def get_menu_count():
    """Restituisce il numero totale di piatti nel menu."""
    return {"totale": len(menu)}


# 3. Prezzo medio
@app.get("/menu/prezzi")
def get_prezzi_medi():
    """Restituisce il prezzo medio dei piatti."""
    prezzi = [piatto["prezzo"] for piatto in menu]
    media = sum(prezzi) / len(prezzi)
    return {"prezzo_medio": round(media, 2)}


# === Messaggio di avvio ===
if __name__ == "__main__":
    print("=" * 60)
    print("ESERCIZIO 2: Primi Endpoint FastAPI")
    print("=" * 60)
    print()
    print("▶️  Per avviare il server, esegui:")
    print("   uvicorn es2_primi_endpoint:app --reload")
    print()
    print("🧪 Endpoint disponibili:")
    print("   http://127.0.0.1:8000/           → Info app")
    print("   http://127.0.0.1:8000/info       → Info autore")
    print("   http://127.0.0.1:8000/saluto     → Messaggio saluto")
    print("   http://127.0.0.1:8000/menu       → Lista menu completa")
    print("   http://127.0.0.1:8000/menu/count → Conteggio piatti")
    print("   http://127.0.0.1:8000/menu/prezzi→ Prezzo medio")
    print("   http://127.0.0.1:8000/docs       → Swagger UI (docs)")
    print()
    print("Concetti applicati:")
    print("✓ Creazione app FastAPI")
    print("✓ Decoratore @app.get() per endpoint GET")
    print("✓ Restituzione dict e list come JSON")
    print("✓ List comprehension per calcoli")
    print("✓ Calcolo media con sum()/len()")
