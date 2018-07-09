from pandas import Series

# creating a new series

data1=Series(["anil","harsh","priya"])

#accessing a particluar index of Series: in this case data1 and we will access the
#index 2 of series which on turn will return us priya
data1[2]

# giving index of our choice to Series

data2=Series(["anil","harsh","priya"],index=["student1","student2","student3"])

#accessing the particular index of the series created with new name
#suppose we want to access student2 of the particular series

data2["student2"]

#this will return us "priya"


#the end

