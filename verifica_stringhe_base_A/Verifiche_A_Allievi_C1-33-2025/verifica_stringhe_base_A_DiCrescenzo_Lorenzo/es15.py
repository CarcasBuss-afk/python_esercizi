# Riepilogo .strip() e validazione

""" SCOPO: Chiedi all'utente di inserire un codice.
Rimuovi gli spazi all'inizio e alla fine del codice.
Se il codice pulito è uguale a "ABC123" stampa "Codice corretto", altrimenti "Codice errato". """
codice = input("inserisci codice: ")
codice.strip()
if codice == "ABC123":
    print("Codice corretto")
else:
    print("Codice errato")







""" Output atteso (esempi):
Inserisci il codice:   ABC123
Codice corretto 
Inserisci il codice: ABC124
Codice errato
"""
