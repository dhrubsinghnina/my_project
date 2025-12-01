import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

df=pd.read_csv("PROJECT/master_income_dataset.csv")
print(df.head())
le=LabelEncoder()
df_label=df.copy()
le=LabelEncoder() # Creating object :
df_label['MasterDegree_x']=le.fit_transform(df_label['MasterDegree'])
df_label['IncomeMoreThan1Lakh_y']=le.fit_transform(df_label['IncomeMoreThan1Lakh'])
print("\n Labele encoded :")
print(df_label[['MasterDegree','MasterDegree_x','IncomeMoreThan1Lakh','IncomeMoreThan1Lakh_y']].head(10))

yes_master=df_label['MasterDegree_x'].sum()
no_master=1000-yes_master
print(yes_master,no_master)

yes_lakh=df_label['IncomeMoreThan1Lakh_y'].sum()
no_lakh=1000-yes_lakh
print(yes_lakh,no_lakh)

Master_arr=np.array([df_label['MasterDegree_x']])
lakh_arr=np.array([df_label['IncomeMoreThan1Lakh_y']])

yes_yes=Master_arr*lakh_arr
total_yes_yes=yes_yes.sum()
yes_no=(Master_arr-lakh_arr)*Master_arr
total_yes_no=yes_no.sum()
no_yes=(lakh_arr-Master_arr)*lakh_arr
total_no_yes=no_yes.sum()
total_no_no=1000-(total_yes_yes+total_yes_no+total_no_yes)

indexs=['Master_lakh','Master_nolakh','Nomaster_lakh','Nomaster_nolakh']
Totals=[total_yes_yes,total_yes_no,total_no_yes,total_no_no]
plt.legend()
plt.bar(indexs,Totals,width=.5,color="orange")
plt.title("Income comparison")
plt.xlabel("Master degree with income")
plt.ylabel("Number of Persons")
plt.legend()
plt.show()


plt.pie(Totals,labels=indexs,autopct='%1.1f%%',colors=['yellow','green','red','brown'])
plt.title("Revnue of states :")
plt.show()