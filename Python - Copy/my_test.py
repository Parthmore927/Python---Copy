import pandas as pd

#loading the sa csv file into the program:
var = pd.read_csv('sa.csv')

#printing all the datasets:
print(var.to_string())

#using the corr() method to find the relation among columns:
print("Following is the co relation : ")
#giving only numerical values to the corr() :
new_var = var.select_dtypes('number')
correlation = new_var.corr()
print("The corelation : ")
print(correlation)