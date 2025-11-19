# Riepilogo len()

""" SCOPO: Chiedi all'utente di inserire il proprio nome e cognome (due input separati).
Calcola la lunghezza di entrambi.
Stampa "Nome: [nome], Lunghezza: [lunghezza_nome]"
Stampa "Cognome: [cognome], Lunghezza: [lunghezza_cognome]" """

nome = input("Inserisci il tuo nome: ")
lunghezza_nome = len(nome)

cognome = input("Inserisci il tuo cognome: ")
lunghezza_cognome = len(cognome)

print("Nome: ", nome, ", ",  "Lunghezza: ", lunghezza_nome)
print("Cognome:", cognome, ", ", "Lunghezza: ", lunghezza_cognome)
""" Output atteso (esempio):
Inserisci il tuo nome: Marco
Inserisci il tuo cognome: Bianchi
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
"""
