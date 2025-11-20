# COMPLETA IL CODICE DOVE TROVI ________ !

"""
SCOPO: RIEPILOGO - Creare funzioni per input validato.
"""

# CREA FUNZIONE chiedi_anno()
# Deve:
# 1. while True
# 2. try/except per int()
# 3. Verificare 1980 <= anno <= 2024
# 4. return anno se valido


# CREA FUNZIONE chiedi_prezzo()
# Deve:
# 1. while True
# 2. try/except per float()
# 3. .replace(",", ".")
# 4. Verificare prezzo >= 0
# 5. return prezzo se valido


# CREA FUNZIONE chiedi_conferma(messaggio)
# Deve:
# 1. input(messaggio + " (s/n): ")
# 2. .lower().strip()
# 3. return True se "s", False altrimenti


print("TEST:")
anno = chiedi_anno()
prezzo = chiedi_prezzo()
if chiedi_conferma("Salvare?"):
    print(f"Salvato: {anno}, €{prezzo}")
