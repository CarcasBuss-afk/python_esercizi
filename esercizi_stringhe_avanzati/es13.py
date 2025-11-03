# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a unire una lista di stringhe in un'unica stringa usando .join().
Creiamo una frase da una lista di parole. """

# Il metodo .join() è l'opposto di .split()
# Unisce gli elementi di una LISTA in un'unica stringa
# usando un separatore
#
# Sintassi: separatore.join(lista)
# ATTENZIONE: il separatore va PRIMA del .join()!
#
# Esempio: " ".join(["Ciao", "mondo"]) = "Ciao mondo"
# Esempio: "-".join(["2025", "01", "15"]) = "2025-01-15"
# Esempio: "".join(["P", "y", "t", "h", "o", "n"]) = "Python"

parole = ["Python", "è", "fantastico"]

# Uniamo le parole con uno spazio
frase = " ".join(______)
print(f"Lista di parole: {parole}")
print(f"Frase unita: {______}")

# Uniamo le parole con un trattino
frase_trattino = _____.join(______)
print(f"Con trattino: {______________}")

# Uniamo senza separatore
frase_senza_spazi = ___.join(______)
print(f"Senza spazi: {_________________}")

# CREA UNA LISTA CON 4 NOMI DI CITTÀ
citta = [______, ______, ______, ______]

# Unisci le città con ", " (virgola e spazio)
elenco_citta = _____.join(_____)

# STAMPA L'ELENCO DELLE CITTÀ


""" Osserva come .join() è utile per formattare output """
