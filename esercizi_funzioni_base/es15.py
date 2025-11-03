# SFIDA! Se questo esercizio ti sembra troppo difficile, puoi passare al successivo
# Riepilogo es09-14
""" SCOPO: Crea una funzione calcolatrice che prende tre parametri e usa input dell'utente.

Definisci la funzione:
- Nome: calcola
- Parametri: num1, num2, operazione
- Comportamento:
  * Se operazione è "somma": stampa "num1 + num2 = risultato"
  * Se operazione è "sottrazione": stampa "num1 - num2 = risultato"
  * Se operazione è "moltiplicazione": stampa "num1 * num2 = risultato"
  * Se operazione è "divisione": stampa "num1 / num2 = risultato"
  * Altrimenti: stampa "Operazione non valida"

Dopo aver definito la funzione, chiedi all'utente di inserire:
- Il primo numero (converti in float)
- Il secondo numero (converti in float)
- L'operazione (stringa: "somma", "sottrazione", "moltiplicazione", "divisione")

Infine, chiama la funzione calcola con i valori inseriti dall'utente.

Suggerimento: usa if/elif/else dentro la funzione per controllare l'operazione

--- BONUS (solo se hai completato l'esercizio principale) ---
Se vuoi migliorare la funzione, fai in modo che accetti l'operazione indipendentemente
da maiuscole/minuscole. Ad esempio: "SOMMA", "Somma", "somma" devono funzionare tutti.
Suggerimento: usa .lower() sul parametro operazione prima di fare i confronti. """
