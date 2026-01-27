"""
Esercizio 2: Gerarchia Veicoli
Modulo 4 - Laboratorio Pratico

Obiettivo: Creare una gerarchia di classi per veicoli usando ereditarietà.
- Classe base Veicolo con attributi comuni
- Classi derivate Auto e Moto con attributi specifici
- Metodi per accendere/spegnere i veicoli
"""


class Veicolo:
    """Classe base per tutti i veicoli."""
    
    def __init__(self, marca, modello, anno):
        """
        Inizializza un veicolo.
        
        Args:
            marca: Marca del veicolo
            modello: Modello del veicolo
            anno: Anno di immatricolazione
        """
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.acceso = False
        self.km_percorsi = 0
    
    def accendi(self):
        """Accende il veicolo."""
        if self.acceso:
            print(f"{self.marca} {self.modello} è già acceso!")
        else:
            self.acceso = True
            print(f"🔑 {self.marca} {self.modello} acceso")
    
    def spegni(self):
        """Spegne il veicolo."""
        if not self.acceso:
            print(f"{self.marca} {self.modello} è già spento!")
        else:
            self.acceso = False
            print(f"🔒 {self.marca} {self.modello} spento")
    
    def guida(self, km):
        """Simula la guida per un certo numero di km."""
        if not self.acceso:
            print(f"⚠️ Devi prima accendere {self.marca} {self.modello}!")
            return
        self.km_percorsi += km
        print(f"🚗 Hai percorso {km} km con {self.marca} {self.modello}")
    
    def info(self):
        """Restituisce le informazioni del veicolo."""
        stato = "acceso" if self.acceso else "spento"
        return f"{self.marca} {self.modello} ({self.anno}) - {stato} - {self.km_percorsi} km"
    
    def __str__(self):
        return self.info()
    
    def __repr__(self):
        return f"Veicolo('{self.marca}', '{self.modello}', {self.anno})"


class Auto(Veicolo):
    """Rappresenta un'automobile."""
    
    def __init__(self, marca, modello, anno, num_porte, tipo_carburante="benzina"):
        """
        Inizializza un'automobile.
        
        Args:
            marca: Marca dell'auto
            modello: Modello dell'auto
            anno: Anno di immatricolazione
            num_porte: Numero di porte
            tipo_carburante: Tipo di carburante (default: benzina)
        """
        super().__init__(marca, modello, anno)
        self.num_porte = num_porte
        self.tipo_carburante = tipo_carburante
    
    def info(self):
        """Restituisce le informazioni dell'auto."""
        base = super().info()
        return f"{base} - {self.num_porte} porte - {self.tipo_carburante}"
    
    def apri_bagagliaio(self):
        """Apre il bagagliaio."""
        print(f"📦 Bagagliaio di {self.marca} {self.modello} aperto")
    
    def __repr__(self):
        return f"Auto('{self.marca}', '{self.modello}', {self.anno}, {self.num_porte})"


class Moto(Veicolo):
    """Rappresenta una motocicletta."""
    
    def __init__(self, marca, modello, anno, cilindrata):
        """
        Inizializza una moto.
        
        Args:
            marca: Marca della moto
            modello: Modello della moto
            anno: Anno di immatricolazione
            cilindrata: Cilindrata in cc
        """
        super().__init__(marca, modello, anno)
        self.cilindrata = cilindrata
    
    def info(self):
        """Restituisce le informazioni della moto."""
        base = super().info()
        return f"{base} - {self.cilindrata}cc"
    
    def impenna(self):
        """Fa un'impennata (solo se accesa)."""
        if not self.acceso:
            print(f"⚠️ Accendi prima la moto!")
        else:
            print(f"🏍️ {self.marca} {self.modello} sta impennando!")
    
    def __repr__(self):
        return f"Moto('{self.marca}', '{self.modello}', {self.anno}, {self.cilindrata})"


class Camion(Veicolo):
    """Rappresenta un camion."""
    
    def __init__(self, marca, modello, anno, capacita_carico):
        """
        Inizializza un camion.
        
        Args:
            marca: Marca del camion
            modello: Modello del camion
            anno: Anno di immatricolazione
            capacita_carico: Capacità di carico in tonnellate
        """
        super().__init__(marca, modello, anno)
        self.capacita_carico = capacita_carico
        self.carico_attuale = 0
    
    def carica(self, peso):
        """Carica merce sul camion."""
        if self.carico_attuale + peso > self.capacita_carico:
            print(f"⚠️ Capacità massima superata! Max: {self.capacita_carico}t")
        else:
            self.carico_attuale += peso
            print(f"📦 Caricato {peso}t. Carico attuale: {self.carico_attuale}t")
    
    def scarica(self):
        """Scarica tutto il carico."""
        print(f"📤 Scaricato {self.carico_attuale}t")
        self.carico_attuale = 0
    
    def info(self):
        """Restituisce le informazioni del camion."""
        base = super().info()
        return f"{base} - Carico: {self.carico_attuale}/{self.capacita_carico}t"
    
    def __repr__(self):
        return f"Camion('{self.marca}', '{self.modello}', {self.anno}, {self.capacita_carico})"


# ==================== TEST ====================
if __name__ == "__main__":
    print("=" * 50)
    print("TEST GERARCHIA VEICOLI")
    print("=" * 50)
    
    # Creazione veicoli
    auto = Auto("Fiat", "Panda", 2020, 5, "benzina")
    moto = Moto("Ducati", "Monster", 2021, 821)
    camion = Camion("Iveco", "Daily", 2019, 3.5)
    
    print("\n--- Veicoli creati ---")
    print(f"  {auto}")
    print(f"  {moto}")
    print(f"  {camion}")
    
    # Test Auto
    print("\n--- Test Auto ---")
    auto.accendi()
    auto.guida(50)
    auto.apri_bagagliaio()
    auto.spegni()
    
    # Test Moto
    print("\n--- Test Moto ---")
    moto.impenna()  # Non funziona, è spenta
    moto.accendi()
    moto.impenna()  # Ora funziona
    moto.guida(30)
    
    # Test Camion
    print("\n--- Test Camion ---")
    camion.accendi()
    camion.carica(2)
    camion.carica(1)
    camion.carica(1)  # Supera la capacità
    camion.guida(100)
    camion.scarica()
    
    # Polimorfismo: lista di veicoli
    print("\n--- Polimorfismo ---")
    veicoli = [auto, moto, camion]
    print("\nStato finale di tutti i veicoli:")
    for v in veicoli:
        print(f"  {v}")
    
    print("\n✅ Tutti i test completati con successo!")
