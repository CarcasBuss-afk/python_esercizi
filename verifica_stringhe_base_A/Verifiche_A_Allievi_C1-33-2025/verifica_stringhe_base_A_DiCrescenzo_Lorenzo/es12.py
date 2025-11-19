# Riepilogo .upper() e .lower()

""" SCOPO: Chiedi all'utente di inserire il proprio nome e cognome (due input separati).
Converti il nome in maiuscolo e il cognome in minuscolo.
Stampa "Nome: [nome_maiuscolo]"
Stampa "Cognome: [cognome_minuscolo]" """
nome = input("inserisci il tuo nome: ")
cognome = input("inserisci il tuo cognome: ")
nome_maiuscolo = nome.upper()
cognome_minuscolo = cognome.lower()
print(f"nome: {nome_maiuscolo} ")
print(f"nome: {cognome_minuscolo} ")




""" Output atteso (esempio):
Inserisci il tuo nome: mario
Inserisci il tuo cognome: ROSSI
Nome: MARIO
Cognome: rossi
"""
