# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: RIEPILOGO - Creare funzione cancella(id) completa.
"""

# IMPORTA LIBRERIE


# CREA FUNZIONE connessione()


# CREA FUNZIONE cancella(id)
# Deve:
# 1. Connettersi
# 2. DELETE FROM videogiochi WHERE id = %s
# 3. Fare commit()
# 4. Chiudere


print("TEST:")
conferma = input("Eliminare ID 999? (s/n): ").lower().strip()
if conferma == "s":
    cancella(999)
    print("Operazione completata")
