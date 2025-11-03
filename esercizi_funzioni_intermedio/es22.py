# SFIDA! Se questo esercizio ti sembra troppo difficile, puoi passare al successivo
# Riepilogo es20 e es21
""" SCOPO: Sistema di gestione rubrica telefonica con dizionari.

Crea un sistema di rubrica usando funzioni e dizionari.

Definisci queste funzioni:

1. crea_contatto(nome, telefono, email, citta)
   - RESTITUISCE un dizionario con tutte queste informazioni

2. mostra_contatto(contatto)
   - Stampa tutte le informazioni del contatto in modo formattato
   - Esempio: "=== CONTATTO ===\nNome: ...\nTelefono: ...\n..."

3. modifica_telefono(contatto, nuovo_telefono)
   - Modifica il telefono nel dizionario contatto
   - RESTITUISCE il contatto modificato

4. cerca_contatti_per_citta(lista_contatti, citta)
   - Prende una lista di dizionari contatto
   - RESTITUISCE una lista con solo i contatti di quella città

5. conta_contatti_per_citta(lista_contatti)
   - RESTITUISCE un dizionario con: {"citta1": conteggio1, "citta2": conteggio2, ...}
   - Esempio: {"Roma": 2, "Milano": 1}

Il programma deve:
- Creare una lista vuota per i contatti
- Chiedere all'utente quanti contatti vuole inserire
- Per ogni contatto, chiedere: nome, telefono, email, città
- Usare crea_contatto() e aggiungere alla lista
- Mostrare tutti i contatti usando mostra_contatto()
- Chiedere una città e mostrare solo i contatti di quella città
- Mostrare le statistiche per città

Esempio output:
  === CONTATTO 1 ===
  Nome: Mario Rossi
  Telefono: 3401234567
  Email: mario@test.com
  Città: Roma

  Contatti a Roma: 2
  Contatti a Milano: 1

Suggerimento: usa cicli for per gestire la lista di contatti! """
