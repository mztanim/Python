import random
n=20
to_be_gussed= int (n*random.random())+1
guess=0

while guess != to_be_gussed:
    guess = int (input ("New Member: "))
    if guess>0:
        if guess > to_be_gussed:
            print ("number too large")
        elif guess < to_be_gussed:
            print("Number too small")
    else:
          print ("sorry")
          break
else:
    print ("Winner")
