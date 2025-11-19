# Riepilogo .upper() e .lower()

""" SCOPO: Chiedi all'utente di inserire un hashtag e uno username (due input separati).
Converti l'hashtag in maiuscolo e lo username in minuscolo.
Stampa "Hashtag: [hashtag_maiuscolo]"
Stampa "Username: [username_minuscolo" """


""" Output atteso (esempio):
Inserisci un hashtag: python
Inserisci uno username: CODER123
Hashtag: PYTHON
Username: coder123
"""
# Scrivi il codice qui sotto

hashtag = input("Inserisci un hastag: ")
nome = input("Inserisci lo username: ")
a_has = hashtag.upper()
a_nome = nome.lower()

print(f"Hashtag: {a_has}")
print(f"username: {a_nome}")