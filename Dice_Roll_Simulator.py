import numpy as np
import matplotlib.pyplot as plt
arr=np.array([0,0,0,0,0,0])
dice_arr=np.array([1,2,3,4,5,6])
print(dice_arr)
i=0
n=int(input("Enter number of time you want to roll :"))
while(i!=n):
    dice=np.random.randint(1,7)
    arr[dice-1]=arr[dice-1]+1
    print(dice_arr)
    print(arr,dice)
    i+=1
    
print(dice_arr)
print(arr)

maximum=np.max(arr)
indexof=np.where(arr==maximum)[0] +1
print(f"The maximum time rooled value is {indexof}")

# diagram :
x=list(dice_arr)
y=list(arr)
plt.bar(x,y,color='blue',label="Dice result :")
plt.show()
