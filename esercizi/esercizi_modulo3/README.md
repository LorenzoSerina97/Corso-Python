# Esercizi Modulo 3 - Flusso, Logica e Funzioni

Questa directory contiene gli esercizi del Modulo 3 del corso Python.

## Esercizi Disponibili

### 1. Password Checker

**File:** `password_checker.py`

**Obiettivo:** Creare una funzione che valida una password secondo regole specifiche.

**Regole di validazione:**

- Lunghezza minima 8 caratteri
- Deve contenere almeno un numero
- Deve contenere almeno una lettera maiuscola

**Funzionalità:** Loop principale che chiede la password finché non è valida.

**Esecuzione:**

```bash
python password_checker.py
```

---

### 2. FizzBuzz

**File:** `fizzbuzz.py`

**Obiettivo:** Classico esercizio di programmazione.

**Regole:**

- Stampa i numeri da 1 a N
- Se divisibile per 3, stampa "Fizz"
- Se divisibile per 5, stampa "Buzz"
- Se divisibile per entrambi, stampa "FizzBuzz"

**Esecuzione:**

```bash
python fizzbuzz.py
```

---

### 3. Calcolatrice

**File:** `calcolatrice.py`

**Obiettivo:** Creare una calcolatrice interattiva con funzioni.

**Funzionalità:**

- Operazioni: somma, sottrazione, moltiplicazione, divisione
- Gestione errori (divisione per zero, input non valido)
- Loop interattivo fino al comando "esci"

**Esecuzione:**

```bash
python calcolatrice.py
```

---

### 4. Analizzatore di Numeri

**File:** `analizzatore_numeri.py`

**Obiettivo:** Funzione che analizza una lista di numeri e restituisce statistiche complete.

**Statistiche calcolate:**

- Conteggio elementi
- Somma totale
- Media
- Minimo e massimo
- Numeri pari e dispari

**Esecuzione:**

```bash
python analizzatore_numeri.py
```

---

### 5. Progetto Cross-Modulo: Rubrica Contatti (Parte 3)

**File:** `rubrica_contatti_v3.py`

**Obiettivo:** Aggiungere funzioni alla rubrica per organizzare il codice.

**Funzioni implementate:**

- `aggiungi_contatto()`: Aggiunge un nuovo contatto
- `cerca_contatto()`: Cerca un contatto per nome
- `mostra_tutti()`: Mostra tutti i contatti

**Esecuzione:**

```bash
python rubrica_contatti_v3.py
```

---

## Concetti Chiave

### Controllo di Flusso

- `if`, `elif`, `else`: Decisioni condizionali
- Operatori di confronto: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Operatori logici: `and`, `or`, `not`
- Operatore ternario: `valore if condizione else altro_valore`

### Cicli (Loops)

- `for`: Iterare su sequenze
- `while`: Iterare finché una condizione è vera
- `break`: Esce dal ciclo
- `continue`: Salta all'iterazione successiva
- `range()`: Genera sequenze numeriche
- `enumerate()`: Indice + valore
- `zip()`: Iterare su più liste in parallelo

### Funzioni

- `def nome_funzione(parametri):`: Definizione
- `return`: Restituisce valori
- Docstring: Documentazione con `"""`
- Parametri default
- `*args`: Argomenti variabili posizionali
- `**kwargs`: Argomenti variabili nominati
- Lambda: Funzioni anonime brevi

### Scope

- Locale vs Globale
- `global`: Modificare variabili globali
- `nonlocal`: Modificare variabili della funzione esterna
- Regola LEGB: Local → Enclosing → Global → Built-in

## Come Usare Questi Esercizi

1. **Prova prima da solo:** Leggi l'obiettivo e prova a scrivere il codice
2. **Consulta le soluzioni:** Se sei bloccato, guarda i file di soluzione
3. **Sperimenta:** Modifica i valori e aggiungi funzionalità extra
4. **Debug:** Usa il debugger di VS Code per capire come funziona il codice
