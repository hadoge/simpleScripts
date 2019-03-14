#Script that opens a file and adds the words that aren't listed to a dictionary
f = open("words.txt")
D = {}
value = 0
for line in f:

    frase = line.split()
    for word in frase:

        value = value + 1
        if word not in D: D[word] = value

print(D)        
t = list(D.values())
        
