import random
x=random.randint(1,101)
n=-1
guesses=0
while(n!=x):
    guesses+=1
    n=int(input("Guess the number :"))
    if(n<x):
        print(f"guess higher than {n} :")
    else:
        print(f"guess lower than {n} :")
else:
    print(f"You correct number this time :{x}")

print(f"The number of guesses you tooked : {guesses}")
        