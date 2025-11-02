import random
# making function for random values :
s=["S","W","G"]
# robert function
def game(s):
    return random.choice(s) #pop retuns random valuse
# game loop :
# sentile control loop:
i=1 #decleration
i=int(input("Enter 1 if you want to play :"))
while(i==1):
    # taking user input :
    u=str(input(""""       Eneter \"S\" : for SNAKE \n
        Enter \"W\" : for WATER\n
        Enter \"G\" : for GUN :"""))
    U=u.capitalize()
    # print user input:
    if(U=="S"):
        print(f"You entered : SNAKE")
    elif(U=="W"):
        print(f"You enter : WATER ")
    elif(U=="G"):
        print(f"You entered : GUN")
    else:
        ("you entered wong value ?")
        i=int(input("Enter 1 if you want to try again else -1:"))
        continue
    # calling rober function:
    r=game(s)
    # print robert input:
    if(r=="S"):
        print(f"Robert enter : SNAKE")
    elif(r=="W"):
        print(f"Robert enter : WATER ")
    elif(r=="G"):
        print(f"Robert entered : GUN")
    # winner discision:
    if(U=="S" and r=="W"):
        print("You won")
    elif(U=="W" and r=="G"):
        print("You won")
    elif(U=="G" and r=="S"):
        print("You won")
    elif(U==r):
        print("Tie")
    else:
        print("You loss")
    i=int(input("Enter 1 if you want to play again else -1:"))
else:
    print("Thank you !")