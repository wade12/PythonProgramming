while True:
    name = raw_input("Enter name: ")
    if name.isalpha():
        break
    else:
        print "Name not recognised.  Try again."
    
while True:
    strhours = raw_input("Enter hours: ")
    try:
        hours = float(strhours)
        if (hours < 0) or (168 < hours):
            print "Hours must be between 0 and 168"
            continue
        break
    except:
        print "Invalid input"
        
while True:
    strrate = raw_input("Enter rate: ")
    try:
        rate = float(strrate)
        if (rate < 0) or (168 < rate):
            print "Rate must be between 0 and 250"
            continue
        break
    except:
        print "Invalid input"
        
while True:
    strtax = raw_input("Enter tax rate: ")
    try:
        tax = float(strtax)
        if (tax < 0) or (168 < tax):
            print "Tax rate must be between 0 and 100"
            continue
        break
    except:
        print "Invalid input"
        
def computepay(hours, rate, tax):
    if (hours <= 40):
        grossPay = hours * rate
    else:
        grossPay = (40 * rate) + ((hours-40)*(1.5*rate))
    taxDeduct = (tax/100) * grossPay
    netPay = grossPay - taxDeduct
    return grossPay, taxDeduct, netPay

grossPay, taxDeduct, netPay = computepay(hours, rate, tax)

print "Name: \t\t", name
print "Gross Pay: \t", round(grossPay,2)
print "Tax Deduct: \t", round(taxDeduct,2)
print "Net Pay: \t", round(netPay,2)
        
        
        
        
        
        
        
        