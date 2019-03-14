inp = input("Enter a spell: ")
spell = str(inp)
lenght = len(inp)
index = (lenght-1)

for letter in spell:

    print(spell[index])
    index = index - 1

print("CONGRATS, IT SPELLS BACKWARDS!")

while True:

    f = input("Press K and ENTER to exit: ")
    result = str(f)
    if result == "k": break
