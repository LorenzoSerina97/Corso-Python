"""
Progetto Cross-Modulo: Rubrica Contatti
Modulo 4 - Parte 4: Classe Contatto e Rubrica

Obiettivo: Creare un sistema di gestione rubrica con:
- Classe Contatto con metodi speciali (__str__, __repr__)
- Classe Rubrica per gestire la collezione
- Ricerca contatti con gestione errori
- Preparazione per salvataggio su file (Modulo 5)
"""

from datetime import date


class ContattoNonTrovatoError(Exception):
    """Eccezione per contatto non trovato."""
    pass


class ContattoDuplicatoError(Exception):
    """Eccezione per contatto già esistente."""
    pass


class Contatto:
    """Rappresenta un singolo contatto della rubrica."""
    
    def __init__(self, nome, telefono, email="", note=""):
        """
        Inizializza un contatto.
        
        Args:
            nome: Nome completo del contatto
            telefono: Numero di telefono
            email: Indirizzo email (opzionale)
            note: Note aggiuntive (opzionale)
        """
        self.nome = nome
        self.telefono = telefono
        self.email = email
        self.note = note
        self.data_creazione = date.today()
    
    def __str__(self):
        """Rappresentazione leggibile del contatto."""
        return f"{self.nome}: {self.telefono}"
    
    def __repr__(self):
        """Rappresentazione per debug."""
        return f"Contatto('{self.nome}', '{self.telefono}', '{self.email}')"
    
    def __eq__(self, altro):
        """Due contatti sono uguali se hanno lo stesso nome (case insensitive)."""
        if not isinstance(altro, Contatto):
            return False
        return self.nome.lower() == altro.nome.lower()
    
    def info_completa(self):
        """Restituisce tutte le informazioni del contatto."""
        info = f"📇 {self.nome}\n"
        info += f"   📞 {self.telefono}\n"
        if self.email:
            info += f"   📧 {self.email}\n"
        if self.note:
            info += f"   📝 {self.note}\n"
        info += f"   📅 Aggiunto: {self.data_creazione}"
        return info
    
    def to_dict(self):
        """Converte il contatto in dizionario (per salvataggio JSON)."""
        return {
            "nome": self.nome,
            "telefono": self.telefono,
            "email": self.email,
            "note": self.note,
            "data_creazione": str(self.data_creazione)
        }
    
    @classmethod
    def from_dict(cls, dati):
        """Crea un contatto da un dizionario."""
        contatto = cls(
            dati["nome"],
            dati["telefono"],
            dati.get("email", ""),
            dati.get("note", "")
        )
        return contatto


class Rubrica:
    """Gestisce una collezione di contatti."""
    
    def __init__(self, nome="Rubrica Personale"):
        """
        Inizializza una rubrica vuota.
        
        Args:
            nome: Nome della rubrica
        """
        self.nome = nome
        self.contatti = []
    
    def aggiungi(self, contatto):
        """
        Aggiunge un contatto alla rubrica.
        
        Args:
            contatto: Oggetto Contatto da aggiungere
            
        Raises:
            ContattoDuplicatoError: Se il contatto esiste già
        """
        if contatto in self.contatti:
            raise ContattoDuplicatoError(f"Contatto '{contatto.nome}' già presente")
        self.contatti.append(contatto)
        print(f"✓ Aggiunto: {contatto.nome}")
    
    def rimuovi(self, nome):
        """
        Rimuove un contatto dalla rubrica.
        
        Args:
            nome: Nome del contatto da rimuovere
            
        Raises:
            ContattoNonTrovatoError: Se il contatto non esiste
        """
        contatto = self.cerca(nome)  # Solleva eccezione se non trovato
        self.contatti.remove(contatto)
        print(f"🗑️ Rimosso: {nome}")
    
    def cerca(self, nome):
        """
        Cerca un contatto per nome.
        
        Args:
            nome: Nome (o parte del nome) da cercare
            
        Returns:
            Contatto trovato
            
        Raises:
            ContattoNonTrovatoError: Se nessun contatto corrisponde
        """
        for c in self.contatti:
            if c.nome.lower() == nome.lower():
                return c
        raise ContattoNonTrovatoError(f"Contatto '{nome}' non trovato")
    
    def cerca_parziale(self, testo):
        """
        Cerca contatti che contengono il testo nel nome, telefono o email.
        
        Args:
            testo: Testo da cercare
            
        Returns:
            Lista di contatti che corrispondono
        """
        testo = testo.lower()
        risultati = []
        for c in self.contatti:
            if (testo in c.nome.lower() or 
                testo in c.telefono or 
                testo in c.email.lower()):
                risultati.append(c)
        return risultati
    
    def modifica(self, nome, **kwargs):
        """
        Modifica un contatto esistente.
        
        Args:
            nome: Nome del contatto da modificare
            **kwargs: Attributi da aggiornare (telefono, email, note)
        """
        contatto = self.cerca(nome)
        for chiave, valore in kwargs.items():
            if hasattr(contatto, chiave):
                setattr(contatto, chiave, valore)
                print(f"📝 Aggiornato {chiave} per {nome}")
    
    def lista_tutti(self):
        """Restituisce tutti i contatti ordinati per nome."""
        return sorted(self.contatti, key=lambda c: c.nome.lower())
    
    def stampa(self):
        """Stampa la rubrica formattata."""
        print(f"\n{'='*50}")
        print(f"📖 {self.nome}")
        print(f"{'='*50}")
        
        if not self.contatti:
            print("  (rubrica vuota)")
        else:
            for i, c in enumerate(self.lista_tutti(), 1):
                print(f"  {i}. {c}")
        
        print(f"{'='*50}")
        print(f"Totale contatti: {len(self.contatti)}")
    
    def stampa_dettagliata(self):
        """Stampa tutti i contatti con dettagli completi."""
        print(f"\n{'='*50}")
        print(f"📖 {self.nome} - Vista Dettagliata")
        print(f"{'='*50}")
        
        for c in self.lista_tutti():
            print(c.info_completa())
            print("-" * 30)
    
    def to_list(self):
        """Converte la rubrica in lista di dizionari (per JSON)."""
        return [c.to_dict() for c in self.contatti]
    
    @classmethod
    def from_list(cls, lista, nome="Rubrica"):
        """Crea una rubrica da una lista di dizionari."""
        rubrica = cls(nome)
        for dati in lista:
            contatto = Contatto.from_dict(dati)
            rubrica.contatti.append(contatto)
        return rubrica
    
    def __len__(self):
        """Restituisce il numero di contatti."""
        return len(self.contatti)
    
    def __iter__(self):
        """Permette di iterare sulla rubrica."""
        return iter(self.contatti)
    
    def __contains__(self, contatto):
        """Permette di usare 'in' per verificare la presenza."""
        return contatto in self.contatti


# ==================== TEST ====================
if __name__ == "__main__":
    print("=" * 50)
    print("TEST RUBRICA CONTATTI")
    print("=" * 50)
    
    # Creazione rubrica
    rubrica = Rubrica("Rubrica di Lavoro")
    
    # Aggiunta contatti
    print("\n--- Aggiunta Contatti ---")
    rubrica.aggiungi(Contatto("Mario Rossi", "+39 333 1234567", "mario@email.it"))
    rubrica.aggiungi(Contatto("Luigi Verdi", "+39 347 9876543", "luigi@email.it", "Collega reparto IT"))
    rubrica.aggiungi(Contatto("Anna Bianchi", "+39 320 5555555", "anna@email.it"))
    rubrica.aggiungi(Contatto("Paolo Neri", "+39 339 1111111"))
    rubrica.aggiungi(Contatto("Giulia Ferrari", "+39 328 2222222", "giulia@ferrari.it"))
    
    # Stampa rubrica
    rubrica.stampa()
    
    # Test ricerca esatta
    print("\n--- Test Ricerca Esatta ---")
    try:
        contatto = rubrica.cerca("mario rossi")  # Case insensitive
        print(f"Trovato: {contatto}")
        print(contatto.info_completa())
    except ContattoNonTrovatoError as e:
        print(f"Errore: {e}")
    
    # Test ricerca parziale
    print("\n--- Test Ricerca Parziale ---")
    risultati = rubrica.cerca_parziale("333")
    print(f"Contatti con '333': {len(risultati)}")
    for c in risultati:
        print(f"  • {c}")
    
    # Test modifica
    print("\n--- Test Modifica ---")
    rubrica.modifica("Paolo Neri", email="paolo.neri@email.it", note="Aggiunta email")
    
    # Test contatto duplicato
    print("\n--- Test Contatto Duplicato ---")
    try:
        rubrica.aggiungi(Contatto("Mario Rossi", "+39 000 0000000"))
    except ContattoDuplicatoError as e:
        print(f"✓ ContattoDuplicatoError: {e}")
    
    # Test contatto non trovato
    print("\n--- Test Contatto Non Trovato ---")
    try:
        rubrica.cerca("Nome Inesistente")
    except ContattoNonTrovatoError as e:
        print(f"✓ ContattoNonTrovatoError: {e}")
    
    # Test rimozione
    print("\n--- Test Rimozione ---")
    rubrica.rimuovi("Anna Bianchi")
    
    # Stampa dettagliata finale
    rubrica.stampa_dettagliata()
    
    # Test conversione a dizionario (preparazione per Modulo 5)
    print("\n--- Preparazione per Salvataggio (Modulo 5) ---")
    import json
    dati_json = json.dumps(rubrica.to_list(), indent=2, ensure_ascii=False)
    print("Dati pronti per JSON:")
    print(dati_json[:300] + "...")
    
    # Test iterazione
    print("\n--- Test Iterazione ---")
    print(f"La rubrica contiene {len(rubrica)} contatti")
    for c in rubrica:
        print(f"  • {c.nome}")
    
    print("\n✅ Tutti i test completati con successo!")
    print("\n📌 Prossimo modulo: implementare salvataggio/caricamento da file!")
