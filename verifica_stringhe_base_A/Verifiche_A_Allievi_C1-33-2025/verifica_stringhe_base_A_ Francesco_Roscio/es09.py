# Riepilogo len()

""" SCOPO: Chiedi all'utente di inserire il proprio nome e cognome (due input separati).
Calcola la lunghezza di entrambi.
Stampa "Nome: [nome], Lunghezza: [lunghezza_nome]"
Stampa "Cognome: [cognome], Lunghezza: [lunghezza_cognome]" """

nome = input ("inserisci il tuo nome: ")
cognome = input ("inserisci il to cognome: ")




lunghezza_nome= len(nome)
lunghezza_cognome= len(cognome)
print("nome:", nome,", i caratteri sono:", lunghezza_nome,)
print("cognome:", cognome,",e i caratteri sono:", lunghezza_cognome,)



""" Output atteso (esempio):
Inserisci il tuo nome: Marco
Inserisci il tuo cognome: Bianchi
Nome: Marco, Lunghezza: 5
Cognome: Bianchi, Lunghezza: 7
"""
