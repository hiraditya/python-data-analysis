from pandas import DataFrame

#creating a dictionary structure which later will be converted to DataFrame

dic1={"Name":["harsh","anil","priya"],"Age":[28,19,18],"Percent":[75,81,89]}

df1=DataFrame(dic1)
#sorting the DataFrame
#we have 2 methods to sort the DataFrame- sort by index and sort by values
#it is quite evident from their naming

df2=df1.sort_values("Percent")

#the above line of code will sort the entire DataFrame in ascending order of Percentage

df2=df1.sort_index()

#the above line of code will sort the DataFrame in increasing index ie 0,1,2.


#now we will learn on how to sort a series

new=Series([7,4,3] ,index=["Japan","S.Korea","India"])

new.sort_values()

#the above line of code will sort the following in increasing no of goals ie Japan.S.Korea,India
#the end
