import pandas as pd     #For Reading CSV file
from sklearn.tree import DecisionTreeClassifier     #For using the prediction model
from matplotlib import pyplot as plt    #For plotting the graph

tercode = int(input("Enter terrain code (Mountains 1, hills 2, plateaus 3, plains 4): "))

sol = int(input("Enter the soil type of your area(sand (1), clay (2), silt (3), peat (4), chalk and loam (5)): "))

rin = int(input("Enter the amount of rainfall in your region: "))

appli = pd.read_csv("/home/rupees/Programming/Python/data.csv") # Reading the CSV file

X = appli.drop(columns = ["tress"])     #setting the parameters
y = appli["tress"]      #settig the drop collumn

model = DecisionTreeClassifier()

model.fit(X, y)     # Fitting the collumns in the prediction model

predct = model.predict([[tercode, rin, sol]])   #Training the model

stor = predct

print(stor) # Prints the prediction

#####################################################################################################

co2 = int(input("Enter the C02 Emission in the region: "))
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