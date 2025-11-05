# Riepilogo len()

""" SCOPO: Chiedi all'utente di inserire il proprio nome e cognome (due input separati).
Calcola la lunghezza di entrambi.
Stampa "Nome: [nome], Lunghezza: [lunghezza_nome]"
Stampa "Cognome: [cognome], Lunghezza: [lunghezza_cognome]" """

""" Output atteso (esempio):
Inserisci il tuo nome: Marco
Inserisci il tuo cognome: Bianchi
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
"""
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
lung_nome = len(nome)
lung_cognome = len(cognome)

print("Nome:", nome, ", ", "Lunghezza: ", lung_nome)
print("Cognome: ", cognome, ", ", "Lunghezza: ", lung_cognome)

