''' Εκφώνηση: Γράψτε μια συνάρτηση η οποία μετατρέπει ένα string σε αριθμό σύμφωνα με την αναπαράσταση των αριθμών σε ASCII 
code και μετά ελέγχει αν ο αριθμός είναι πρώτος. Για τον έλεγχο αν ένας αριθμός είναι πρώτος ΔΕΝ μπορείτε να χρησιμοποιήσετε
εξωτερική βιβλιοθήκη. '''

string = input("Give me a string: ")
mylist=[]


for i in range(len(string)):
    mylist.append(ord(string[i]))


x = int("".join(map(str, mylist)))


for i in range(2, x//2):
    if x % i == 0:
        print("The ASCII code for your string is %s and it's not a prime number." % (str(x)))
        break
else:
    print("The ASCII code for your string is %s and it is a prime number." % (str(x)))





