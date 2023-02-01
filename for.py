#Esercizio 1: Creare una variabile parola con un valore casuale. Mandare a schermo ciascuna lettera della parola.
parola = "parola"
for p in parola:
    print(p)
#Esercizio 2: Creare una variabile lista con valori a scelta e mandarli a schermo con un ciclo for.
lista = ["parola", "cane", "blu", "rosso"]
for m in lista:
    print(m)

#Esercizio 3: Mandare a schermo solo i numeri pari nel range() tra 5 e 100 (non compreso).
for n in range(2,100,2):
    print(n)
#Esercizio 4: Stampare con print() tutti i nomi delle celle di una scacchiera sapendo che le righe sono numerate 
#e le colonne nominate con lettere.
righe = range(1,9)
colonne = ["a", "b", "c", "d", "e", "f", "g", "h"]

for c in colonne:
    for riga in righe:
        print(c + str(riga))
#Esercizio 5: Creare una lista = ["parola", "parola"...] inserendo un numero a piacere di parole.
#Mandare a schermo tutte le parole con lunghezza pari ed in aggiunta le singole vocali che le compongono.
parole = ["rossi", "luca", "edoardo", "marco", "anna"]
for parola in parole:
    if len(parola) % 2 == 0:
        print(parola)
        for lettera in parola:
            if lettera in "aeiou":
                print(lettera)
#Esercizio 6: Creare due liste di numeri separate. Iterare la prima lista e mandare a schermo il numero 
#solo se parte anche della seconda.
numero1 = [1,2,3,4,5]
numero2 = [6,7,3,9,5]
for i1 in numero1:
    for i2 in numero2:
        if i1 == i2:
            print(i1)