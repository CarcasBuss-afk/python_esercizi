# Riepilogo concatenazione

""" SCOPO: Chiedi all'utente di inserire nome, cognome e codice fiscale (tre input separati).
Crea una variabile 'carta_identita' che concatena queste informazioni nel formato:
"Nome: [nome], Cognome: [cognome], CF: [codice_fiscale]"
Stampa la carta d'identità completa. """

""" Output atteso (esempio):
Inserisci il nome: Luigi
Inserisci il cognome: Verdi
Inserisci il codice fiscale: VRDLGU80A01H501Z
Nome: Luigi, Cognome: Verdi, CF: VRDLGU80A01H501Z
"""
# Scrivi il codice qui sotto

nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
cf = input("Inserisci il tuo CF: ")

carta_identita = "Nome: " + nome + ", Cognome: " + cognome + ", Codice Fiscale: " + cf
print(f"Carta d'idendità: {carta_identita}")