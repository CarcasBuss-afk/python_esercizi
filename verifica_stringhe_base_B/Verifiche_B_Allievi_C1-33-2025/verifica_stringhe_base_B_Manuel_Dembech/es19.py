# Riepilogo validazione username

""" SCOPO: Chiedi all'utente di inserire uno username.
Prima pulisci lo username rimuovendo gli spazi e convertendo in minuscolo.
Lo username è valido se soddisfa TUTTE queste condizioni:
- NON contiene spazi (dopo la pulizia lo username originale e quello pulito devono essere uguali in lunghezza)
- ha una lunghezza tra 5 e 15 caratteri
- contiene almeno un numero
Se tutte le condizioni sono vere stampa "Username valido", altrimenti "Username non valido". """

""" Output atteso (esempi):
Inserisci uno username: Gamer99
Username valido

Inserisci uno username: User Name
Username non valido

Inserisci uno username: abc
Username non valido

Inserisci uno username: player
Username non valido
"""
# Scrivi il codice qui sotto

username = input("Inserisci uno username: ")

username_minuscolo = username.lower()

username_pulito = username.strip()

lunghezza_username = len(username)
lunghezza_username_pulito = len(username_pulito)


if (lunghezza_username == lunghezza_username_pulito) and () and (username.isdecimal == True):
    print("Username valido")
else:
    print("Username non valido")