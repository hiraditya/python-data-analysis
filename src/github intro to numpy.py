import numpy

#creating a numpy array

new=numpy.array([1,3,7,8,14,11])

#to view this array simply input new

print(new)

#using arange command to input numbers automatically

new=numpy.arange(100)

#this will automatically include numbers from 0 to 99 without having users to input it

#now we will use reshape command to convert this 1D array to 2D array

new.reshape(25,4)

#this command will convert this 1D array to 25 rows and 4 Columns 2D array

#the end
