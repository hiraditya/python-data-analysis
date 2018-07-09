import numpy as nu
from matplotlib import pyplot as py

#creating a numpy array for numbers in range 15 to 20
x=nu.arange(15,20)
#creating a eqn of the required line
y=5*x+8
#plotting the required graph
py.xlabel("x axis")
py.ylabel("y axis")

py.plot(x,y)
