#Esercizio 1: Creare una lista di numeri interi e stampare solo gli elementi che sono divisibili per 3.
lista = [1,2,3,4,5,6,7,8,9,10]
for m in lista:
    if m % 3 == 0:
        print(m)
#Esercizio 2: Creare una tupla di stringhe e stampare solo le stringhe di lunghezza pari.
tupla = ("ciao", "bao", "miao")
for m in tupla:
    if len(m) % 2 == 0:
        print(m)
#Esercizio 3: Creare un set e una lista di numeri interi. Stampare solo i numeri che sono presenti sia nel 
#set che nella lista.
set = {1,23,4,50,34,2,45,0}
lista = [1,223,40,50,6,5,4,32,12,10]

for s in set:
    for l in lista:
        if s == l:
            print(s)
#Esercizio 4: Creare un dizionario in cui le chiavi sono stringhe e i valori sono numeri interi. 
#Stampare solo le coppie chiave-valore in cui il valore è maggiore di 5.
dizionario = {"chiave1":3, "chiave2":20, "chiave3":30}

for k,v in dizionario.items():
    if v > 5:
        print(k,v)
#Esercizio 5: Creare una lista_di_tuple, in cui ogni tupla contiene due stringhe. 
#Stampare le tuple in cui la prima stringa inizia con la lettera ‘a’.
lista_di_tuple = [("albero", "pino"), ("casa", "villa"), ("auto", "bmw")]
for tupla in lista_di_tuple:
    if tupla[0][0] == "a":
        print(tupla)
#Esercizio 6: Creare un set_di_tuple in cui ogni tupla contiene due numeri interi. 
#Stampare le tuple in cui la somma dei due numeri è pari.
set_di_tuple = {(23,45), (22,42), (1,2)}
for set in set_di_tuple:
    if (set[0]+set[1]) & 2 == 0:
        print(set)