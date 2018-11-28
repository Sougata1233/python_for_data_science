# It is the foundation on which all higher level tools for scientific Python are built.
# Here are some of the functionalities it provides:

# N- Dimensional array, a fast and memory efficient multidimensional array providing vectorized arithmetic 
# operations.
# You can apply standard mathematical operations on arrays of entire data without writing loops.
# It is very easy to transfer data to external libraries written in a low-level language (such as C or C++), 
# and also for external libraries to return data to Python as Numpy arrays.Linear algebra, Fourier transforms 
# and random number generation.

# NumPy does not provide high-level data analysis functionality, 
# having an understanding of NumPy arrays and array-oriented computing will help you use tools like Pandas
# much more effectively.




import numpy as np
from numpy import random

age = [10,11,12,13,14,15,16,25,21,42,32]
ages = [[21, 20, 23, 56, 21, 45], [12, 25, 56, 25]]
arr = np.array(ages)
print(arr)
print(arr.dtype) #returns data type
print(arr.ndim) #returns dimension of the array
print(arr.shape) #returns number of rows and columns
print(np.zeros((4,3))) #creating multi dimensional array with 0s
print(np.arange(10)) #aranging 0-9
print(np.eye(4)) #creates NxN identity matrix
print(ages[0])

#Batch operations on data can be performed without using for loops, this is called vectorization
arr2 = np.array(age)
print(arr2)
print(arr2*arr2)
print(arr2-arr2)
print(1/arr2)
print(arr2**0.5)

#indexing and slicing
arr3 = np.arange(12)
print(arr3)
print(arr3[4])
print(arr3[3:9])
arr3[3:9] = 32
print(arr3)

#treat array like matrices
list1 = [[1,2,3],[2,3,4],[5,6,9]]
arr4 = np.array(list1)
print(arr4)
print(arr4[0])
print(arr4[0][1])

from IPython.display import Image 
from IPython import display

i = Image(filename='logo.png')
print(i._FMT_PNG)
# display(i)

#3d array
threeD = np.array([[[1,2,3],[7,8,9]],[[5,6,4],[5,9,3]]])
print(threeD)
print("Returning second list of first list: ".format(threeD))
print(threeD[0])
print(threeD[0,1])
print(threeD[0,1,0])

#copying array
copies_array = threeD.copy()
print("copied array "+str(copies_array))
copied_value = threeD[0].copy()
copied_value1 = threeD[0,1].copy()
copied_value2 = threeD[0,1,1].copy()
print("****************")
print(copied_value)
print(copied_value1)
print(copied_value2)

print("*******checking a value in array**************")
personals = np.array(['Manu', 'Jeevan', 'Prakash', 'Manu', 'Prakash', 'Jeevan', 'Prakash'])
print(personals == 'Manu') #checks for the string 'Manu' in personals. If present it returns true; else false#

print("***********numpy random********")
#numpy random
print(random.randn(1,7))
print("*****")
print(random.randn(10,7))
print("******")
ran_no = random.randn(7,3)
print(ran_no[personals=='Manu'])
print("*********")
print(ran_no[ran_no<0])


#Fancy Indexing or Indexing using Integer Arrays
print("Fancy Indexing or Indexing using Integer Arrays")
algebra = random.randn(7,4)
for j in range(7):
    algebra[j] = j
print(algebra)
print("subset of rows")
print(algebra[[4,5,1]])
print("reshape an array")
print(np.arange(36).reshape(12,3))
print("the position of the output array are[(1,3),(4,2),(3,1),(2,0)]")
fancy = np.arange(36).reshape(9,4)
print(fancy)
print("****")
print(fancy[[1,4,3,2],[3,2,1,0]])
print("entire first row is selected, but the elements are interchanged, same goes for 4th, 8th and 2 nd row.")
print(fancy[[1, 4, 8, 2]][:, [0, 3, 1, 2]])
print(fancy[np.ix_([1,4,8,2],[0,3,1,2])])

#Transposing Arrays
print("Transposing Arrays")
transpose = np.arange(12).reshape(3,4)
print("original")
print(transpose)
print("after transpose")
print(transpose.T)
print("dot product of transpose and original matrix")
print(np.dot(transpose, transpose.T))

#Universal Functions
print("Universal Functions")
funky = np.arange(8)
print("unary functions")
print("square root")
print(np.sqrt(funky))
print("exponent")
print(np.exp(funky))

print("Binary functions")
print("Binary functions take two value")
x = random.randn(10)
y = random.randn(10)
print("value of x "+str(x))
print("value of y "+str(y))
print("This is element wise operation")
print("value of max: "+str(np.maximum(x,y)))
print("function modf returns the fractional and integral parts of a floating point arrays")
print("value of mod "+ str(np.modf(x,y)))

#Data processing using array
print("Data processing using array")
