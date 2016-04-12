print "Type 'q' to quit"
marks = []
i = 1
counta = countb = countc = countd = countf = 0

while True:
    strmark = raw_input('Enter mark for Student %d: ' %i)
    strmark = strmark.lower()
    if strmark == 'q':
        break
    try:
        mark = int(strmark)
        if (mark < 0) or (100 < mark):
            print "Mark must be between 0 and 100"
            continue
        if 70 < mark:
            grade = 'A'
            counta += 1
        if 60 < mark:
            grade = 'B'
            countb += 1
        if 50 < mark:
            grade = 'C'
            countc += 1
        if 40 < mark:
            grade = 'D'
            countd += 1
        else:
            grade = 'F'
            countf += 1
        marks.append(mark)
        i += 1
    except:
        print "Invalid input. Try again."

if len(marks) > 0:
    average = sum(marks) / len(marks)
    average = round(average,2)
    print "Average: \t", average
    print "\tGrade \tCount"
    grades = ['A', 'B', 'C', 'D', 'F']
    for grade in grades:
        if grade == 'A':
            print "\t", grade, "\t", counta
        elif grade == 'B':
            print "\t", grade, "\t", countb
        elif grade == 'C':
            print "\t", grade, "\t", countc
        elif grade == 'D':
            print "\t", grade, "\t", countd
        else:
            print "\t", grade, "\t", countf
    
        
        
        
        
        
        
        
        
        
        