"""
Esercizio 5: Pydantic - Validazione Dati

Obiettivo:
Definire modelli Pydantic per validare automaticamente i dati
in ingresso, usando BaseModel, Field e modelli annidati.

Concetti chiave:
- BaseModel per definire la "forma" dei dati
- Campi obbligatori vs opzionali (Optional)
- Validazione con Field (min_length, gt, ge, max_length)
- Modelli annidati e List di modelli
- Endpoint POST con body JSON validato

Come eseguire:
    uvicorn es5_pydantic:app --reload

Come testare (Swagger UI è il modo più comodo!):
    http://127.0.0.1:8000/docs

Oppure con curl:
    curl -X POST http://127.0.0.1:8000/contatti \
      -H "Content-Type: application/json" \
      -d '{"nome": "Mario", "email": "mario@email.it"}'
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(
    title="Esercizio 5 - Pydantic",
    description="Validazione dati con Pydantic: BaseModel, Field, modelli annidati"
)


# === ESERCIZIO 4.1: Modelli Pydantic Base ===

class Contatto(BaseModel):
    """Modello per un contatto della rubrica."""
    nome: str                           # Obbligatorio
    email: str                          # Obbligatorio
    telefono: Optional[str] = None      # Opzionale
    nota: Optional[str] = None          # Opzionale


@app.post("/contatti")
def crea_contatto(contatto: Contatto):
    """
    Crea un nuovo contatto.

    FastAPI valida automaticamente il JSON in ingresso
    usando il modello Pydantic. Se manca un campo obbligatorio
    (nome o email), restituisce errore 422.
    """
    return {
        "messaggio": "Contatto creato",
        "contatto": contatto.model_dump()
    }


# === ESERCIZIO 4.2: Validazione con Field ===

class Prodotto(BaseModel):
    """Modello per un prodotto con validazione avanzata."""
    nome: str = Field(
        min_length=2,
        max_length=100,
        description="Nome del prodotto (2-100 caratteri)"
    )
    prezzo: float = Field(
        gt=0,
        description="Prezzo in euro (deve essere positivo)"
    )
    quantita: int = Field(
        ge=0,
        description="Quantità in magazzino (>= 0)"
    )
    descrizione: Optional[str] = Field(
        None,
        max_length=500,
        description="Descrizione opzionale (max 500 caratteri)"
    )


@app.post("/prodotti")
def crea_prodotto(prodotto: Prodotto):
    """
    Crea un nuovo prodotto con validazione.

    Pydantic valida automaticamente:
    - nome: minimo 2, massimo 100 caratteri
    - prezzo: deve essere > 0
    - quantita: deve essere >= 0
    - descrizione: opzionale, max 500 caratteri

    Prova a inviare valori non validi per vedere gli errori 422!
    """
    return {
        "prodotto": prodotto.model_dump(),
        "totale_valore": round(prodotto.prezzo * prodotto.quantita, 2)
    }


# === ESERCIZIO 4.3: Modelli Annidati ===

class Indirizzo(BaseModel):
    """Modello per un indirizzo di spedizione."""
    via: str
    citta: str
    cap: str


class Riga(BaseModel):
    """Modello per una singola riga dell'ordine."""
    prodotto: str
    quantita: int = Field(ge=1, description="Almeno 1")
    prezzo_unitario: float = Field(gt=0, description="Prezzo > 0")


class Ordine(BaseModel):
    """
    Modello per un ordine completo con modelli annidati.

    - indirizzo_spedizione: un oggetto Indirizzo (annidato)
    - righe: una lista di oggetti Riga (lista di modelli)
    """
    cliente: str
    indirizzo_spedizione: Indirizzo          # Modello annidato
    righe: List[Riga]                        # Lista di modelli


@app.post("/ordini")
def crea_ordine(ordine: Ordine):
    """
    Crea un nuovo ordine con struttura dati complessa.

    Pydantic valida ricorsivamente l'intera struttura JSON,
    inclusi i modelli annidati (Indirizzo) e le liste (Riga).

    Esempio JSON da inviare:
    {
        "cliente": "Mario Rossi",
        "indirizzo_spedizione": {
            "via": "Via Roma 1",
            "citta": "Milano",
            "cap": "20100"
        },
        "righe": [
            {"prodotto": "Laptop", "quantita": 1, "prezzo_unitario": 999.99},
            {"prodotto": "Mouse", "quantita": 2, "prezzo_unitario": 25.00}
        ]
    }
    """
    totale = sum(
        riga.quantita * riga.prezzo_unitario
        for riga in ordine.righe
    )
    return {
        "ordine": ordine.model_dump(),
        "totale": round(totale, 2)
    }


# === Messaggio di avvio ===
if __name__ == "__main__":
    print("=" * 60)
    print("ESERCIZIO 5: Pydantic - Validazione Dati")
    print("=" * 60)
    print()
    print("▶️  Per avviare il server, esegui:")
    print("   uvicorn es5_pydantic:app --reload")
    print()
    print("🧪 Endpoint disponibili:")
    print("   POST /contatti  → Crea contatto (BaseModel base)")
    print("   POST /prodotti  → Crea prodotto (con Field)")
    print("   POST /ordini    → Crea ordine (modelli annidati)")
    print()
    print("💡 Consiglio: usa Swagger UI per testare facilmente!")
    print("   http://127.0.0.1:8000/docs")
    print()
    print("📝 Prova questi test:")
    print('   ✅ POST /contatti → {"nome": "Mario", "email": "m@e.it"}')
    print('   ❌ POST /contatti → {"email": "m@e.it"}  (manca nome → 422)')
    print('   ❌ POST /prodotti → {"nome": "L", "prezzo": -5, "quantita": 1}')
    print("      → 422: nome troppo corto E prezzo negativo")
    print()
    print("Concetti applicati:")
    print("✓ BaseModel con campi obbligatori e Optional")
    print("✓ Field(gt, ge, min_length, max_length) per vincoli")
    print("✓ Modelli annidati (Indirizzo dentro Ordine)")
    print("✓ List[Riga] per liste di modelli validati")
    print("✓ model_dump() per convertire in dizionario")
