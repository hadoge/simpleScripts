#Script made for learn diferences on list modification

t = [2,1,3,4,5]
p = [2,1,3,4,5]

def chop(b):

    a = (len(b)) - 1
    del b[a]
    del b[0]
    return None #This function returns None, while the list is modified.

def middle(b):

    a = (len(b)) - 1
    return b[1:a] #This function returns a new Value, leaving the list unmodified

chop(p)
print(p)
print(chop(p))

middle(t)
print(t)
print(middle(t))


