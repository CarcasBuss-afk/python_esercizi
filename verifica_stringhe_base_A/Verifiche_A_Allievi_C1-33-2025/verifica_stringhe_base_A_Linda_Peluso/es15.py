# Riepilogo .strip() e validazione

""" SCOPO: Chiedi all'utente di inserire un codice.
Rimuovi gli spazi all'inizio e alla fine del codice.
Se il codice pulito è uguale a "ABC123" stampa "Codice corretto", altrimenti "Codice errato". """

codice = input("Inserisci un codice: ")
codice_pulito = codice.strip()

if codice_pulito == "ABC123" :
    print("Codice corretto")
else:
    print("Codice errato")
""" Output atteso (esempi):
Inserisci il codice:   ABC123
Codice corretto

Inserisci il codice: ABC124
Codice errato
"""
