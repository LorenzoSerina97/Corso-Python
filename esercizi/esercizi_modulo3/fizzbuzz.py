"""
Esercizio 2: FizzBuzz

Obiettivo:
- Classico esercizio di programmazione
- Stampare numeri da 1 a N con regole speciali
- Divisibile per 3: "Fizz"
- Divisibile per 5: "Buzz"
- Divisibile per entrambi: "FizzBuzz"
"""


def fizzbuzz(n):
    """
    Stampa i numeri da 1 a n con le regole FizzBuzz.

    Args:
        n: Il numero massimo da stampare.
    """
    for i in range(1, n + 1):
        # Controllare prima entrambi (3 E 5)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Esecuzione
print("=== FIZZBUZZ ===")
print("Numeri da 1 a 30:\n")
fizzbuzz(30)
