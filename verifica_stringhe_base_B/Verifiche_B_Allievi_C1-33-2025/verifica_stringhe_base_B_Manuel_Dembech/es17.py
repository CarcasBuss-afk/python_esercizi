# COMPLETA IL CODICE DOVE TROVI ________ !

""" SCOPO del programma: contare gli spazi in una descrizione e classificarla come corta o lunga """

# Chiedi all'utente di inserire una descrizione prodotto
descrizione = input("Inserisci una descrizione prodotto: ")

# Conta quanti spazi ci sono
numero_spazi = descrizione.count(" ")

# Stampa quanti spazi ci sono
print(f"La descrizione contiene {numero_spazi} spazi")

# Verifica se la descrizione è lunga (più di 5 spazi)
if numero_spazi > 5:
    print("Descrizione lunga")
else:
    print("Descrizione corta")

""" Output atteso (esempi):
Inserisci una descrizione prodotto: Smartphone con fotocamera ad alta risoluzione
La descrizione contiene 5 spazi
Descrizione corta

Inserisci una descrizione prodotto: Questo è un ottimo prodotto di alta qualità
La descrizione contiene 8 spazi
Descrizione lunga
"""
