# Riepilogo .strip() e validazione

""" SCOPO: Chiedi all'utente di inserire un codice coupon.
Rimuovi gli spazi all'inizio e alla fine del codice.
Se il codice pulito, è uguale a "SCONTO20" stampa "Coupon valido", altrimenti "Coupon non valido". """

""" Output atteso (esempi):
Inserisci il codice coupon:   SCONTO20
Coupon valido

Inserisci il codice coupon: SCONTO10
Coupon non valido
"""

# Scrivi il codice qui sotto

codice = input("Inserisci un codice coupon: ")
codice.strip()
if codice == "SCONTO20":
    print("Coupon valido")
else:
    print("Coupon non valido")
