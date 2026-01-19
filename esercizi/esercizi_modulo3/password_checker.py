"""
Esercizio 1: Password Checker

Obiettivo:
- Creare una funzione che valida una password
- Regole: min 8 caratteri, almeno un numero, almeno una maiuscola
- Loop principale che chiede password finché non è valida
"""


def check_password(pwd):
    """
    Valida una password secondo regole specifiche.

    Args:
        pwd: La password da validare.

    Returns:
        Tupla (bool, str): (è_valida, messaggio_errore/successo)
    """
    # Regola 1: lunghezza minima 8 caratteri
    if len(pwd) < 8:
        return False, "Troppo corta (minimo 8 caratteri)"

    # Regola 2: almeno un numero
    if not any(c.isdigit() for c in pwd):
        return False, "Deve contenere almeno un numero"

    # Regola 3: almeno una maiuscola
    if not any(c.isupper() for c in pwd):
        return False, "Deve contenere almeno una maiuscola"

    return True, "Password valida!"


# Main loop - chiede password finché non è valida
print("=== PASSWORD CHECKER ===")
print("Regole:")
print("- Minimo 8 caratteri")
print("- Almeno un numero")
print("- Almeno una lettera maiuscola\n")

while True:
    pwd = input("Inserisci password: ")
    valida, messaggio = check_password(pwd)
    print(messaggio)
    if valida:
        print("✓ Password accettata!")
        break
    print()  # Riga vuota per leggibilità
