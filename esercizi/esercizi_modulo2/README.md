# Esercizi Modulo 2 - Strutture Dati Core

Questa directory contiene gli esercizi del Modulo 2 del corso Python.

## Esercizi Disponibili

### 1. Gestore Magazzino

**File:** `gestore_magazzino.py`

**Obiettivo:** Usare Liste e Dizionari insieme per gestire un magazzino.

- Dizionario `magazzino` con `prodotto: quantità`
- Lista `movimenti` che registra le operazioni
- Simulazione di vendita con aggiornamento quantità

**Esecuzione:**

```bash
python gestore_magazzino.py
```

---

### 2. Analizzatore di Testo

**File:** `analizzatore_testo.py`

**Obiettivo:** Usare Set e Dizionari per analizzare testi.

- Contare la frequenza di ogni parola (dizionario)
- Trovare le parole uniche (set)
- Trovare le parole in comune tra due testi

**Esecuzione:**

```bash
python analizzatore_testo.py
```

---

### 3. Rubrica Telefonica

**File:** `rubrica_telefonica.py`

**Obiettivo:** Dizionario annidato con operazioni CRUD (Create, Read, Update, Delete).

- Aggiungere contatti
- Cercare contatti
- Eliminare contatti

**Esecuzione:**

```bash
python rubrica_telefonica.py
```

---

### 4. Progetto Cross-Modulo: Rubrica Contatti (Parte 2)

**File:** `rubrica_contatti_v2.py`

**Obiettivo:** Gestire MOLTI contatti usando liste di dizionari.

- Lista di dizionari: ogni contatto è un dict
- Operazioni su collezioni di contatti

**Esecuzione:**

```bash
python rubrica_contatti_v2.py
```

---

## Concetti Chiave

### Liste

- Collezioni ordinate e modificabili
- Metodi: `append()`, `extend()`, `insert()`, `pop()`, `remove()`
- List comprehension: `[x**2 for x in range(10)]`

### Tuple

- Sequenze immutabili
- Unpacking: `x, y = (10, 20)`
- Utili per dati costanti

### Dizionari

- Associazioni chiave-valore
- Metodi: `.get()`, `.keys()`, `.values()`, `.items()`
- Dictionary comprehension

### Set

- Collezioni di elementi unici
- Operazioni insiemistiche: unione, intersezione, differenza
- Rimozione automatica duplicati

## Come Usare Questi Esercizi

1. **Prova prima da solo:** Leggi l'obiettivo e prova a scrivere il codice
2. **Consulta le soluzioni:** Se sei bloccato, guarda i file di soluzione
3. **Sperimenta:** Modifica i valori e aggiungi funzionalità extra
4. **Debug:** Usa il debugger di VS Code per capire come funziona il codice
