from pandas import DataFrame

#creating a dictionary structure which later will be converted to DataFrame

dic1={"Name":["harsh","anil","priya"],"Age":[28,19,18],"Percent":[75,81,89]}

df1=DataFrame(dic1)

#accessing a particular column in DataFrame

df1["Name"]
df1["Age"]
df1["Percent"]

#accessing a particular row in DataFrame
df1.iloc[0]
df1.iloc[1]
df1.iloc[2]

#some version support iloc and some support ix.Please check for the same.

#transposing the given dataframe

df2=df1.T
# Now we have transposed dataframe as df2 and normal dataframe as df1

#changing column sequence as per our wish in DataFrame

df3=DataFrame(dic1, columns=["Age","Name","Percent"])

#the ends
