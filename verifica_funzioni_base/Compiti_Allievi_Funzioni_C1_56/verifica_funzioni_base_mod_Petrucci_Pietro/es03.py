# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: menu con funzioni """

# DEFINISCI UNA FUNZIONE chiamata 'mostra_menu' che stampa:
# "1. Visualizza prodotti"
# "2. Aggiungi al carrello"
# "3. Esci"
def mostra_menu():
    print("1. Visualizza prodotti")
    print("2. Aggiungi al carrello")
    print("3. Esci")


# DEFINISCI UNA FUNZIONE chiamata 'mostra_prodotti' che stampa:
# "Prodotti disponibili: Laptop, Mouse, Tastiera"
def mostra_prodotti():
    print("Prodotti disponibili: Laptop, Mouse, Tastiera")


# DEFINISCI UNA FUNZIONE chiamata 'mostra_carrello' che stampa:
# "Hai aggiunto un prodotto al carrello"
def mostra_carrello():
    print("Hai aggiunto un prodotto al carrello")


# DEFINISCI UNA FUNZIONE chiamata 'mostra_uscita' che stampa:
# "Grazie per gli acquisti!"
def mostra_uscita():
    print("Grazie per gli acquisti!")


# Programma principale
# CHIAMA mostra_menu
mostra_menu()

scelta = input("\nScegli un'opzione: ")

if scelta == "1":
    # CHIAMA mostra_prodotti
    mostra_prodotti()
elif scelta == "2":
    # CHIAMA mostra_carrello
    mostra_carrello()
elif scelta == "3":
    # CHIAMA mostra_uscita
    mostra_uscita()
else:
    print("Opzione non valida")
