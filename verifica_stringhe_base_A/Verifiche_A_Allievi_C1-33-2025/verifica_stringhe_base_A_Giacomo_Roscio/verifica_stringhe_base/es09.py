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
nome = input("Inserisci il tuo nome:  ")
n_nome = len(nome)
nome1 = input("Inserisci il tuo cognome:  ")
n_nome1 = len(nome1)
print(f"{nome}, lunghezza: {n_nome} ")
print(f"{nome1}, lunghezza: {n_nome1} ")