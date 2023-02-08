
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt

tercode = int(input("Enter terrain code (Mountains 1, hills 2, plateaus 3, plains 4): "))
rin = int(input("Enter the amount of rainfall in your region: "))
sol = int(input("Enter the soil type of your area(sand (1), clay (2), silt (3), peat (4), chalk and loam (5)): "))
co2 = int(input("Enter the C02 Emission in the region: "))

appli = pd.read_csv("data.csv")

X = appli.drop(columns = ["tress"])
y = appli["tress"]

model = DecisionTreeClassifier()

model.fit(X, y)

predct = model.predict([[tercode, rin, sol,co2]])

stor = predct

print(stor) #Improve the database + Proff dena tha

#####################################################################################################

rate = co2 / 10
index = 0
decrease = []

while(co2 > 0):
    decrease.append(co2)
    co2 = co2 - rate
    index += 1
    
year = [1,2,3,4,5,6,7,8,9,10,11]

x_values = year
y_values = decrease

plt.plot(x_values, y_values)

plt.show()