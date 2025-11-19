# Riepilogo finale - Validazione codice prodotto

""" SCOPO: Chiedi all'utente di inserire un codice prodotto.
Prima pulisci il codice rimuovendo gli spazi e convertendo in maiuscolo.
Il codice è valido se soddisfa TUTTE queste condizioni:
- ha una lunghezza esatta di 7 caratteri
- contiene il simbolo '-' (trattino)
- inizia con "ABC"
Se tutte le condizioni sono vere stampa "Codice valido", altrimenti "Codice non valido". """

""" Output atteso (esempi):
Inserisci un codice prodotto:   abc-123
Codice valido

Inserisci un codice prodotto: ABC-12
Codice non valido

Inserisci un codice prodotto: DEF-123
Codice non valido

Inserisci un codice prodotto: ABC1234
Codice non valido
"""

# Scrivi il codice qui sotto

cod = input("Inserisci il codice prodotto: ")
cod = cod.upper()
cod = cod.strip()
lung = len(cod)

if lung == 7 and "-" in cod and cod.startswith("ABC"):
    print("CODICE VALIDO")
else: 
    print("CODICE NON VALIDO")