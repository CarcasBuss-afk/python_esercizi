# SFIDA! Se questo esercizio ti sembra troppo difficile, puoi passare al successivo
# Riepilogo es17 e es18
""" SCOPO: Sistema di gestione voti con statistiche complete.

Crea funzioni per analizzare una lista di voti.

Definisci queste funzioni:

1. calcola_statistiche(voti)
   - RESTITUISCE (con return multiplo): media, minimo, massimo
   - Usa sum(), len(), min(), max()

2. conta_per_giudizio(voti)
   - RESTITUISCE (con return multiplo):
     * numero di voti >= 9 (ottimo)
     * numero di voti >= 7 e < 9 (buono)
     * numero di voti >= 6 e < 7 (sufficiente)
     * numero di voti < 6 (insufficiente)

3. filtra_voti_sopra_media(voti, media)
   - RESTITUISCE una lista con solo i voti >= media

4. stampa_report(voti)
   - Non restituisce niente, solo stampa
   - Usa le funzioni sopra per creare un report completo:
     * Stampa tutti i voti
     * Stampa media, minimo, massimo
     * Stampa conteggio per giudizio
     * Stampa voti sopra la media

Il programma deve:
- Chiedere all'utente quanti voti vuole inserire
- Chiedere ogni voto uno per uno (usa un ciclo for)
- Salvare tutti i voti in una lista
- Chiamare stampa_report(voti) per mostrare l'analisi completa

Esempio output:
  === REPORT VOTI ===
  Voti inseriti: [7, 8, 6, 9, 7, 5]
  Media: 7.0
  Minimo: 5
  Massimo: 9
  Ottimi (>=9): 1
  Buoni (7-8): 3
  Sufficienti (6): 1
  Insufficienti (<6): 1
  Voti sopra la media: [8, 9]

Suggerimento: costruisci le funzioni una alla volta e testale separatamente! """
