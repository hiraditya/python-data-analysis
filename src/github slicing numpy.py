import numpy

#creating numpy array from 0 to 19 ie total 20 numbers

a=numpy.arange(20)

#slicing a numpy means to cut between the array to get desired result

b=slice(3,17,2)

#it will slice the array from index 3 to index 17 with a gap of 2 elements

print(a[b])
#this will print the sliced numpy array

#the end
