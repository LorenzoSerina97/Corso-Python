import pandas as pd
import json

def analizza_e_salva_dati():
    """Legge il JSON grezzo, pulisce i dati, li raggruppa per giorno e salva in CSV."""
    try:
        # 1. Leggiamo il file JSON salvato dal fetcher
        with open("dati_grezzi.json", "r", encoding="utf-8") as file:
            dati_json = json.load(file)
        
        # Estraiamo orari e temperature dal dizionario
        orari = dati_json["hourly"]["time"]
        temperature_celsius = dati_json["hourly"]["temperature_2m"]
        
        # BONUS: List Comprehension per convertire in Fahrenheit (se temp non è None)
        # Formula: (C * 9/5) + 32
        temperature_f = [
            (temp * 9/5) + 32 if temp is not None else None 
            for temp in temperature_celsius
        ]
        
        # 2. Creazione del DataFrame Pandas
        df = pd.DataFrame({
            "data_ora": orari,
            "temperatura_F": temperature_f
        })
        
        # 3. Pulizia Dati: Gestione dei NaN sostituendoli con la media globale
        media_globale = df["temperatura_F"].mean()
        df["temperatura_F"] = df["temperatura_F"].fillna(media_globale)
        
        # 4. Manipolazione: Creiamo una colonna solo per il giorno (formato "YYYY-MM-DD")
        df['giorno'] = df['data_ora'].str.split('T').str[0]
        
        # 5. Analisi & GroupBy: Raggruppiamo per giorno
        df_riassunto = df.groupby('giorno').agg(
            temp_media=('temperatura_F', 'mean'),
            temp_max=('temperatura_F', 'max'),
            temp_min=('temperatura_F', 'min')
        ).reset_index()
        
        # Arrotondiamo a due decimali
        df_riassunto = df_riassunto.round(2)
        
        # 6. Automazione: Esportiamo in CSV
        df_riassunto.to_csv("report_meteo.csv", index=False)
        print("✅ Analisi completata. Report salvato in 'report_meteo.csv'")
        
    except FileNotFoundError:
        print("❌ Errore: file 'dati_grezzi.json' non trovato. Assicurati di scaricare i dati prima.")
        raise