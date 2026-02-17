"""
Esercizio 4: Query Parameters

Obiettivo:
Usare query parameters per filtrare, paginare risultati
e combinarli con path parameters.

Concetti chiave:
- Query parameters (dopo il ? nell'URL)
- Parametri opzionali con Optional e default
- Filtri in cascata (categoria, prezzo)
- Paginazione con skip e limit

Come eseguire:
    uvicorn es4_query_parameters:app --reload

Come testare:
    http://127.0.0.1:8000/prodotti
    http://127.0.0.1:8000/prodotti?categoria=accessori
    http://127.0.0.1:8000/prodotti?categoria=accessori&prezzo_max=80
"""

from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Esercizio 4 - Query Parameters",
    description="Filtri, paginazione e combinazione di parametri"
)

# === Dati statici ===

prodotti = [
    {"id": 1, "nome": "Laptop", "prezzo": 999, "categoria": "elettronica"},
    {"id": 2, "nome": "Mouse", "prezzo": 25, "categoria": "accessori"},
    {"id": 3, "nome": "Monitor", "prezzo": 299, "categoria": "elettronica"},
    {"id": 4, "nome": "Tastiera", "prezzo": 75, "categoria": "accessori"},
    {"id": 5, "nome": "Webcam", "prezzo": 89, "categoria": "accessori"},
]


# === ESERCIZIO 3.2: Query Parameters ===

@app.get("/prodotti")
def list_prodotti(
    categoria: Optional[str] = None,    # 1. Filtro per categoria
    prezzo_max: Optional[float] = None, # 2. Filtro per prezzo massimo
    skip: int = 0,                      # 3. Paginazione - offset
    limit: int = 10                     # 3. Paginazione - limite
):
    """
    Lista prodotti con filtri opzionali e paginazione.

    - categoria: filtra per categoria (es. "accessori", "elettronica")
    - prezzo_max: mostra solo prodotti con prezzo <= valore
    - skip: numero di risultati da saltare (default 0)
    - limit: numero massimo di risultati (default 10)
    """
    risultati = prodotti

    # Filtra per categoria se specificata
    if categoria:
        risultati = [p for p in risultati if p["categoria"] == categoria]

    # Filtra per prezzo massimo se specificato
    if prezzo_max is not None:
        risultati = [p for p in risultati if p["prezzo"] <= prezzo_max]

    # Applica paginazione
    risultati_paginati = risultati[skip : skip + limit]

    return {
        "totale": len(risultati),
        "prodotti": risultati_paginati
    }

# === Messaggio di avvio ===
if __name__ == "__main__":
    print("=" * 60)
    print("ESERCIZIO 4: Query Parameters")
    print("=" * 60)
    print()
    print("▶️  Per avviare il server, esegui:")
    print("   uvicorn es4_query_parameters:app --reload")
    print()
    print("🧪 Endpoint disponibili:")
    print("   GET /prodotti                → Tutti i prodotti")
    print("   GET /prodotti?categoria=...  → Filtro per categoria")
    print("   GET /prodotti?prezzo_max=... → Filtro per prezzo")
    print("   GET /prodotti?skip=0&limit=2 → Paginazione")
    print()
    print("📝 Prova questi URL:")
    print("   /prodotti?categoria=accessori&prezzo_max=80")
    print("   → Mouse (25€) e Tastiera (75€)")
    print()
    print("Concetti applicati:")
    print("✓ Query params con default → diventano opzionali")
    print("✓ Optional[str] = None per parametri facoltativi")
    print("✓ Filtri in cascata (categoria → prezzo)")
    print("✓ Paginazione con skip/limit e slicing")
