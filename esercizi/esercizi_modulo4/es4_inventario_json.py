"""
Esercizio 4: Inventario con JSON
Modulo 4 - Laboratorio Pratico

Obiettivo: Creare un sistema di gestione inventario con persistenza JSON.
- Caricamento e salvataggio automatico su file
- CRUD operations (Create, Read, Update, Delete)
- Gestione errori per file mancanti o corrotti
"""

import json
import os
from datetime import datetime


class ProdottoNonTrovatoError(Exception):
    """Eccezione per prodotto non trovato."""
    pass


class QuantitaInsufficienteError(Exception):
    """Eccezione per quantità insufficiente."""
    pass


class Inventario:
    """Sistema di gestione inventario con persistenza JSON."""
    
    def __init__(self, file_path="inventario.json"):
        """
        Inizializza l'inventario.
        
        Args:
            file_path: Percorso del file JSON per la persistenza
        """
        self.file_path = file_path
        self.prodotti = self._carica()
    
    def _carica(self):
        """Carica l'inventario dal file JSON."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                print(f"✓ Inventario caricato da {self.file_path}")
                return data
        except FileNotFoundError:
            print(f"ℹ File {self.file_path} non trovato, creo nuovo inventario")
            return {}
        except json.JSONDecodeError:
            print(f"⚠ File {self.file_path} corrotto, creo nuovo inventario")
            return {}
    
    def salva(self):
        """Salva l'inventario su file JSON."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.prodotti, f, indent=2, ensure_ascii=False)
        print(f"💾 Inventario salvato su {self.file_path}")
    
    def aggiungi(self, nome, quantita, prezzo, categoria="generale"):
        """
        Aggiunge un nuovo prodotto all'inventario.
        
        Args:
            nome: Nome del prodotto
            quantita: Quantità disponibile
            prezzo: Prezzo unitario
            categoria: Categoria del prodotto
        """
        if nome in self.prodotti:
            # Se esiste, aggiorna la quantità
            self.prodotti[nome]["quantita"] += quantita
            print(f"📦 Aggiunta quantità a {nome}: +{quantita}")
        else:
            # Nuovo prodotto
            self.prodotti[nome] = {
                "quantita": quantita,
                "prezzo": prezzo,
                "categoria": categoria,
                "data_inserimento": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            print(f"✓ Nuovo prodotto aggiunto: {nome}")
        self.salva()
    
    def rimuovi(self, nome):
        """Rimuove un prodotto dall'inventario."""
        if nome not in self.prodotti:
            raise ProdottoNonTrovatoError(f"Prodotto '{nome}' non trovato")
        del self.prodotti[nome]
        print(f"🗑️ Prodotto rimosso: {nome}")
        self.salva()
    
    def aggiorna_quantita(self, nome, quantita):
        """Aggiorna la quantità di un prodotto."""
        if nome not in self.prodotti:
            raise ProdottoNonTrovatoError(f"Prodotto '{nome}' non trovato")
        self.prodotti[nome]["quantita"] = quantita
        print(f"📝 Quantità aggiornata per {nome}: {quantita}")
        self.salva()
    
    def aggiorna_prezzo(self, nome, prezzo):
        """Aggiorna il prezzo di un prodotto."""
        if nome not in self.prodotti:
            raise ProdottoNonTrovatoError(f"Prodotto '{nome}' non trovato")
        self.prodotti[nome]["prezzo"] = prezzo
        print(f"💰 Prezzo aggiornato per {nome}: {prezzo}€")
        self.salva()
    
    def vendi(self, nome, quantita):
        """
        Registra una vendita (diminuisce la quantità).
        
        Args:
            nome: Nome del prodotto
            quantita: Quantità venduta
            
        Returns:
            Totale della vendita
        """
        if nome not in self.prodotti:
            raise ProdottoNonTrovatoError(f"Prodotto '{nome}' non trovato")
        
        if self.prodotti[nome]["quantita"] < quantita:
            raise QuantitaInsufficienteError(
                f"Quantità insufficiente per '{nome}'. "
                f"Disponibili: {self.prodotti[nome]['quantita']}"
            )
        
        self.prodotti[nome]["quantita"] -= quantita
        totale = quantita * self.prodotti[nome]["prezzo"]
        print(f"💵 Vendita: {quantita}x {nome} = {totale}€")
        self.salva()
        return totale
    
    def cerca(self, nome):
        """Cerca un prodotto per nome."""
        if nome not in self.prodotti:
            raise ProdottoNonTrovatoError(f"Prodotto '{nome}' non trovato")
        return self.prodotti[nome]
    
    def lista_per_categoria(self, categoria):
        """Restituisce tutti i prodotti di una categoria."""
        return {
            nome: info for nome, info in self.prodotti.items()
            if info.get("categoria") == categoria
        }
    
    def prodotti_in_esaurimento(self, soglia=5):
        """Restituisce i prodotti con quantità sotto la soglia."""
        return {
            nome: info for nome, info in self.prodotti.items()
            if info["quantita"] <= soglia
        }
    
    def valore_totale(self):
        """Calcola il valore totale dell'inventario."""
        return sum(
            info["quantita"] * info["prezzo"]
            for info in self.prodotti.values()
        )
    
    def stampa_inventario(self):
        """Stampa l'inventario formattato."""
        print(f"\n{'='*60}")
        print(f"{'INVENTARIO':^60}")
        print(f"{'='*60}")
        
        if not self.prodotti:
            print("  (inventario vuoto)")
        else:
            print(f"{'Prodotto':<20} {'Qtà':>6} {'Prezzo':>10} {'Categoria':<15}")
            print("-" * 60)
            for nome, info in self.prodotti.items():
                print(f"{nome:<20} {info['quantita']:>6} {info['prezzo']:>9}€ {info.get('categoria', 'N/A'):<15}")
        
        print("=" * 60)
        print(f"{'Valore totale inventario:':<40} {self.valore_totale():>10}€")
        print()


# ==================== TEST ====================
if __name__ == "__main__":
    # Usa un file temporaneo per i test
    TEST_FILE = "test_inventario.json"
    
    print("=" * 50)
    print("TEST INVENTARIO CON JSON")
    print("=" * 50)
    
    # Crea inventario
    inv = Inventario(TEST_FILE)
    
    # Aggiungi prodotti
    print("\n--- Aggiunta Prodotti ---")
    inv.aggiungi("Laptop Dell XPS", 10, 1299.99, "elettronica")
    inv.aggiungi("Mouse Logitech", 50, 29.99, "elettronica")
    inv.aggiungi("Tastiera Meccanica", 25, 89.99, "elettronica")
    inv.aggiungi("Monitor 27\"", 15, 349.99, "elettronica")
    inv.aggiungi("Cavo USB-C", 100, 9.99, "accessori")
    inv.aggiungi("Webcam HD", 8, 79.99, "accessori")
    
    # Stampa inventario
    inv.stampa_inventario()
    
    # Test vendita
    print("\n--- Test Vendite ---")
    inv.vendi("Mouse Logitech", 5)
    inv.vendi("Laptop Dell XPS", 2)
    
    # Test aggiornamenti
    print("\n--- Test Aggiornamenti ---")
    inv.aggiorna_prezzo("Cavo USB-C", 7.99)
    inv.aggiungi("Mouse Logitech", 20, 29.99)  # Aggiungi scorte
    
    # Test ricerca
    print("\n--- Test Ricerca ---")
    prodotto = inv.cerca("Laptop Dell XPS")
    print(f"Trovato: Laptop Dell XPS - {prodotto}")
    
    # Prodotti in esaurimento
    print("\n--- Prodotti in Esaurimento (<=10) ---")
    esaurimento = inv.prodotti_in_esaurimento(10)
    for nome, info in esaurimento.items():
        print(f"  ⚠️ {nome}: {info['quantita']} unità")
    
    # Prodotti per categoria
    print("\n--- Prodotti Elettronica ---")
    elettronica = inv.lista_per_categoria("elettronica")
    for nome in elettronica:
        print(f"  • {nome}")
    
    # Test eccezioni
    print("\n--- Test Eccezioni ---")
    try:
        inv.cerca("Prodotto Inesistente")
    except ProdottoNonTrovatoError as e:
        print(f"✓ ProdottoNonTrovatoError: {e}")
    
    try:
        inv.vendi("Webcam HD", 100)
    except QuantitaInsufficienteError as e:
        print(f"✓ QuantitaInsufficienteError: {e}")
    
    # Stampa finale
    inv.stampa_inventario()
    
    # Cleanup file di test
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
        print(f"🧹 File di test {TEST_FILE} rimosso")
    
    print("\n✅ Tutti i test completati con successo!")
