import numpy as np

np.absolute(-5)

#numpy array
a=np.array([1,2,3,4])
print(a)

print(type(a))

#dimensions od array
a.shape

#2D array
b=np.array([[1,2,3,4],[5,6,7,8]])

print(b)
b.shape

#Transpose
print(b.T)
b.T.shape

np.dot(b,b.T)

np.random.randint(60,100,10)
#random numbers from 60-100,10 such numbers

#to generate matrix instead of numbers
matrix=np.random.randint(60,100,(5,5))
print(matrix)

np.max(matrix)

np.min(matrix)

k=np.array([0,1,10,10,2,-8,6,6,6,6,8,10])

#gives index of minimum element
np.argmin(k)

#number of unique elements
np.unique(k)

print(np.unique(k))

g=np.unique(k,return_counts=True)
print(g)
print(g[0])
print(g[1])

#program to find out number with highest frequency in an array
g=np.unique(k,return_counts=True)
print(g)

idx=np.argmax(g[1])#highest frequency
element=g[0][idx]
print(element)

#slicing
#start:end+1 because end is not included
matrix

matrix[2:4,1:4]
#find element
matrix[0][0]
