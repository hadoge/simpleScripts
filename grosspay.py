def computepay(hours, rate):

    hour = input("Enter Hours: ")
    try :
        a1 = float(hour)
    except :
        print("Error, please enter numeric input")
        quit()
        
    rate = input("Enter Rate: ")
    try :
        a2 = float(rate)
    except :
        print("Error, please enter numeric input")
        quit()
        
    if a1 > 40 :

        result = (a2 * 40) + ((a1 - 40) * (a2 * 1.5))
        print("Pay:",result)

    else :

        result = a1 * a2
        print("Pay:",result)

computepay(0,0)


