from pandas import DataFrame

dic1={"cse":[15,11,13],"maths":[5,7,6],"english":[15,17,18]}

df1=DataFrame(dic1)

#calculating the sum of individual columns

df1.sum()

#calculating the sum of individual rows

df1.sum(axis=1)
#here axis =1 represents the horizontal axis

#calculating the maximum values for each individual columns
#results will in the form of displayed index

df1.idxmax()

#similarly for minimum values for each individual columns

df1.idxmin()

#fundamental operations on DataFrames like addition,subtraction etc

dic2={"cse":[10,13,11],"maths":[11,14,17],"english":[5,7,9],"ece":[11,13,15]}
df2=DataFrame(dic2)

##adding df1+df2

df1+df2

#when we add df1+df2 the corresponding index gets added up by matching with column name
#ie cse[0]of df1 gets added with cse[1] of df2 and so on
#but since we dont have column for ece in df1 so we get something in final result as Nan ie not a number
#same is the case with series

#the end.
