from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import os

# Importiamo i moduli scritti da noi
from fetcher import MeteoClient
from analyzer import analizza_e_salva_dati

# Inizializzazione applicazione
app = FastAPI(title="Meteo Data Hub & API")

# Modello Pydantic per validare il Body della POST
class Coordinate(BaseModel):
    latitudine: float
    longitudine: float

# --- ROUTING E CRUD ---
@app.get("/")
def root():
    """Endpoint di benvenuto sulla root."""
    return {
        "messaggio": "Benvenuto nel Meteo Data Hub!", 
        "istruzioni": "Vai all'indirizzo /docs per esplorare e testare le API."
    }
@app.post("/aggiorna-dati")
def aggiorna_dati(coords: Coordinate):
    """Scarica i nuovi dati per le coordinate fornite e genera il report."""
    client = MeteoClient()
    try:
        # Fase di estrazione
        client.ottieni_previsioni(coords.latitudine, coords.longitudine)
        # Fase di analisi e salvataggio
        analizza_e_salva_dati()
        
        return {"messaggio": "Successo! Dati aggiornati e report generato."}
    except Exception as e:
        # Gestione dell'errore lato Server (HTTP 500)
        raise HTTPException(status_code=500, detail=f"Errore interno: {str(e)}") from e


@app.get("/report-completo")
def get_report_completo():
    """Ritorna tutto il file CSV generato sotto forma di JSON."""
    if not os.path.exists("report_meteo.csv"):
        raise HTTPException(status_code=404, detail="Report inesistente. Chiama /aggiorna-dati prima.")
    
    df = pd.read_csv("report_meteo.csv")
    # Convertiamo il DataFrame in una lista di dizionari, perfetto per il JSON
    return df.to_dict(orient="records")


@app.get("/meteo/{giorno}")
def get_meteo_giorno(giorno: str):
    """
    Ritorna le statistiche meteo per un giorno specifico.
    Formato atteso: YYYY-MM-DD
    """
    if not os.path.exists("report_meteo.csv"):
        raise HTTPException(status_code=404, detail="Report inesistente.")
    
    df = pd.read_csv("report_meteo.csv")
    
    # Filtriamo il DataFrame Pandas per il giorno richiesto
    df_filtrato = df[df['giorno'] == giorno]
    
    # Se il DataFrame filtrato è vuoto, il giorno non esiste
    if df_filtrato.empty:
        raise HTTPException(status_code=404, detail=f"Dati non trovati per il giorno: {giorno}")
    
    return df_filtrato.to_dict(orient="records")[0]