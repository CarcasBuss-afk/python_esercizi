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
    print("abbonato", nome)

def calcola_costo_mensile(ore_settimanali):
    costo = ore_settimanali * 15
    print("Costo mensile:", costo)

def verifica_livello(anni_esperienza):
   if anni_esperienza >= 5:
       print("Livello: esperto")
   elif anni_esperienza >= 2:
       print("Livello: intermedio")
   else:
       print("Livello: principiante")

nome_imput = input("Come ti chiami ")
nome = str(nome_imput)

ore_settimanali_imput = input("Quante ore settimanali pensa di fare ")
ore_settimanali = int(ore_settimanali_imput)

anni_esperienza_imput = input("Da quanti anni fa palestra ")
anni_esperienza = int(anni_esperienza_imput)


stampa_nome_abbonato(nome)
calcola_costo_mensile(ore_settimanali)
verifica_livello(anni_esperienza)










# SCRIVI IL PROGRAMMA PRINCIPALE QUI








