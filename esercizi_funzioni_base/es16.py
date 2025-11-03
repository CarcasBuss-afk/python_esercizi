# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo la differenza tra PRINT e RETURN nelle funzioni """

# DIFFERENZA TRA PRINT E RETURN
# - print(): stampa un valore a schermo ma NON lo restituisce
# - return: restituisce un valore che può essere usato successivamente
#
# Con return possiamo:
# 1. Salvare il risultato in una variabile
# 2. Usare il risultato in altri calcoli
# 3. Passare il risultato ad altre funzioni

# Funzione con PRINT (stampa ma non restituisce)
def somma_con_print(a, b):
    risultato = a + b
    print(risultato)

# Funzione con RETURN (restituisce il valore)
def somma_con_return(a, b):
    risultato = a + b
    return risultato

print("=== Con PRINT ===")
somma_con_print(5, 3)  # Stampa 8
# Non posso salvare il risultato!

print("\n=== Con RETURN ===")
valore = somma_con_return(5, 3)  # Restituisce 8
print(f"Valore salvato: {valore}")  # Posso usarlo!

# Ora posso fare altri calcoli con il valore
doppio = valore * 2
print(f"Il doppio è: {______}")

print("\n--- Separatore ---\n")

# DEFINISCI UNA FUNZIONE chiamata 'moltiplica' che prende due parametri (a, b)
# e RESTITUISCE il risultato di a * b (usa return, NON print)
___ moltiplica(_, _):
    ______ _ * _


# Chiama la funzione e salva il risultato
risultato = moltiplica(__, __)
print(f"Risultato: {_________}")

""" Osserva come return permette di riutilizzare il valore! """
