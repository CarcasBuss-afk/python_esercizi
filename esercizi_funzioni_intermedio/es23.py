# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" MINI-PROGETTO: Calcolatrice Scientifica con Menu
Combina: parametri default, return multiplo, composizione, validazione """

# DEFINISCI UNA FUNZIONE chiamata 'potenza' che prende (base, esponente=2)
# e RESTITUISCE base ** esponente
___ potenza(____, _________=2):
    ______ ____ ** _________


# DEFINISCI UNA FUNZIONE chiamata 'radice_quadrata' che prende 'numero'
# e RESTITUISCE numero ** 0.5
___ radice_quadrata(______):
    ______ ______ ** 0.5


# DEFINISCI UNA FUNZIONE chiamata 'operazioni_complete' che prende (num1, num2)
# e RESTITUISCE (somma, sottrazione, moltiplicazione, divisione)
___ operazioni_complete(____, ____):
    somma = ____ + ____
    sottrazione = ____ - ____
    moltiplicazione = ____ * ____
    divisione = ____ / ____
    ______ _____, ___________, _______________, _________


# DEFINISCI UNA FUNZIONE chiamata 'valida_numero' che prende 'testo'
# - Se può essere convertito in float: RESTITUISCE (True, float(testo))
# - Altrimenti: RESTITUISCE (False, 0)
# Usa try/except per gestire l'errore
___ valida_numero(_____):
    try:
        numero = float(_____)
        ______ ____, ______
    except:
        ______ _____, _


# DEFINISCI UNA FUNZIONE chiamata 'mostra_menu' che stampa:
# "=== CALCOLATRICE ==="
# "1. Operazioni base (somma, sottrazione, moltiplicazione, divisione)"
# "2. Potenza"
# "3. Radice quadrata"
# "4. Esci"
___ mostra_menu():
    print("=== CALCOLATRICE ===")
    print("1. Operazioni base")
    print("2. Potenza")
    print("3. Radice quadrata")
    print("4. Esci")


# Programma principale
while True:
    mostra_menu()
    scelta = input("\nScegli un'opzione: ")

    if scelta == "_":
        # Operazioni base
        num1_input = input("Primo numero: ")
        valido1, num1 = _____________(__________)

        num2_input = input("Secondo numero: ")
        valido2, num2 = _____________(__________)

        if valido1 ___ valido2:
            s, sot, m, d = ___________________(____, ____)
            print(f"\nSomma: {_}")
            print(f"Sottrazione: {___}")
            print(f"Moltiplicazione: {_}")
            print(f"Divisione: {_}")
        ____:
            print("Errore: inserisci numeri validi")

    elif scelta == "_":
        # Potenza
        base_input = input("Base: ")
        valido_base, base = _____________(__________)

        if valido_base:
            usa_default = input("Vuoi usare esponente 2? (si/no): ")
            if usa_default == "si":
                risultato = _______(____)
            ____:
                esp_input = input("Esponente: ")
                valido_esp, esp = _____________(________)
                if valido_esp:
                    risultato = _______(_____, ___)
                ____:
                    print("Errore: esponente non valido")
                    continue
            print(f"\nRisultato: {_________}")
        ____:
            print("Errore: base non valida")

    elif scelta == "_":
        # Radice quadrata
        num_input = input("Numero: ")
        valido, num = _____________(________)

        if valido ___ num __ 0:
            risultato = _______________(___)
            print(f"\nRisultato: {_________}")
        ____:
            print("Errore: numero non valido o negativo")

    elif scelta == "_":
        print("Arrivederci!")
        break
    ____:
        print("Opzione non valida")

    print()  # Riga vuota

""" Testa tutte le funzionalità! """
