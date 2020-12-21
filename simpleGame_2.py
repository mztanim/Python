import random
number=1
while number>0:
    random_number= random.randrange(1,11)
    number = int(input("enter a number between 1 to 10, 0 to exit: "))

    if number == random_number:
        print ("U r lucky")
    else:
        print ("Thank you")
else:
    print ("Thank you")