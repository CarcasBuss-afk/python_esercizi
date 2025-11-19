# Riepilogo .upper() e .lower()

""" SCOPO: Chiedi all'utente di inserire il proprio nome e cognome (due input separati).
Converti il nome in maiuscolo e il cognome in minuscolo.
Stampa "Nome: [nome_maiuscolo]"
Stampa "Cognome: [cognome_minuscolo]" """

""" Output atteso (esempio):
Inserisci il tuo nome: mario
Inserisci il tuo cognome: ROSSI
Nome: MARIO
Cognome: rossi
"""
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
nome1 = nome.upper()
nome2 = cognome.lower()
print(f"Nome: {nome1}")
print(f"Cognome: {nome2}")