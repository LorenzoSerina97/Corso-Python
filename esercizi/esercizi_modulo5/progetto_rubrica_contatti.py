"""
Progetto Cross-Modulo: Rubrica Contatti
Modulo 5 - Parte 5: Persistenza su File (FINALE)

Obiettivo: Completare il sistema di gestione rubrica con:
- Salvataggio automatico su file JSON
- Caricamento automatico all'avvio
- Persistenza tra le esecuzioni
- Gestione errori file

Questo è il completamento del progetto iniziato nel Modulo 1!
"""

import json
from pathlib import Path
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
        # Ripristina la data se presente
        if "data_creazione" in dati:
            try:
                contatto.data_creazione = date.fromisoformat(dati["data_creazione"])
            except ValueError:
                pass  # Usa la data corrente se il formato è invalido
        return contatto


class Rubrica:
    """
    Gestisce una collezione di contatti con persistenza su file JSON.
    
    NOVITÀ MODULO 5:
    - Salvataggio automatico dopo ogni modifica
    - Caricamento automatico all'avvio
    - Backup automatico prima di salvare
    """
    
    def __init__(self, file_path="rubrica.json", nome="Rubrica Personale"):
        """
        Inizializza la rubrica e carica i dati dal file se esiste.
        
        Args:
            file_path: Percorso del file JSON
            nome: Nome della rubrica
        """
        self.file_path = Path(file_path)
        self.nome = nome
        self.contatti = []
        
        # Carica i contatti esistenti
        self._carica()
    
    def _carica(self):
        """
        Carica i contatti dal file JSON.
        
        NOVITÀ MODULO 5: Gestione automatica del caricamento.
        """
        if self.file_path.exists():
            try:
                dati = json.loads(self.file_path.read_text(encoding="utf-8"))
                
                # Converti ogni dizionario in oggetto Contatto
                for contatto_dict in dati:
                    contatto = Contatto.from_dict(contatto_dict)
                    self.contatti.append(contatto)
                
                print(f"✅ Caricati {len(self.contatti)} contatti da {self.file_path}")
            
            except json.JSONDecodeError:
                print(f"⚠️  File {self.file_path} corrotto, partenza con rubrica vuota")
            except Exception as e:
                print(f"⚠️  Errore caricamento: {e}")
        else:
            print(f"📝 Nuova rubrica: {self.file_path}")
    
    def _salva(self):
        """
        Salva i contatti su file JSON.
        
        NOVITÀ MODULO 5: Salvataggio automatico con backup.
        """
        try:
            # Crea backup se il file esiste
            if self.file_path.exists():
                backup_path = self.file_path.with_suffix('.json.bak')
                backup_path.write_text(
                    self.file_path.read_text(encoding="utf-8"),
                    encoding="utf-8"
                )
            
            # Salva i dati
            dati = [c.to_dict() for c in self.contatti]
            self.file_path.write_text(
                json.dumps(dati, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )
            
            print(f"💾 Rubrica salvata in {self.file_path}")
        
        except Exception as e:
            print(f"❌ Errore salvataggio: {e}")
    
    def aggiungi(self, contatto):
        """
        Aggiunge un contatto alla rubrica e salva.
        
        Args:
            contatto: Oggetto Contatto da aggiungere
            
        Raises:
            ContattoDuplicatoError: Se il contatto esiste già
        """
        if contatto in self.contatti:
            raise ContattoDuplicatoError(f"Contatto '{contatto.nome}' già presente")
        
        self.contatti.append(contatto)
        print(f"✓ Aggiunto: {contatto.nome}")
        
        # NOVITÀ: Salva automaticamente
        self._salva()
    
    def rimuovi(self, nome):
        """
        Rimuove un contatto dalla rubrica e salva.
        
        Args:
            nome: Nome del contatto da rimuovere
            
        Raises:
            ContattoNonTrovatoError: Se il contatto non esiste
        """
        contatto = self.cerca(nome)
        self.contatti.remove(contatto)
        print(f"🗑️ Rimosso: {nome}")
        
        # NOVITÀ: Salva automaticamente
        self._salva()
    
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
        Modifica un contatto esistente e salva.
        
        Args:
            nome: Nome del contatto da modificare
            **kwargs: Attributi da aggiornare (telefono, email, note)
        """
        contatto = self.cerca(nome)
        for chiave, valore in kwargs.items():
            if hasattr(contatto, chiave):
                setattr(contatto, chiave, valore)
                print(f"📝 Aggiornato {chiave} per {nome}")
        
        # NOVITÀ: Salva automaticamente
        self._salva()
    
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
    
    def esporta_csv(self, file_path="rubrica.csv"):
        """
        Esporta la rubrica in formato CSV.
        
        NOVITÀ MODULO 5: Export in CSV per compatibilità.
        """
        import csv
        
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, 
                fieldnames=["nome", "telefono", "email", "note", "data_creazione"]
            )
            writer.writeheader()
            for c in self.contatti:
                writer.writerow(c.to_dict())
        
        print(f"📄 Rubrica esportata in {file_path}")
    
    def __len__(self):
        """Restituisce il numero di contatti."""
        return len(self.contatti)
    
    def __iter__(self):
        """Permette di iterare sulla rubrica."""
        return iter(self.contatti)
    
    def __contains__(self, contatto):
        """Permette di usare 'in' per verificare la presenza."""
        return contatto in self.contatti


# ==================== DEMO INTERATTIVA ====================
def demo_persistenza():
    """Dimostra la persistenza tra esecuzioni."""
    
    print("=" * 60)
    print("DEMO: PERSISTENZA RUBRICA CONTATTI")
    print("=" * 60)
    print()
    
    # Crea/carica rubrica
    rubrica = Rubrica("rubrica_demo.json", "Rubrica Demo")
    
    print("\n--- Stato Iniziale ---")
    rubrica.stampa()
    
    # Se la rubrica è vuota, aggiungi contatti di esempio
    if len(rubrica) == 0:
        print("\n--- Prima Esecuzione: Aggiungo Contatti ---")
        rubrica.aggiungi(Contatto("Mario Rossi", "+39 333 1234567", "mario@email.it"))
        rubrica.aggiungi(Contatto("Luigi Verdi", "+39 347 9876543", "luigi@email.it"))
        rubrica.aggiungi(Contatto("Anna Bianchi", "+39 320 5555555", "anna@email.it"))
        
        print("\n✨ I contatti sono stati salvati!")
        print("🔄 Esegui di nuovo questo script per vedere la persistenza!")
    else:
        print("\n--- Esecuzione Successiva: Contatti Caricati! ---")
        print("✅ La rubrica ha mantenuto i dati tra le esecuzioni!")
        
        # Aggiungi un nuovo contatto
        print("\n--- Aggiungo un Nuovo Contatto ---")
        try:
            rubrica.aggiungi(Contatto(
                f"Contatto {len(rubrica) + 1}", 
                f"+39 333 {len(rubrica):07d}", 
                f"contatto{len(rubrica) + 1}@email.it"
            ))
        except ContattoDuplicatoError:
            print("⚠️  Contatto già presente")
    
    # Mostra rubrica finale
    print("\n--- Rubrica Finale ---")
    rubrica.stampa_dettagliata()
    
    # Test ricerca
    print("\n--- Test Ricerca ---")
    risultati = rubrica.cerca_parziale("333")
    print(f"Contatti con '333': {len(risultati)}")
    for c in risultati:
        print(f"  • {c}")
    
    # Export CSV
    print("\n--- Export CSV ---")
    rubrica.esporta_csv("rubrica_demo.csv")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETATA")
    print("=" * 60)
    print(f"\n📁 File creati:")
    print(f"  • rubrica_demo.json (dati persistenti)")
    print(f"  • rubrica_demo.json.bak (backup)")
    print(f"  • rubrica_demo.csv (export)")


# ==================== TEST COMPLETO ====================
if __name__ == "__main__":
    print("=" * 60)
    print("PROGETTO CROSS-MODULO: RUBRICA CONTATTI")
    print("Modulo 5 - Versione Finale con Persistenza")
    print("=" * 60)
    print()
    
    # Esegui la demo
    demo_persistenza()
    
    print("\n\n🎉 PROGETTO COMPLETATO!")
    print("\n📚 Evoluzione del progetto:")
    print("  Modulo 1: Input/Output base")
    print("  Modulo 2: Liste e dizionari")
    print("  Modulo 3: Funzioni e validazione")
    print("  Modulo 4: Classi e OOP")
    print("  Modulo 5: Persistenza su file ✅")
    print()
    print("💡 Prossimi miglioramenti possibili:")
    print("  • Interfaccia grafica (Tkinter)")
    print("  • Database SQL (SQLite)")
    print("  • API REST (Flask)")
    print("  • App mobile (Kivy)")
