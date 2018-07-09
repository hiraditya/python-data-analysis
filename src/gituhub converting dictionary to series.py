from pandas import Series

# in this lecture we will learn to create series from dictionary
# we will take name of students and their age

da1={"anil":26,"harsh":19,"priya":18}
da2=Series(da1)

#here the key becomes the index and values as the particular value of that index

#to access age of let's say priya we will have to input

da2["priya"]

#this will return us the age of priya which is 18

#the end
