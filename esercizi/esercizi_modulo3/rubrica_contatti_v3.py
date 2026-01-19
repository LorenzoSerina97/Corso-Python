"""
Progetto Cross-Modulo: Rubrica Contatti - Parte 3

Obiettivo Modulo 3:
- Organizzare il codice con funzioni
- Aggiungere, cercare e mostrare contatti
- Usare docstring per documentare le funzioni

Evoluzione dal Modulo 2: Ora usiamo funzioni per organizzare il codice!
"""

# Lista globale di contatti
rubrica = []


def aggiungi_contatto(nome, telefono, email):
    """
    Aggiunge un nuovo contatto alla rubrica.

    Args:
        nome: Nome del contatto.
        telefono: Numero di telefono.
        email: Indirizzo email.
    """
    contatto = {"nome": nome, "telefono": telefono, "email": email}
    rubrica.append(contatto)
    print(f"✓ Aggiunto: {nome}")


def cerca_contatto(nome):
    """
    Cerca un contatto per nome (case-insensitive).

    Args:
        nome: Nome del contatto da cercare.

    Returns:
        Dizionario del contatto se trovato, None altrimenti.
    """
    for contatto in rubrica:
        if contatto["nome"].lower() == nome.lower():
            return contatto
    return None


def mostra_tutti():
    """Mostra tutti i contatti nella rubrica."""
    if not rubrica:
        print("Rubrica vuota!")
        return

    print(f"\n=== TUTTI I CONTATTI ({len(rubrica)}) ===")
    for i, c in enumerate(rubrica, start=1):
        print(f"{i}. {c['nome']}: {c['telefono']} - {c['email']}")


# Utilizzo delle funzioni
print("=== RUBRICA CONTATTI V3 ===\n")

# Aggiungere contatti
aggiungi_contatto("Mario Rossi", "333-111", "mario@email.com")
aggiungi_contatto("Luigi Verdi", "333-222", "luigi@email.com")
aggiungi_contatto("Peach Bianchi", "333-333", "peach@email.com")
aggiungi_contatto("Toad Gialli", "333-444", "toad@email.com")

# Mostrare tutti i contatti
mostra_tutti()

# Cercare un contatto
print("\n=== RICERCA CONTATTO ===")
nome_cercato = "Luigi Verdi"
risultato = cerca_contatto(nome_cercato)

if risultato:
    print(f"Trovato: {risultato['nome']}")
    print(f"  Telefono: {risultato['telefono']}")
    print(f"  Email: {risultato['email']}")
else:
    print(f"Contatto '{nome_cercato}' non trovato")

# Cercare un contatto inesistente
print()
nome_cercato2 = "Bowser"
risultato2 = cerca_contatto(nome_cercato2)

if risultato2:
    print(f"Trovato: {risultato2['nome']}")
else:
    print(f"✗ Contatto '{nome_cercato2}' non trovato")
