"""
Esercizio 3: Path Parameters

Obiettivo:
Creare endpoint con parametri dinamici nel path dell'URL
per accedere a risorse specifiche.

Concetti chiave:
- Path parameters con {parametro} nell'URL
- Type hints per validazione automatica (int, str)
- Gestione risorse non trovate con HTTPException (404)

Come eseguire:
    uvicorn es3_path_parameters:app --reload

Come testare:
    http://127.0.0.1:8000/studenti/1     → Dati di Alice
    http://127.0.0.1:8000/studenti/99    → Errore 404
    http://127.0.0.1:8000/studenti/abc   → Errore 422 (non è int)
    http://127.0.0.1:8000/saluta/Mario   → Saluto personalizzato
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Esercizio 3 - Path Parameters",
    description="Endpoint con parametri dinamici nel path"
)

# === Dati statici ===
studenti = {
    1: {"nome": "Alice", "voto": 28},
    2: {"nome": "Bob", "voto": 25},
    3: {"nome": "Charlie", "voto": 30},
}


# === ESERCIZIO 3.1: Path Parameters ===

# 1. Endpoint con path parameter per ID studente
@app.get("/studenti/{studente_id}")
def get_studente(studente_id: int):
    """
    Restituisce i dati di uno studente dato il suo ID.

    - studente_id è validato automaticamente come int
    - Se l'ID non esiste, restituisce errore 404
    """
    # 2. Controllo se l'ID esiste
    if studente_id not in studenti:
        raise HTTPException(
            status_code=404,
            detail="Studente non trovato"
        )
    return studenti[studente_id]


# 3. Endpoint saluto con path parameter stringa
@app.get("/saluta/{nome}")
def saluta(nome: str):
    """Restituisce un messaggio di saluto personalizzato."""
    return {"messaggio": f"Ciao, {nome}!"}


# === Messaggio di avvio ===
if __name__ == "__main__":
    print("=" * 60)
    print("ESERCIZIO 3: Path Parameters")
    print("=" * 60)
    print()
    print("▶️  Per avviare il server, esegui:")
    print("   uvicorn es3_path_parameters:app --reload")
    print()
    print("🧪 Endpoint disponibili:")
    print("   GET /studenti/{id}  → Dati dello studente")
    print("   GET /saluta/{nome}  → Saluto personalizzato")
    print()
    print("📝 Prova questi URL:")
    print('   /studenti/1  → {"nome": "Alice", "voto": 28}')
    print('   /studenti/99 → 404 "Studente non trovato"')
    print('   /studenti/abc→ 422 Errore validazione (non è int)')
    print('   /saluta/Mario→ {"messaggio": "Ciao, Mario!"}')
    print()
    print("Concetti applicati:")
    print("✓ Path parameter {studente_id} → parametro funzione")
    print("✓ Type hint : int → validazione automatica (422 se sbagliato)")
    print("✓ HTTPException(status_code=404) per risorse non trovate")
