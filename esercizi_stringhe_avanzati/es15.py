# Riepilogo es13 e es14
""" SCOPO: Chiedi all'utente una lista di nomi separati da virgola.
Dividi la stringa, rimuovi eventuali spazi all'inizio e fine di ogni nome,
e crea tre output diversi:
1. Nomi separati da " | " (pipe con spazi)
2. Nomi separati da " - " (trattino con spazi)
3. Nomi separati da newline "\n" (uno per riga)

Esempio:
- Input: "Mario, Luigi , Anna,  Carlo"
- Output 1: "Mario | Luigi | Anna | Carlo"
- Output 2: "Mario - Luigi - Anna - Carlo"
- Output 3:
  Mario
  Luigi
  Anna
  Carlo

Suggerimento: usa .split(','), poi un ciclo per fare .strip() su ogni nome,
e infine .join() per i tre formati diversi. """
