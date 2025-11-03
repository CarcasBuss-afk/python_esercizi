# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: funzioni che analizzano e modificano dizionari """

# DEFINISCI UNA FUNZIONE chiamata 'aggiungi_sconto' che prende un dizionario 'prodotto'
# (con chiavi: nome, prezzo) e una percentuale_sconto
# - Calcola il prezzo_scontato: prezzo - (prezzo * percentuale_sconto / 100)
# - Aggiunge al dizionario la chiave "prezzo_scontato"
# - RESTITUISCE il dizionario modificato
___ aggiungi_sconto(________, ___________________):
    prezzo = ________["______"]
    prezzo_scontato = ______ - (______ * ___________________ / ___)
    ________["_______________"] = _______________
    ______ ________


# Crea un prodotto
prodotto = {"nome": "Laptop", "prezzo": 1000}
print(f"Prodotto originale: {________}")

# Aggiungi lo sconto
prodotto_scontato = ______________(________, __)
print(f"Prodotto con sconto: {__________________}")

# DEFINISCI UNA FUNZIONE chiamata 'combina_dati_studente' che prende (nome, voti_lista)
# - Calcola la media dei voti
# - RESTITUISCE un dizionario con: nome, voti, media




# Crea dati studente
studente = _____________________("Marco", [7, 8, 9, 7])
print(f"Studente: {________}")

# DEFINISCI UNA FUNZIONE chiamata 'cerca_in_dizionario' che prende un dizionario e una 'chiave'
# - Se la chiave esiste: RESTITUISCE il valore
# - Se la chiave non esiste: RESTITUISCE "Chiave non trovata"
# Usa: if chiave in dizionario




# Dizionario di test
dati = {"nome": "Luigi", "eta": 30, "citta": "Milano"}

# Cerca chiavi
valore1 = __________________(____, "nome")
print(f"Nome: {_______}")

valore2 = __________________(____, "telefono")
print(f"Telefono: {_______}")

""" Prova con chiavi diverse """
