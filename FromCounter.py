#Script opens a mail and print and counts each line that starts with From
f = open("supermail.txt")
count = 0
for line in f:

    word = line.split()
    if len(word) is not 0 and word[0] == "From":
        count = count + 1 
        print(word[1])

print("There were %d lines with From as the first word" % (count))
