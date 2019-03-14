#words count

def count(a, b):
    
    c = 0
    for i in a:
        
        if i == b :
            
            c = c + 1
            
    return c

word = count("I knew you would come, but i didn't know how", "o")
print(word)


