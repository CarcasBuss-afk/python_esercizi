# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a allineare e formattare stringhe usando i metodi di allineamento.
Creiamo testo centrato, allineato a sinistra e allineato a destra. """

# METODI DI ALLINEAMENTO
# .center(larghezza) = centra la stringa aggiungendo spazi
# .ljust(larghezza) = allinea a sinistra (left justify)
# .rjust(larghezza) = allinea a destra (right justify)
#
# Esempio: "Ciao".center(10) = "   Ciao   " (3 spazi prima, 3 dopo)
# Esempio: "Ciao".ljust(10) = "Ciao      " (6 spazi dopo)
# Esempio: "Ciao".rjust(10) = "      Ciao" (6 spazi prima)
#
# Si può anche specificare un carattere di riempimento:
# "Ciao".center(10, '*') = "***Ciao***"

titolo = "PYTHON"

# Centriamo il titolo in uno spazio di 30 caratteri
titolo_centrato = titolo.center(__)
print(titolo_centrato)

# Allineiamo a sinistra in 30 caratteri
titolo_sinistra = titolo.______(30)
print(titolo_sinistra)

# Allineiamo a destra in 30 caratteri
titolo_destra = titolo.______(__)
print(_____________)

# Usiamo caratteri di riempimento
titolo_decorato = titolo.center(30, ____)
print(titolo_decorato)

# CHIEDI ALL'UTENTE UN MESSAGGIO


# Centra il messaggio in 40 caratteri
messaggio_centrato = messaggio.______(__)
print(messaggio_centrato)

# Crea una cornice con caratteri '-'
linea = ______.center(__, ___)
print(_____)

""" Questi metodi sono utili per creare interfacce testuali """
