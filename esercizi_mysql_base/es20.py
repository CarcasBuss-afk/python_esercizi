# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: Validare input con while True e try/except.
"""

print("Inserisci anno (1980-2024):")

while ________:                                                      # COMPLETA: True
    try:
        anno = int(input("Anno: "))
        if 1980 <= anno <= 2024:
            ________                                                 # COMPLETA: break
        print("Anno non valido!")
    except:
        print("Inserisci un numero!")

print(f"Anno valido: {anno}\n")

print("Inserisci prezzo (positivo):")

while True:
    try:
        prezzo = float(input("Prezzo: ").replace(",", "."))
        if ________ >= 0:                                            # COMPLETA: prezzo
            break
        print("Deve essere positivo!")
    except:
        print("________!")                                           # COMPLETA: messaggio errore

print(f"Prezzo valido: €{prezzo}")
