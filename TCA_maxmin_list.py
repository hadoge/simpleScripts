numberCount = 0
total = 0
inu = []
maximum = None
minimum = None

while True:
    
    line = input("Enter a number: ")
    
    if line == "done":
        
        break
    
    try:
        lastInp = float(line)
        
        if maximum == None or lastInp > maximum:
            
            maximum = lastInp
            
        if minimum == None or lastInp < minimum:
            
            minimum = lastInp
            
        numberCount = numberCount + 1
        total = total + lastInp
        inu = inu + [line]
        
    except:
        
        print("Invalid input")
        continue

result = numberCount, total
print("Number Count, Total:", result)
print("Maximum:", max(inu))
print("Minimunm:", min(inu))
