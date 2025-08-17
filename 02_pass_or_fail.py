# minum percentage in each subject have to >=33%
# total percentage should be 40%
name=str(input("Enter your name :"))
m=int(input("Eneter percentage in Math :")) # math
s=int(input("Enter percentage in Science :")) # science
e=int(input("Enter percentage in English :")) #english
# total percentage :
t=(m+s+e)/3
# condition
if((m>=33 and s>=33 and e>=33 )and t>=40):
    print(f"{name} you are pass : total percentage is {t}")
elif(m>=33 and s>=33 and e>=33 ):
    print(f"your total percenage {t} is less than 40%")
elif(m<33 and s<33 and e<33):
    print(f"You are fail in Math({m}) , Science({s}) and English({e})")
elif(s<33 and e<33):
    print(f"You are fail in Science({s}) and English({e})")
elif(m<33 and e<33):
    print(f"You are fail in Math({m}) and English({e})")
elif(s<33 and m<33):
    print(f"You are fail in Science({s}) and Math({e})")    
elif(m<33):
    print(f"You are fail in Math({m})")
elif(s<33):
    print(f"You are fail in Science({s})")
elif(e<33):
    print(f"You are fail in English({e})")
