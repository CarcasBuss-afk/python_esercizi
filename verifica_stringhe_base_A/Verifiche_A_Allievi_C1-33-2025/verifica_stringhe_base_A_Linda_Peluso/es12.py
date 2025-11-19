# Riepilogo .upper() e .lower()

""" SCOPO: Chiedi all'utente di inserire il proprio nome e cognome (due input separati).
Converti il nome in maiuscolo e il cognome in minuscolo.
Stampa "Nome: [nome_maiuscolo]"
Stampa "Cognome: [cognome_minuscolo]" """

nome = input("Inserisci il tuo nome: ")
nome_maiuscolo = nome.upper()

cognome = input("Inserisci il tuo cognome: ")
cognome_minuscolo = cognome.lower()

print("Nome: ", nome_maiuscolo)
print("Cognome: ", cognome_minuscolo)
""" Output atteso (esempio):
Inserisci il tuo nome: mario
Inserisci il tuo cognome: ROSSI
Nome: MARIO
Cognome: rossi
"""
