#Esercizio 1: Scrivere una funzione che accetti una lista di interi e restituisca una lista di tuple, 
#dove ogni tupla contenga l’elemento e il suo indice nella lista originale. Ad esempio, se la funzione 
#viene chiamata con la lista [4, 5, 6, 7], dovrebbe restituire [(4, 0), (5, 1), (6, 2), (7, 3)].
def Esercizio1 (numeri):
    risultato = []
    for n in numeri:
    #[(n, 0), (5, 1), (6, 2), (7, 3)]

   
#Esercizio 2: Creare una funzione che accetti una lista di stringhe e restituisca un dizionario dove 
#le chiavi sono le stringhe e i valori sono il numero di volte in cui ogni stringa appare nella lista.
#Ad esempio, se la funzione viene chiamata con la lista [‘ciao’, ‘mondo’, ‘ciao’, ‘mondo’, ‘mondo’], 
#dovrebbe restituire {‘ciao’: 2, ‘mondo’: 3}.

#Esercizio 3: Scrivere una funzione che accetti una lista di interi e restituisca il numero di elementi
#pari presenti nella lista. Ad esempio, se la funzione viene chiamata con la lista [1, 2, 3, 4, 5], 
#dovrebbe restituire 2.

#Esercizio 4: Scrivere una funzione che accetti una stringa e un carattere di ricerca e restituisca il numero 
#di volte in cui il carattere appare nella stringa. Ad esempio, se la funzione viene chiamata con la stringa ‘ciao’ 
#e il carattere ‘o’, dovrebbe restituire 1.

#Esercizio 5: Scrivere una funzione che accetti una lista di interi e restituisca una lista di interi contenente 
#solo i numeri divisibili per 3. Ad esempio, se la funzione viene chiamata con la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 
#10], dovrebbe restituire [3, 6, 9].