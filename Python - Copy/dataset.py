import pandas as pd
myDataSet = {
    "cars" : ["volvo","BMW","audi","jaguar"],
    "owners" : [23,53,21,22]
}

myVar = pd.DataFrame(myDataSet)

print(myVar)