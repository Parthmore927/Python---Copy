import pandas as pd;

data = {
    'toy' : ['animal','block','car','stuff','animal','car','block','stuff'],
    'colour' : ['brown','blue','red','yellow','brown','red','blue','yellow'],
    'count' : [5,3,8,3,1,4,3,7]
}

df = pd.DataFrame(data)
print("Following is the dataframe : ")
print(df)

#grouping on the basis of the toy 
grouped = df.groupby('toy')
result = grouped['count'].sum()
print("Count of each toy : ")
print(result)

#finding average count in each toy type
avg = df.groupby('toy')['count'].mean()
print("Average count of each toy : ")
print(avg)

#finding maximum count in each toy type
maxi = df.groupby('toy')['count'].max()
print("Maximum count of each toy : ")
print(maxi)

#finding minimum count in each toy type
mini = df.groupby('toy')['count'].min()
print("Minimum count of each toy : ")
print(mini)

#finding total no. of enteries
enteries = df.groupby('toy').size()
print("Total no. of enteries : ")
print(enteries)