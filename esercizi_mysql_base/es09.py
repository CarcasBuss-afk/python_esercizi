# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: RIEPILOGO - Creare funzione elenco(ricerca_='') completa con LIKE.
Questa è la funzione finale di videogiochi.py!
"""

# IMPORTA LIBRERIE


# CREA FUNZIONE connessione()


# CREA FUNZIONE elenco(ricerca_="")
# Deve:
# 1. Connettersi
# 2. Usare LIKE con f"{ricerca_}%"
# 3. Restituire risultati


print("TEST:")
print("1. Ricerca 'Mine':")
giochi = elenco("Mine")
for g in giochi:
    print(f"  - {g[1]}")

print("\n2. Tutti i giochi:")
tutti = elenco("")
print(f"  Totale: {len(tutti)}")
