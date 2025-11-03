# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: chiediamo all'utente un messaggio. Creiamo un messaggio "criptato" dove i caratteri
in posizioni pari sono in maiuscolo e quelli in posizioni dispari sono in minuscolo.
Esempio: "ciao" diventa "CiAo" """

# CHIEDI ALL'UTENTE DI INSERIRE UN MESSAGGIO


# Estraiamo i caratteri in posizioni pari e convertiamoli in maiuscolo
caratteri_pari = messaggio[___].______()

# Estraiamo i caratteri in posizioni dispari e convertiamoli in minuscolo
caratteri_dispari = messaggio[___].______()

# Ora dobbiamo ricostruire il messaggio alternando i caratteri
# Usiamo un ciclo per farlo
messaggio_criptato = ""
for i in range(len(caratteri_pari)):
    messaggio_criptato = messaggio_criptato + caratteri_pari[i]
    if i < len(caratteri_dispari):
        messaggio_criptato = messaggio_criptato + caratteri_dispari[i]

# Se c'è un carattere dispari in più, lo aggiungiamo alla fine
if len(caratteri_dispari) > len(caratteri_pari):
    messaggio_criptato = messaggio_criptato + ________________[-1]

# STAMPA IL MESSAGGIO ORIGINALE E QUELLO CRIPTATO



""" Prova con: "programmazione", "python", "ciao mondo" """
