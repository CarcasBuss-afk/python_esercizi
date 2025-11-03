# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a dividere una stringa in parti usando .split().
Dividiamo una frase in parole e contiamo quante parole ci sono. """

# Il metodo .split() divide una stringa in una LISTA di sottostringhe
# basandosi su un separatore (delimitatore)
#
# Sintassi: stringa.split(separatore)
# - Se non specifichi il separatore, .split() usa lo spazio come default
# - Restituisce una LISTA di stringhe
#
# Esempio: "Ciao mondo python".split() = ["Ciao", "mondo", "python"]
# Esempio: "rosso,verde,blu".split(',') = ["rosso", "verde", "blu"]

frase = "Python è un linguaggio di programmazione"

# Dividiamo la frase in parole usando .split()
parole = frase.split()
print(f"Frase: {frase}")
print(f"Lista di parole: {______}")

# Contiamo quante parole ci sono
numero_parole = len(______)
print(f"Numero di parole: {_____________}")

# Stampiamo ogni parola su una riga separata
print("\nParole separate:")
for parola in ______:
    print(f"- {______}")

# CHIEDI ALL'UTENTE DI INSERIRE UNA FRASE


# Dividi la frase in parole
parole_utente = _____________.______()

# CONTA E STAMPA IL NUMERO DI PAROLE



""" Prova con frasi diverse """
