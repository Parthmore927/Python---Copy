import pandas as pd
var = {
    "SUBJECT" : ["Maths","Science","Economy"],
    "MARKS" : [96,87,97]
}

myVar = pd.DataFrame(var)
#myVar = pd.Series(var,index=['>','>','>'])
#print(myVar)

print("Printing a specific row using loc attribute :")
print(myVar.loc[[0,2]])

# giving our own names to the indexes 
myVar = pd.DataFrame(var,index=["1","2","3"])
print(myVar)