"""
Esercizio 1: Sistema Bancario
Modulo 4 - Laboratorio Pratico

Obiettivo: Creare una classe ContoBancario completa con:
- Attributi: titolare, saldo, storico_operazioni
- Metodi: deposita, preleva, trasferisci
- Gestione errori con eccezioni personalizzate
- Property per saldo (solo lettura)
"""


class SaldoInsufficienteError(Exception):
    """Eccezione per saldo insufficiente."""
    pass


class ImportoNonValidoError(Exception):
    """Eccezione per importo non valido."""
    pass


class ContoBancario:
    """Rappresenta un conto bancario con gestione completa delle operazioni."""
    
    def __init__(self, titolare, saldo_iniziale=0):
        """
        Inizializza un nuovo conto bancario.
        
        Args:
            titolare: Nome del titolare del conto
            saldo_iniziale: Saldo iniziale (default 0)
        """
        if saldo_iniziale < 0:
            raise ValueError("Il saldo iniziale non può essere negativo")
        self.titolare = titolare
        self._saldo = saldo_iniziale
        self.storico = []
        self.storico.append(f"Conto aperto con saldo: {saldo_iniziale}€")
    
    @property
    def saldo(self):
        """Restituisce il saldo corrente (solo lettura)."""
        return self._saldo
    
    def deposita(self, importo):
        """
        Deposita un importo sul conto.
        
        Args:
            importo: Importo da depositare (deve essere positivo)
            
        Raises:
            ImportoNonValidoError: Se l'importo è <= 0
        """
        if importo <= 0:
            raise ImportoNonValidoError("L'importo deve essere positivo!")
        self._saldo += importo
        self.storico.append(f"Deposito: +{importo}€")
        return self._saldo
    
    def preleva(self, importo):
        """
        Preleva un importo dal conto.
        
        Args:
            importo: Importo da prelevare
            
        Raises:
            ImportoNonValidoError: Se l'importo è <= 0
            SaldoInsufficienteError: Se il saldo è insufficiente
        """
        if importo <= 0:
            raise ImportoNonValidoError("L'importo deve essere positivo!")
        if importo > self._saldo:
            raise SaldoInsufficienteError(
                f"Saldo {self._saldo}€ insufficiente per prelevare {importo}€"
            )
        self._saldo -= importo
        self.storico.append(f"Prelievo: -{importo}€")
        return self._saldo
    
    def trasferisci(self, destinatario, importo):
        """
        Trasferisce un importo verso un altro conto.
        
        Args:
            destinatario: ContoBancario destinatario
            importo: Importo da trasferire
            
        Raises:
            ImportoNonValidoError: Se l'importo è <= 0
            SaldoInsufficienteError: Se il saldo è insufficiente
        """
        self.preleva(importo)  # Può sollevare eccezioni
        destinatario.deposita(importo)
        self.storico.append(f"Trasferimento a {destinatario.titolare}: -{importo}€")
        destinatario.storico.append(f"Trasferimento da {self.titolare}: +{importo}€")
    
    def stampa_storico(self):
        """Stampa lo storico delle operazioni."""
        print(f"\n{'='*40}")
        print(f"Storico operazioni - {self.titolare}")
        print(f"{'='*40}")
        for operazione in self.storico:
            print(f"  • {operazione}")
        print(f"{'='*40}")
        print(f"Saldo attuale: {self._saldo}€")
    
    def __str__(self):
        return f"ContoBancario({self.titolare}, saldo={self._saldo}€)"
    
    def __repr__(self):
        return f"ContoBancario('{self.titolare}', {self._saldo})"


# ==================== TEST ====================
if __name__ == "__main__":
    print("=" * 50)
    print("TEST SISTEMA BANCARIO")
    print("=" * 50)
    
    # Creazione conti
    conto_mario = ContoBancario("Mario Rossi", 1000)
    conto_luigi = ContoBancario("Luigi Verdi", 500)
    
    print(f"\nConti creati:")
    print(f"  {conto_mario}")
    print(f"  {conto_luigi}")
    
    # Test deposito
    print("\n--- Test Deposito ---")
    conto_mario.deposita(250)
    print(f"Mario dopo deposito 250€: {conto_mario.saldo}€")
    
    # Test prelievo
    print("\n--- Test Prelievo ---")
    conto_mario.preleva(100)
    print(f"Mario dopo prelievo 100€: {conto_mario.saldo}€")
    
    # Test trasferimento
    print("\n--- Test Trasferimento ---")
    conto_mario.trasferisci(conto_luigi, 300)
    print(f"Mario dopo trasferimento 300€: {conto_mario.saldo}€")
    print(f"Luigi dopo trasferimento 300€: {conto_luigi.saldo}€")
    
    # Test eccezioni
    print("\n--- Test Eccezioni ---")
    
    # Prelievo con saldo insufficiente
    try:
        conto_mario.preleva(5000)
    except SaldoInsufficienteError as e:
        print(f"✓ SaldoInsufficienteError catturato: {e}")
    
    # Deposito con importo negativo
    try:
        conto_mario.deposita(-100)
    except ImportoNonValidoError as e:
        print(f"✓ ImportoNonValidoError catturato: {e}")
    
    # Stampa storico
    conto_mario.stampa_storico()
    conto_luigi.stampa_storico()
    
    print("\n✅ Tutti i test completati con successo!")
