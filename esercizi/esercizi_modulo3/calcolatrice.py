"""
Esercizio 3: Calcolatrice

Obiettivo:
- Creare una calcolatrice interattiva con funzioni
- Operazioni: +, -, *, /
- Gestione errori (divisione per zero, input non valido)
- Loop interattivo fino al comando "esci"
"""


def somma(a, b):
    """Somma due numeri."""
    return a + b


def sottrai(a, b):
    """Sottrae b da a."""
    return a - b


def moltiplica(a, b):
    """Moltiplica due numeri."""
    return a * b


def dividi(a, b):
    """Divide a per b. Gestisce divisione per zero."""
    if b == 0:
        return "Errore: divisione per zero"
    return a / b


# Dizionario di operazioni (funzioni come valori!)
operazioni = {
    "+": somma,
    "-": sottrai,
    "*": moltiplica,
    "/": dividi
}


def calcolatrice():
    """Loop principale della calcolatrice."""
    print("=== CALCOLATRICE ===")
    print("Formato: numero operatore numero")
    print("Esempio: 5 + 3")
    print("Scrivi 'esci' per uscire\n")

    while True:
        expr = input("Calcolo: ")

        if expr.lower() == "esci":
            print("Arrivederci!")
            break

        try:
            # Spacchetta l'input
            parti = expr.split()
            a = float(parti[0])
            op = parti[1]
            b = float(parti[2])

            # Esegue l'operazione
            if op in operazioni:
                risultato = operazioni[op](a, b)
                print(f"= {risultato}\n")
            else:
                print("Operatore non valido. Usa: +, -, *, /\n")

        except (IndexError, ValueError):
            print("Formato non valido. Usa: numero operatore numero\n")
        except Exception as e:
            print(f"Errore: {e}\n")


# Esecuzione
if __name__ == "__main__":
    calcolatrice()
