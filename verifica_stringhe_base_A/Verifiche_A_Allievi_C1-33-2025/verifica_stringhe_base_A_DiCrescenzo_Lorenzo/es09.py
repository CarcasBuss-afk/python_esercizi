# Riepilogo len()

""" SCOPO: Chiedi all'utente di inserire il proprio nome e cognome (due input separati).
Calcola la lunghezza di entrambi.
Stampa "Nome: [nome], Lunghezza: [lunghezza_nome]"
Stampa "Cognome: [cognome], Lunghezza: [lunghezza_cognome]" """
nome = input("inserisci il tuo nome: ")
cognome = input("inserisci il tuo cognome: ")
lunghezza_n = len(nome)
lunghezza_co = len(cognome)
print(f"Nome: {nome} lunghezza: {lunghezza_n}")
print(f"cognome: {cognome} lunghezza: {lunghezza_co}")



""" Output atteso (esempio):
Inserisci il tuo nome: Marco
Inserisci il tuo cognome: Bianchi
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
"""
