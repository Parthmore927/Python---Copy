import pandas as pd;
print("Imported Successfully")
var = pd.read_csv(r'C:\Users\Aryan\Desktop.csv')
new_var = var.dropna()

#printing the entire datasets
print("Following is the entire dataset :")
print(new_var.to_string())

#identifying duplicate rows
print(new_var.duplicated())

#removing duplicates
new_var.drop_duplicates(inplace = True)

#printing the entire datasets again but with no duplicates
print("Following is the entire dataset but without duplicates :")
print(new_var.to_string())
