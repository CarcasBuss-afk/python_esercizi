# Riepilogo operatore in e .count()

""" SCOPO: Chiedi all'utente di inserire una frase.
Converti la frase in minuscolo.
Conta quante volte appare la lettera 'a' nella frase.
Stampa "La lettera 'a' appare [numero] volte".
Se appare più di 3 volte stampa "Ci sono molte 'a'!", altrimenti "Ci sono poche 'a'". """

frase = input("Inserisci una frase: ")
frase_minuscola = frase.lower()
numero = frase.count("a")
print(f"La lettera A compare {numero} volte")
""" Output atteso (esempi):
Inserisci una frase: La casa ha tante stanze
La lettera 'a' appare 6 volte
Ci sono molte 'a'!

Inserisci una frase: Ciao mondo
La lettera 'a' appare 1 volte
Ci sono poche 'a'
"""
