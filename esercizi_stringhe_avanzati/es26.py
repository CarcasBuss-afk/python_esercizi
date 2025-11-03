# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: creiamo una tabella allineata con tre colonne: Nome (sinistra), Età (destra), Città (centro).
Usiamo i metodi di allineamento per formattare l'output. """

# Dati della tabella
persone = [
    ["Mario", "25", "Roma"],
    ["Alessandro", "30", "Milano"],
    ["Luca", "22", "Napoli"],
    ["Francesca", "28", "Torino"]
]

# Larghezze colonne
larghezza_nome = 15
larghezza_eta = 10
larghezza_citta = 15

# Stampiamo l'intestazione
print("TABELLA PERSONE".center(40))
print("-" * 40)

intestazione_nome = "Nome".______(______________)
intestazione_eta = "Età".______(____________)
intestazione_citta = "Città".______(______________)

print(f"{intestazione_nome} {intestazione_eta} {intestazione_citta}")
print(____ * 40)

# Stampiamo ogni riga della tabella
for persona in persone:
    nome = persona[0].ljust(______________)
    eta = persona[1].______(____________)
    citta = persona[2].______(______________)

    print(f"{____} {___} {_____}")

print(____ * 40)

""" Osserva come la tabella è ben formattata e allineata """
