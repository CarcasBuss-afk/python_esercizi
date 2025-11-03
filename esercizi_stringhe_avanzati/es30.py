# Riepilogo es28 e es29
""" SCOPO: Crea un DECIFRATORE per il cifrario di Cesare. Chiedi all'utente un messaggio
cifrato e lo shift usato per cifrarlo. Decifra il messaggio.

La decifratura è semplicemente il processo inverso: invece di aggiungere lo shift,
lo sottraiamo. Oppure possiamo usare uno shift negativo o shift di (26 - shift_originale).

Esempio:
- Messaggio cifrato: "FLDER" (cifrato con shift 3)
- Shift: 3
- Messaggio decifrato: "CIAO"

Il programma deve:
1. Chiedere il messaggio cifrato
2. Chiedere lo shift usato per cifrarlo
3. Decifrare il messaggio (shift negativo o sottrarre lo shift)
4. Gestire maiuscole, minuscole e caratteri speciali
5. Stampare il messaggio decifrato

Suggerimento: per decifrare, usa (codice - shift) invece di (codice + shift),
e gestisci il wrap around all'indietro (se vai sotto A, vai a Z). """
