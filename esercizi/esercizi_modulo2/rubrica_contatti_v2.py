"""
Progetto Cross-Modulo: Rubrica Contatti - Parte 2

Obiettivo Modulo 2:
- Gestire MOLTI contatti usando liste di dizionari
- Ogni contatto è un dizionario
- Operazioni su collezioni di contatti

Evoluzione dal Modulo 1: Ora possiamo gestire più contatti!
"""

# Lista di dizionari: ogni contatto è un dict
rubrica = [
    {"nome": "Mario", "telefono": "333-111", "email": "mario@email.com"},
    {"nome": "Luigi", "telefono": "333-222", "email": "luigi@email.com"},
    {"nome": "Peach", "telefono": "333-333", "email": "peach@email.com"}
]

print("=== RUBRICA CONTATTI V2 ===\n")

# Accesso ai dati
print(f"Primo contatto: {rubrica[0]['nome']}")

# Aggiungere un contatto
nuovo_contatto = {
    "nome": "Toad",
    "telefono": "333-444",
    "email": "toad@email.com"
}
rubrica.append(nuovo_contatto)
print(f"\nAggiunto nuovo contatto: {nuovo_contatto['nome']}")

# Quanti contatti?
print(f"\nContatti totali: {len(rubrica)}")

# Mostrare tutti i contatti
print("\n=== TUTTI I CONTATTI ===")
for contatto in rubrica:
    print(f"Nome: {contatto['nome']}")
    print(f"  Telefono: {contatto['telefono']}")
    print(f"  Email: {contatto['email']}")
    print()

# Cercare un contatto per nome
nome_cercato = "Luigi"
print(f"=== CERCA '{nome_cercato}' ===")
for contatto in rubrica:
    if contatto['nome'] == nome_cercato:
        print(f"Trovato! Telefono: {contatto['telefono']}")
        break
else:
    print("Contatto non trovato")
