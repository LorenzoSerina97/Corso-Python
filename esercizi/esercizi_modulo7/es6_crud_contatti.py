"""
Esercizio 6: CRUD Rubrica Contatti

Obiettivo:
Implementare un CRUD completo (Create, Read, Update, Delete)
per una rubrica contatti con FastAPI e Pydantic.

Concetti chiave:
- POST (Create) con status code 201
- GET (Read) lista e singolo
- PUT (Update) parziale con exclude_unset
- DELETE con status code 204
- Modelli separati per input (Create/Update) e output
- HTTPException per gestione errori
- Query parameter per ricerca
- Endpoint count e ordinamento

Come eseguire:
    uvicorn es6_crud_contatti:app --reload

Come testare:
    http://127.0.0.1:8000/docs  (Swagger UI - consigliato!)

Oppure con curl:
    # Crea contatto
    curl -X POST http://127.0.0.1:8000/contatti \
      -H "Content-Type: application/json" \
      -d '{"nome": "Mario", "telefono": "333-1234567"}'

    # Lista tutti
    curl http://127.0.0.1:8000/contatti

    # Ricerca
    curl http://127.0.0.1:8000/contatti?q=mario

    # Dettaglio
    curl http://127.0.0.1:8000/contatti/1

    # Aggiorna
    curl -X PUT http://127.0.0.1:8000/contatti/1 \
      -H "Content-Type: application/json" \
      -d '{"telefono": "333-9999999"}'

    # Elimina
    curl -X DELETE http://127.0.0.1:8000/contatti/1
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Esercizio 6 - CRUD Rubrica Contatti",
    description="API completa con Create, Read, Update, Delete"
)


# === MODELLI ===

# Modello per creare un contatto (input - senza ID)
class ContattoCreate(BaseModel):
    """Dati per creare un nuovo contatto. L'ID viene generato dal server."""
    nome: str
    telefono: str
    email: Optional[str] = None


# Modello per aggiornare un contatto (tutti i campi opzionali)
class ContattoUpdate(BaseModel):
    """Dati per aggiornare un contatto. Solo i campi inviati vengono modificati."""
    nome: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None


# Modello completo con ID (output)
class Contatto(BaseModel):
    """Modello completo di un contatto, include l'ID generato dal server."""
    id: int
    nome: str
    telefono: str
    email: Optional[str] = None


# === "DATABASE" IN MEMORIA ===
db_contatti: dict[int, Contatto] = {}
contatto_counter = 0


# === HELPER ===
def get_contatto_or_404(contatto_id: int) -> Contatto:
    """Restituisce il contatto o lancia 404 se non esiste."""
    if contatto_id not in db_contatti:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Contatto con id {contatto_id} non trovato"
        )
    return db_contatti[contatto_id]


# === ENDPOINT CRUD ===

# ATTENZIONE: /contatti/count DEVE stare PRIMA di /contatti/{contatto_id}
# altrimenti FastAPI interpreta "count" come un ID!

# Conteggio contatti
@app.get("/contatti/count")
def conta_contatti():
    """Restituisce il numero totale di contatti nella rubrica."""
    return {"totale": len(db_contatti)}


# CREATE - POST /contatti
@app.post("/contatti", response_model=Contatto,
          status_code=status.HTTP_201_CREATED)
def crea_contatto(dati: ContattoCreate):
    """
    Crea un nuovo contatto nella rubrica.

    - Genera automaticamente un ID univoco
    - Restituisce il contatto creato con status 201
    """
    global contatto_counter
    contatto_counter += 1
    nuovo = Contatto(
        id=contatto_counter,
        nome=dati.nome,
        telefono=dati.telefono,
        email=dati.email
    )
    db_contatti[contatto_counter] = nuovo
    return nuovo


# READ ALL - GET /contatti (con ricerca opzionale)
@app.get("/contatti", response_model=List[Contatto])
def lista_contatti(q: Optional[str] = None):
    """
    Lista tutti i contatti, con ricerca opzionale per nome.

    - q: stringa di ricerca (case-insensitive)
    - Senza parametro q, restituisce tutti i contatti
    """
    contatti = list(db_contatti.values())

    # Filtra per nome se query parameter "q" è specificato
    if q:
        contatti = [
            c for c in contatti
            if q.lower() in c.nome.lower()
        ]

    return contatti


# READ ONE - GET /contatti/{id}
@app.get("/contatti/{contatto_id}", response_model=Contatto)
def get_contatto(contatto_id: int):
    """Restituisce i dettagli di un singolo contatto."""
    return get_contatto_or_404(contatto_id)


# UPDATE - PUT /contatti/{id}
@app.put("/contatti/{contatto_id}", response_model=Contatto)
def aggiorna_contatto(contatto_id: int, dati: ContattoUpdate):
    """
    Aggiorna un contatto esistente (update parziale).

    - Solo i campi effettivamente inviati vengono modificati
    - I campi non inviati restano invariati
    - Esempio: {"telefono": "333-9999"} cambia solo il telefono
    """
    contatto = get_contatto_or_404(contatto_id)

    # Aggiorna solo i campi forniti (exclude_unset=True)
    update_data = dati.model_dump(exclude_unset=True)
    for campo, valore in update_data.items():
        setattr(contatto, campo, valore)

    return contatto


# DELETE - DELETE /contatti/{id}
@app.delete("/contatti/{contatto_id}",
            status_code=status.HTTP_204_NO_CONTENT)
def elimina_contatto(contatto_id: int):
    """
    Elimina un contatto dalla rubrica.

    - Restituisce status 204 (No Content) in caso di successo
    - Restituisce 404 se il contatto non esiste
    """
    get_contatto_or_404(contatto_id)
    del db_contatti[contatto_id]
    return None


# === Messaggio di avvio ===
if __name__ == "__main__":
    print("=" * 60)
    print("ESERCIZIO 6: CRUD Rubrica Contatti")
    print("=" * 60)
    print()
    print("▶️  Per avviare il server, esegui:")
    print("   uvicorn es6_crud_contatti:app --reload")
    print()
    print("🧪 Endpoint CRUD disponibili:")
    print("   POST   /contatti          → Crea contatto (201)")
    print("   GET    /contatti          → Lista tutti")
    print("   GET    /contatti?q=mario  → Ricerca per nome")
    print("   GET    /contatti/count    → Conteggio totale")
    print("   GET    /contatti/{id}     → Dettaglio singolo")
    print("   PUT    /contatti/{id}     → Aggiorna (parziale)")
    print("   DELETE /contatti/{id}     → Elimina (204)")
    print()
    print("💡 Usa Swagger UI per testare: http://127.0.0.1:8000/docs")
    print()
    print("📝 Flusso di test consigliato:")
    print('   1. POST /contatti → {"nome":"Mario","telefono":"333-111"}')
    print('   2. POST /contatti → {"nome":"Luigi","telefono":"333-222"}')
    print("   3. GET  /contatti → Vedi entrambi")
    print("   4. GET  /contatti?q=mario → Solo Mario")
    print("   5. GET  /contatti/count → {\"totale\": 2}")
    print('   6. PUT  /contatti/1 → {"email":"mario@email.it"}')
    print("   7. GET  /contatti/1 → Verifica email aggiunta")
    print("   8. DELETE /contatti/1 → Elimina Mario")
    print("   9. GET  /contatti → Solo Luigi rimasto")
    print()
    print("Concetti applicati:")
    print("✓ Modelli separati: Create (input), Update (parziale), Contatto (output)")
    print("✓ Status code: 201 (Created), 204 (No Content), 404 (Not Found)")
    print("✓ response_model per documentazione automatica")
    print("✓ model_dump(exclude_unset=True) per update parziale")
    print("✓ setattr() per aggiornamento dinamico attributi")
    print("✓ Ricerca case-insensitive con .lower()")
    print("✓ Ordine endpoint: /count prima di /{id}")
