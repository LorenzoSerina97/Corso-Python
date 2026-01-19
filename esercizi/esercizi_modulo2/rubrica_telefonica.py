"""
Esercizio 3: Rubrica Telefonica

Obiettivo:
- Dizionario annidato con operazioni CRUD
- Aggiungere, cercare ed eliminare contatti
"""

# Rubrica inizialmente vuota
rubrica = {}


def aggiungi_contatto(nome, telefono, email=None):
    """Aggiunge un contatto alla rubrica."""
    rubrica[nome] = {"telefono": telefono, "email": email}
    print(f"Contatto '{nome}' aggiunto con successo!")


def cerca_contatto(nome):
    """Cerca un contatto nella rubrica."""
    return rubrica.get(nome, "Contatto non trovato")


def elimina_contatto(nome):
    """Elimina un contatto dalla rubrica."""
    contatto = rubrica.pop(nome, None)
    if contatto:
        print(f"Contatto '{nome}' eliminato.")
        return contatto
    else:
        print(f"Contatto '{nome}' non trovato.")
        return None


# Utilizzo della rubrica
print("=== GESTIONE RUBRICA TELEFONICA ===\n")

# Aggiungere contatti
aggiungi_contatto("Mario", "123456", "mario@email.com")
aggiungi_contatto("Luigi", "789012")
aggiungi_contatto("Peach", "555-0123", "peach@email.com")

# Cercare contatti
print(f"\nCerca 'Mario': {cerca_contatto('Mario')}")
print(f"Cerca 'Bowser': {cerca_contatto('Bowser')}")

# Mostrare tutti i contatti
print(f"\nTutti i contatti: {rubrica}")

# Eliminare un contatto
print()
elimina_contatto("Luigi")

# Mostrare contatti rimanenti
print(f"\nContatti rimanenti: {rubrica}")
