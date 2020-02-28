''' Εκφώνηση: Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει έναν αριθμό, τον τριπλασιάζει, προσθέτει ένα και
στην συνέχεια προσθέτει τα ψηφία του. Η διαδικασία επαναμβάνεται μέχρι ο αριθμός να γίνει μονοψήφιος. '''

while True:
    try:
        x = abs(int(input("Give me a number: ")))
    except ValueError:
        print("Try again. ", end="")
        continue
    break


while True:
    x = (x * 3 + 1)
    z = 0
    while x > 0:
        k = x % 10
        z = z + k
        x = int(x/10)
    if z >= 10:
        x = z
        continue
    else:
        break
print(z)
