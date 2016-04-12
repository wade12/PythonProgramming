smallest = None
largest = None

soccur = 0
loccur = 0

print 'Type "Q" to quit this program.'

while True:
    strinput = raw_input("Enter integer: ")
    strinput = strinput.lower()
    if strinput == "q":
        break
    try:
        input = int(strinput)
        if (input < 0) or (100 < input):
            print "Integer must be between 0 and 100"
            continue
        if (smallest is None) or (input < smallest):
            smallest = input
            soccur = 1
        elif (input == smallest):
            soccur += 1
        if (largest is None) or (largest < input):
            largest = input
            loccur = 1
        elif (input == largest):
            loccur += 1      
    except:
        print "Invalid input.  Try again."

print "Largest integer: ", largest
print "Occurrences of largest: ", loccur
print "Smallest integer: ", smallest
print "Occurrences of smallest: ", soccur
        

