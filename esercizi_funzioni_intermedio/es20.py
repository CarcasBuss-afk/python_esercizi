# COMPLETA IL CODICE DOVE TROVI ________ !
# QUANDO CI SONO I COMMENTI IN MAIUSCOLO SIGINIFCA CHE DEVI SCRIVERE TU
# IL CODICE IN BASE A QUANTO RICHIESTO NEL COMMENTO

""" SCOPO: impariamo a creare funzioni che lavorano con i DIZIONARI """

# I DIZIONARI sono strutture dati che associano chiavi a valori
# Sintassi: {"chiave1": valore1, "chiave2": valore2}
#
# Le funzioni possono:
# - Creare dizionari
# - Leggere valori
# - Modificare valori
# - Analizzare dizionari

# Funzione che crea un dizionario persona
def crea_persona(nome, eta, citta):
    persona = {
        "nome": nome,
        "eta": eta,
        "citta": citta
    }
    return persona

# Testiamo
mario = crea_persona("Mario", 25, "Roma")
print(f"Persona: {mario}")
print(f"Nome: {mario['nome']}")

print("\n--- Separatore ---\n")

# DEFINISCI UNA FUNZIONE chiamata 'crea_libro' che prende (titolo, autore, anno)
# e RESTITUISCE un dizionario con queste chiavi
___ crea_libro(______, ______, ____):
    libro = {
        "______": ______,
        "______": ______,
        "____": ____
    }
    ______ _____


# Crea un libro
libro1 = __________(_______, _______, ____)
print(f"Libro: {______}")

# DEFINISCI UNA FUNZIONE chiamata 'mostra_contatto' che prende un dizionario 'contatto'
# e stampa: "Nome: [nome], Tel: [telefono], Email: [email]"
___ mostra_contatto(________):
    print(f"Nome: {________['____']}, Tel: {________['________']}, Email: {________['_____']}")


# Crea un dizionario contatto
contatto = {
    "nome": "Anna Rossi",
    "telefono": "3401234567",
    "email": "anna@test.com"
}

# Mostra il contatto
_______________(________)

# DEFINISCI UNA FUNZIONE chiamata 'calcola_eta_da_anno' che prende 'anno_nascita'
# e RESTITUISCE un dizionario con: anno_nascita e eta_attuale (2025 - anno_nascita)




# Usa la funzione
info_eta = ___________________(____)
print(f"Info età: {________}")

""" Osserva come i dizionari organizzano i dati in modo strutturato! """
