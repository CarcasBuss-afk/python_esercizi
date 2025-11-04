# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni con validazione """

# DEFINISCI UNA FUNZIONE chiamata 'valida_voto' che prende 'voto'
# - Se voto >= 60: stampa "Promosso"
# - Altrimenti: stampa "Bocciato"
def validita_voto(voto):
    if voto >= 60:
        print("Promosso")
    else:
        print("Bocciato")


# DEFINISCI UNA FUNZIONE chiamata 'calcola_sconto_eta' che prende 'prezzo' e 'eta'
# - Se eta < 18: applica sconto 20% e stampa "Prezzo scontato: €[prezzo_scontato]"
# - Se eta >= 65: applica sconto 30% e stampa "Prezzo scontato: €[prezzo_scontato]"
# - Altrimenti: stampa "Prezzo pieno: €[prezzo]"
# Formula sconto: prezzo_scontato = prezzo - (prezzo * percentuale / 100)
def calcola_sconto_eta(prezzo, eta):
    if eta < 18:
        percentuale = 20
        prezzo_scontato = prezzo - (prezzo * percentuale / 100)
        print(f"Prezzo scontato: €{prezzo_scontato}")
    elif eta >= 65:
        percentuale = 30
        prezzo_scontato = prezzo - (prezzo * percentuale / 100)
        print(f"Prezzo scontato: €{prezzo_scontato}")
    else:
        print(f"Prezzo pieno: €{prezzo}")
    


# Programma principale
voto = int(input("Inserisci il voto: "))
# CHIAMA valida_voto
validita_voto(voto)

prezzo_biglietto = int(input("Prezzo biglietto: "))
eta_utente = int(input("Età: "))
# CHIAMA calcola_sconto_eta
calcola_sconto_eta(prezzo_biglietto, eta_utente)
