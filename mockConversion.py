print "Type 'q' to quit this program."

while True:
    streuro = raw_input("Enter Euro: ")
    streuro = streuro.lower()
    if streuro == 'q':
        quit()
    try:
        euro = int(streuro)
        if (0 < euro):
            break
        else:
            print "Euro amount must be greater than zero."
    except:
        print "Invalid input.  Try again."

while True:
    strconvert = raw_input("Choose currency: 'd', 'p' or 'y': ")
    strconvert = strconvert.lower()
    if strconvert =='q':
        quit()
    currencies = ['d', 'p', 'y']
    if strconvert in currencies:
        print "Calculating conversion now."
        break
    else:
        print "Invalid choice.  Try again."
    

def conversion(euro):
    if strconvert == 'd':
        result = euro * 1.35
    elif strconvert == 'p':
        result = euro * 0.78
    elif strconvert == 'y':
        result = euro * 110.23
    else:
        print "Oops! ... we shouldn't be here!"
    return result

result = conversion(euro)

print "Your %.2f euro converts to %.2f at current exchange rate." %(euro, result)

    