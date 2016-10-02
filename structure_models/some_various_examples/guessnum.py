import random

number = int(random.randint(0, 100))
name = raw_input("Hi! I'd like to play a little game with you. What in your name?: ")
print "OK, %s, I think of a number between 0 and 100. Guess it!" % name
while True:
    mynum = int(raw_input("Type a number.. "))
    if mynum == number:
        print "You finaly did it %s, my number is %s." % (name, mynum)
        break
    elif mynum > 100:
        print "From zero to HUNDRED, you dumass fuck!"
    elif mynum < 0:
        print "From ZERO to hundred, you dumass fuck!"
    elif mynum > number:
        print "Nope. Go down."
    elif mynum < number:
        print "Nope. Go up."
