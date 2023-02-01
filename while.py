#Esercizio 1: Scrivi un programma che chiede all’utente di inserire un numero intero. 
#Continua a chiedere all’utente di inserire un numero finché non viene inserito un numero pari.
numero = 1
while not numero % 2 == 0:
    numero = int(input("Inserisco intero pari: "))

#Esercizio 2: Scrivi un programma che stampa i numeri da 1 a 100.
n = 1
while n <= 100:
    print(n) 
    n += 1
#Esercizio 3: Scrivi un programma che chiede all’utente di inserire un numero intero.
#Continua a chiedere all’utente di inserire un numero finché non viene inserito un numero multiplo di 3.
while True:
    num = int(input("Inserisco intero divisibile per 3: "))

    if num % 3 == 0:
        break
    else:
        "Numero non divisibile per tre"
#Esercizio 4: Scrivi un programma che chiede all’utente di inserire una parola. 
#Continua a chiedere all’utente di inserire una parola finché la parola inserita non è “ciao”.
while True:
    parola = input("Inserisci parola ciao: ")

    if parola.lower() == "ciao":
        break
#Esercizio 5: Scrivi un programma che stampa i numeri pari da 1 a 100.
n = 2
while n <= 100:
    print(n) 
    n += 2
#Esercizio 6: Scrivi un programma che chiede all’utente di inserire una lettera. 
#Continua a chiedere all’utente di inserire una lettera finché la lettera inserita non è una vocale.
while True:
    lettera = input("Inserisci vocale: ")

    if lettera.lower() not in "aeiou":
        break
#Esercizio 7: Scrivi un programma che stampa i numeri multipli di 3 e 25 compresi tra 1 e 1000.
n = 1
while n <= 1000:
    if n % 3 == 0 and n % 25 == 0:
        print(n) 
    n += 1
#Esercizio 8: Scrivi un programma che chiede all’utente di inserire un numero intero. 
#Continua a chiedere all’utente di inserire un numero finché non viene inserito un numero intero compreso 
#tra 1 e 100.
num = 0
while True:
    num = int(input("Inserisco intero da 1 a 100: "))

    if 1 <= num <= 100:
        break
    else:
        "Numero non tra 1 e 100"
#Esercizio 9: Scrivi un programma che chiede all’utente di inserire una parola. 
#Continua a chiedere all’utente di inserire una parola finché la parola inserita non è lunga almeno 8 caratteri.
while True:
    lettera = input("Inserisci parola 8 caratteri: ")

    if len(lettera) >= 8:
        break