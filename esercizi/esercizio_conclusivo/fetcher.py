import requests
import json

class MeteoClient:
    """Classe per scaricare i dati meteo da Open-Meteo."""
    def __init__(self):
        # Utilizziamo l'API pubblica di Open-Meteo
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def ottieni_previsioni(self, lat: float, lon: float) -> dict:
        """Scarica i dati meteo e li salva in un file JSON."""
        # Parametri della richiesta (Query Parameters)
        parametri = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m",
            "timezone": "auto"
        }
        try:
            # Effettuiamo la GET request
            risposta = requests.get(self.base_url, params=parametri, timeout=10)   
            # Genera un'eccezione se lo status code indica un errore (es. 404, 500)
            risposta.raise_for_status() 
            # Estraiamo il JSON
            dati = risposta.json()
            # File I/O: Salviamo i dati grezzi in locale
            with open("dati_grezzi.json", "w", encoding="utf-8") as file:
                json.dump(dati, file, indent=4)
            print("✅ Dati meteo scaricati e salvati in 'dati_grezzi.json'")
            return dati
        except requests.exceptions.RequestException as errore_http:
            print(f"❌ Errore di connessione o HTTP: {errore_http}")
            raise
        except Exception as errore_generico:
            print(f"❌ Errore inaspettato: {errore_generico}")
            raise