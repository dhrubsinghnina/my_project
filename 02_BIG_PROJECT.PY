from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing csv file
data=pd.read_csv("PROJECT/student_data_1000.csv")

# making lables
X = data[['hours']]  # ensure X is 2D (DataFrame) for sklearn
y = data[['marks']]

# creating object of the model:
model = LinearRegression()
# train:
model.fit(X, y)
pred = model.predict(X)

# valid regression metrics:
mae = mean_absolute_error(y, pred)
mse = mean_squared_error(y, pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, pred)  # actual,predicted coficient to detemision 1-best 0-bad 0> worst

print(f"the mean_absolute_error:{round(mae,2)}")
print(f"the mean_squared_error:{round(mse,2)}")
print(f"the root_mean squared_error:{round(rmse,2)}")
print(f"The r2_score is :{round(r2,4)}")

# ploting graph:
plt.figure(figsize=(10,10)) # width,height
plt.hist(data['marks'],bins=25,color='skyblue',edgecolor='black')
plt.title("Distribution of final exam score :")
plt.xlabel("marks")
plt.ylabel("number of student")
plt.grid(True)
plt.show()
# scater + regression line :
plt.figure(figsize=(10,7))
plt.scatter(X,y,color='blue',label='Actual score')
plt.plot(X,pred,color='red',label='predicted score regresion line')
plt.title("MOdel prediction vs actual score :")
plt.xlabel("hours")
plt.ylabel("marks")
plt.grid(True)
plt.show()