import random
x=random.randint(1,101)
n=-1
guessee=1
while(n!=x):
    n=int(input("Guess the number :"))
    if(x>n):
        print(f"please guess higher than {n}:")
        guessee+=1
    else:
        print(f"please guess lower than {n}:")
        guessee+=1
else:
    print(f"You guess the correct number this timme : {x}")

print(f"Number of gusses needed :{guessee}")
        
