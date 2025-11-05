# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con tre parametri """

# DEFINISCI UNA FUNZIONE chiamata 'calcola_media' che prende 'voto1', 'voto2', 'voto3'
# e stampa "Media: [media]"
# Formula: media = (voto1 + voto2 + voto3) / 3
def calcola_media(voto1, voto2, voto3):
    calc = (voto1 + voto2 + voto3) / 3
    print("Media:", calc)


# DEFINISCI UNA FUNZIONE chiamata 'stampa_prodotto' che prende 'nome', 'prezzo', 'quantita'
# e stampa "Prodotto: [nome], Prezzo: €[prezzo], Quantità: [quantita]"
def stampa_prodotto(nome, prezzo, quantita):
    print(f"Prodotto:", {nome}, ", Prezzo: €", {prezzo}, ", Quantità:", {quantita})


# Programma principale
v1 = int(input("Voto 1: "))
v2 = int(input("Voto 2: "))
v3 = int(input("Voto 3: "))
# CHIAMA calcola_media
calcola_media(v1, v2, v3)

nome = input("Nome prodotto: ")
prezzo = int(input("Prezzo: "))
qta = int(input("Quantità: "))
# CHIAMA stampa_prodotto
stampa_prodotto(nome, prezzo, qta)
