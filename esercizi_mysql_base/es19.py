# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Gestire input prezzi con .replace(",", ".").
Permette agli utenti di usare la virgola!
"""

print("Inserisci prezzi (usa virgola o punto):\n")

# Test 1
prezzo1 = float(input("Prezzo 1: ").________(________, ________))    # COMPLETA: replace, ",", "."
print(f"Convertito: €{prezzo1}\n")

# Test 2
prezzo2 = float(input("Prezzo 2: ").replace(",", "."))
print(f"Convertito: €{prezzo2}")

# Funzione helper
def chiedi_prezzo(msg):
    return float(input(msg).________(________, ________))            # COMPLETA: replace, ",", "."

prezzo3 = chiedi_prezzo("Prezzo 3: ")
print(f"Convertito: €{prezzo3}")
