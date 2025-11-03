# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: creiamo funzioni con parametri default multipli """

# DEFINISCI UNA FUNZIONE chiamata 'calcola_sconto' con parametri:
# (prezzo, percentuale=10, arrotonda=True)
# Formula sconto: prezzo_scontato = prezzo - (prezzo * percentuale / 100)
# Se arrotonda è True: RESTITUISCE int(prezzo_scontato)
# Altrimenti: RESTITUISCE prezzo_scontato normale
___ calcola_sconto(______, ___________=10, _________=True):
    prezzo_scontato = ______ - (______ * ___________ / 100)
    if _________:
        ______ int(________________)
    ____:
        ______ ________________


# Chiamala solo con il prezzo 100
prezzo1 = ________________(___)
print(f"Prezzo scontato 1: {_______}")

# Chiamala con prezzo 100 e percentuale 20
prezzo2 = ________________(___, __)
print(f"Prezzo scontato 2: {_______}")

# Chiamala con tutti i parametri: 100, 15, False
prezzo3 = ________________(___, __, _____)
print(f"Prezzo scontato 3: {_______}")

# DEFINISCI UNA FUNZIONE chiamata 'crea_username' con parametri:
# (nome, cognome, separatore="_")
# che RESTITUISCE: nome.lower() + separatore + cognome.lower()
# Esempio: crea_username("Mario", "Rossi", ".") restituisce "mario.rossi"




# Chiamala con "Mario" e "Rossi" (usa separatore default)
user1 = _____________("_____", "_____")
print(f"Username 1: {_____}")

# Chiamala con "Mario", "Rossi" e separatore "."
user2 = _____________("_____", "_____", "_")
print(f"Username 2: {_____}")

""" Prova con nomi diversi """
