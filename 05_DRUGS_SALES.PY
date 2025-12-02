import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("PROJECT/DRUGS_SALES.CSV")
print(df.head())
df_label=df.copy()
df_encoded=pd.get_dummies(df_label,columns=['Region'])
le=LabelEncoder() # Creating object :
df_encoded['East']=le.fit_transform(df_encoded['Region_East'])
df_encoded['North']=le.fit_transform(df_encoded['Region_North'])
df_encoded['South']=le.fit_transform(df_encoded['Region_South'])
df_encoded['West']=le.fit_transform(df_encoded['Region_West'])
print(df_encoded.head())

def addrev(x,y):
    sum=0
    for i in range(0,1000):
        if y[i]==1:
            sum+=x[i]
    return sum

east_rev=addrev(df_encoded['Revenue'],df_encoded['Region_East'])
west_rev=addrev(df_encoded['Revenue'],df_encoded['Region_West'])
north_rev=addrev(df_encoded['Revenue'],df_encoded['Region_North'])
south_rev=addrev(df_encoded['Revenue'],df_encoded['Region_South'])

indexs=['East','West','North','South']
Totals=[east_rev,west_rev,north_rev,south_rev]
plt.legend()
plt.bar(indexs,Totals,width=.5,color="orange")
plt.title("Drugs revenue in each directions :")
plt.show()
 

