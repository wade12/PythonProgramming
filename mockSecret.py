while True:
    strsecret = raw_input("Set secret number: ")
    try:
        secret = int(strsecret)
        if (secret < 0) or (100 < secret):
            print "Secret number must be between 1 and 100."
            continue
        else:
            break
    except:
        print "Invalid input."
 
count = 0
while True:
    strguess = raw_input("Guess secret number: ")
    count += 1
    try:
        guess = int(strguess)
        if (guess < 0) or (100 < guess):
            print "Guess must be between 1 and 100."
            continue
        if guess == secret:
            print "Congrats!"
            print "You only took", count, "guesses"
            break
        elif guess < secret:
            print "Guess higher."
        elif secret < guess:
            print "Guess lower."
        else:
            print "Houston, we have a problem!"
    except:
        print "Invalid guess."
        