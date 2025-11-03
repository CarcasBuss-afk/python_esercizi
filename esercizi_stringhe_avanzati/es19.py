# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a verificare se due parole sono ANAGRAMMI.
Due parole sono anagrammi se contengono le stesse lettere nello stesso numero,
ma in ordine diverso. """

# ALGORITMO ANAGRAMMA
# Due parole sono anagrammi se, dopo averle ordinate alfabeticamente,
# risultano identiche.
#
# Esempio: "roma" e "amor"
# - "roma" ordinato = "amor"
# - "amor" ordinato = "amor"
# - Sono uguali → anagrammi!
#
# La funzione sorted() ordina i caratteri di una stringa
# e restituisce una lista di caratteri ordinati
# Esempio: sorted("roma") = ['a', 'm', 'o', 'r']

parola1 = "roma"
parola2 = "amor"

# Ordiniamo le lettere di entrambe le parole
parola1_ordinata = sorted(______)
parola2_ordinata = sorted(______)

print(f"'{parola1}' ordinato: {parola1_ordinata}")
print(f"'{parola2}' ordinato: {parola2_ordinata}")

# Confrontiamo le versioni ordinate
if parola1_ordinata __ parola2_ordinata:
    print(f"'{parola1}' e '{parola2}' sono anagrammi!")
____:
    print(f"'{parola1}' e '{parola2}' non sono anagrammi")

# CHIEDI ALL'UTENTE DUE PAROLE


# Convertiamo in minuscolo e verifichiamo se sono anagrammi
__ ______(parola_a.______()) == ______(parola_b.______()):
    print(f"'{parola_a}' e '{parola_b}' sono anagrammi!")
____:
    print(f"'{parola_a}' e '{parola_b}' non sono anagrammi")

""" Prova con: "roma/amor", "cane/ance", "casa/saca", "gatto/cane" """
