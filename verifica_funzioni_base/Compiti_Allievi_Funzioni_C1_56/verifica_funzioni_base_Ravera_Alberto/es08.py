# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" Riepilogo: funzioni con un parametro

Crea un programma per gestire abbonamenti palestra.

Definisci queste funzioni:

1. stampa_nome_abbonato(nome) - stampa "Abbonato: [nome]"

2. calcola_costo_mensile(ore_settimanali) - stampa "Costo mensile: €[costo]"
   Formula: costo = ore_settimanali * 15

3. verifica_livello(anni_esperienza) - stampa il livello:
   - Se anni_esperienza >= 5: "Livello: Esperto"
   - Se anni_esperienza >= 2: "Livello: Intermedio"
   - Altrimenti: "Livello: Principiante"

Il programma deve:
- Chiedere nome, ore settimanali e anni di esperienza all'utente
- Chiamare le tre funzioni passando i valori inseriti
"""

# DEFINISCI LE FUNZIONI QUI

def stampa_nome_abbonato(nome):
   print(f"Abbonato: {nome}")

def calcola_costo_mensile(ore_settimanali):
   costo = ore_settimanali * 15
   print(f"Costo mensile {costo}")

def verifica_livello(anni_esperienza):
   print(f"Anni di seperienza: {anni_esperienza}")
   if anni_esperienza >= 5:
      print("Livello eserto")
   elif anni_esperienza >= 2:
      print("Livello: Intermedio")
   else:
      print("Livello: Principiante")


# SCRIVI IL PROGRAMMA PRINCIPALE QUI
nome = input("Inserisci il nome con cui ti sei iscritto: ")

ore_settimanali = int(input("Inserisci quante ore a settimana vai: "))

anni_esperienza = int(input("Inserisci gi anni di esperienza che hai: "))

stampa_nome_abbonato(nome)

calcola_costo_mensile(ore_settimanali)

verifica_livello(anni_esperienza)









