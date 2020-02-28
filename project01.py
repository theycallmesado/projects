def project(filename):
    # This code opens and reads the file.
    with open(filename, 'r') as file:
        wordList = file.read().split()
        
    # This code finds the 5 longest words.
    resultList = []
    for i in range(5):
        x = (max(wordList, key=len))
        wordList.remove(x)
        resultList.append(x)

    # This code finds the vowels in each word and removes them.
    newList = []
    for i in resultList:
        for j in i:
            if j in "aeiouAEIOU":
                i = i.replace(j, "")
        newList.append(i)

    # This code reverses the words and prints them out.
    for i in newList:
        print(i[::-1])


# Asks for the name of the file and calls the project() function.
project(input("The name of the text file that you want me to read: ") + ".txt")
