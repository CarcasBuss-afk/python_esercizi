# Riepilogo .upper() e .lower()

""" SCOPO: Chiedi all'utente di inserire un hashtag e uno username (due input separati).
Converti l'hashtag in maiuscolo e lo username in minuscolo.
Stampa "Hashtag: [hashtag_maiuscolo]"
Stampa "Username: [username_minuscolo]" """

""" Output atteso (esempio):
Inserisci un hashtag: python
Inserisci uno username: CODER123
Hashtag: PYTHON
Username: coder123
"""
# Scrivi il codice qui sotto
hastag = input("Inserisci un hastag: ")
username = input("Inserisci un username: ")
hastag_maiuscolo = hastag.upper()
username_minuscolo = username.lower()
print(hastag_maiuscolo)
print(username_minuscolo)
