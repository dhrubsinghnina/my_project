import numpy as np
import matplotlib.pyplot as plt

arr=np.array([0,0])
coin=["H","T"]
i=0
while(i!=1000):
    toss=np.random.randint(0,2)
    arr[toss]+=1
    print(coin)
    print(arr)
    i+=1
    
res=list(arr)

plt.pie(res,labels=coin,autopct='%1.1f%%')
plt.show()