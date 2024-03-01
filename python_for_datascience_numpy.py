# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:27:46 2023

@author: Dell
"""
#numpy
#it is open source library
#it is use for scientific computing application
#it is stand for numerical python
#which is consisting of multi dimentional array
#install [python numpy library
#1)go to base terminal and open prompt
#2)pip install numpy
#3)install numpy using conda
#conda installl numpy
#python list contain different data type with in single list
#but python array contain similar dadatype
#Array In Numpy
#crreat ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)
#output-[10,20,30]
##############################
#create multidimentional array
import numpy as np
arr = np.array([[10,20.30],[40,50,60]])
print(arr)
#output-[[10,20.30],
#        [40,50,60]]
#repreresnt the minimum dimention
#use ndmin param to specifiy how many minimum
#dimention you wanted to create an array with minimum dimension
arr=np.array([10,20,30,40],ndmin=3)
print(arr)
##########################################
#change the datatype
#dtype parameter
arr=np.array([10,20,30],dtype = complex)
print(arr)
###################################
#Get the dimension of array
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)
###############################
#find the size of each items in array
arr=np.array([10,20,30])
print("Each item is of the type",arr.dtype)
######################################
#get the shape and size of the array
import numpy as np
arr = np.array([[10,20,30],[40,50,60]])
print("Array Size:",arr.size)
print("Shape",arr.shape)
######################################
#create  sequence of integer using range
arr = np.arange(0,20,3)
print("sequence of array with step of 3:\n",arr)
###################################################
#array indexing in numpy
# access single element using index
arr = np.arange(11)
print(arr)
###########################
print(arr[2])
################
print(arr[-2])
############################
#multidimensional array indexing
#Access multidimentional array element using array indexing
import numpy as np
arr = np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)
#############################################################
print(arr.shape)
###############################
print(arr[1,1]) #[[10,20,30,40,50],[20,30,50,10,30]]
 #                      0                    1
################################################
print(arr[0,4])
#################################
print(arr[1,-1])
#########################################
#Access array element  using slicing
arr= np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]  #start:end:setp of 2
print(x)
####################################
x=arr[-2:3:-1]
print(x)
#####################################
x=arr[-2:8]   #not understand
print(x)
#######################################
#indexing in numpy   #  not exicute
import numpy as np
multi_arr=np.array([[10,20,10,40],
                    [40,50,70,90],
                    [60.10,70,80],
                    [30,90,40,30]])
arr
#slicing array
#for multidimensional numpy array
multi_arr[1,2]#to access the value at row 1 and column 2.
multi_arr[1,:]#to get the value at row 1 and all column
multi_arr[:,-1]#Access the value at all the row and column1
x=multi_arr[:3,::2]#column from 0 to 3,in all selected rows
print(x)
#output:
###################################################
#integer array indexing
#integer array indexing allow selection arbitory indexing
arr=np.arange(35).reshape(5,7)
print(arr)    
###################################################3
#Boolean array indexing
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)  
rows=np.array([False,True,True])#not 0th row only first and second
wanted_rows=arr[rows,:]
print(wanted_rows) 
##################################
#converting array in to list
#1st up all create array
array=np.array([10,20,30,40])
print("Array :",array)
print(type(array))

#Convert list
lst=array.tolist()
print("list",lst)
print(type(lst))
####################################
#covert multidimensional array to list
array=np.array([[10,20,10,40],
                    [40,50,70,90],
                    [60.10,70,80],
                    [30,90,40,30]])
print("array:",array)
#convert to list
lst=array.tolist()
print(lst)
##################################
#how to convert list in to array

#numpy provide as  to use two function  to ues
#when converting list in to array
#numpy.array()
#numpy.asarray()
#numpy.array():using numpy.array() this function of numpy

#create list
list=[20,40,60,80]
array=np.asarray(list)
print("Array",array)
print(type(array))
#########################################
#Numpy array properties
      #ndarray.shape
      #ndarray.
      
      
      
##########################################
#ndarray.shape
#to get shape of python numpy a    
#########################################
array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)  
######################################
#Operation using numpy
#Numpy's oprations are  divided in to three main categores
'''
Fourier Transform and Shape Manipulation
Mathematical and Logical Operation
Linear Algebra and  random number generation
 '''
 ############################################
#Assignment
#write python program to get the numpy version and show the Numpy
import numpy as np   #not exicute
print(np._version_) 

############################################
#write nump array program to test whether none of the 
#element of given array are Zero
import numpy as np
x=np.array([1,2,3,4])
print("original array:") 
print(x) 
print("Test if none of the element of the saide array is zero")  
print(np.all(x))

x=np.array([0,1,2,3,4])
print("original array:") 
print(x) 
print("Test if none of the element of the saide array is zero")  
print(np.all(x))
###############################################
#write numpy program to test if any  of the element of a given array
#array are none zero
import numpy as np
x=np.array([1,0,0,0])
print("original array:") 
print(x) 
print("Test wether any of element of given array is non-")  
print(np.any(x))

x=np.array([0,0,0,0])
print("original array:") 
print(x) 
print("Test ")  
print(np.any(x))
###################################################
#write numpy program to test a given 
#array element-wise  for infinitenss(if not infinity or no number)
import pandas as pd
a=np.array([1,0,np.nan,np.inf])
print("original array")
print(a)
print("Test a given array element-wise for finiteness:")
print(np.isfinite(a))
####################################################
#write numpy program to test element wise for NaN of a given arrray
import pandas as pd
a=np.array([1,0,np.nan,np.inf])
print("original array")
print(a)
print("Test a given array element-wise for finiteness:")
print(np.isnan(a))
##########################################################
#write a numpy program to create element wise 
#comparison(greater,greater equal,less,lessequal)
import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("original number:")
print(x)
print(y)
print("comparison-greater")
print(np.greater(x,y))
print("camparison greater equal:")
print(np.greater_equal(x,y))
print("comparison-less")
print(np.less(x,y))
print("camparison less equal:")
print(np.less_equal(x,y))
#########################################################
#write numpy program to create 3x3 matrix
import numpy as np
array_2D=np.identity(3)
print("3x3 matrix:")
print(array_2D)
#########################################################
#write numpy program to generat random number between 0 to1
import numpy as np
rand_no=np.random.normal(0,1,1)
print("Random number between 0 and 1")
print(rand_no)
#####################################################
#write a numpy program to create 3x4 array and iterate over it
import numpy as np   
a=np.arange(10,22).reshape((3,4))
print("original array:")
print(a)
print("each element of the array is:")
for x in np.nditer(a):
 print(x,end=" ")
 print() 
################################################
#write a numpy program to create a vector 
#of length 5 with values starting  between 5 to 50
import pandas as pd
v=np.linspace(10,49,5)
print("lenth 10 with value evenly distributed bet ")
print(v)
########################################
#write numpy program to create a 3x3 matrix with values ranging from 2 to 10
import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)
###############################################
#write numpy program to revers an array
#the first element become the last
import numpy as np
x=np.arange(12,38)
print("original array:")
print(x)
print("reverse array:")
x=x[::-1]
print(x)
##########################################################
#write numpy program to compute the multiplication 
#of two matrix
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result1=np.dot(p,q)
print("result of the saide matrix multiplication:")
print(result1)
###############################################
#write numpy program to compute cross product of two matrix
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result1=np.cross(p,q)
print("result of the saide matrix multiplication:")
print(result1)
###################################################
#write numpy program to compute the determinant of matrix
import numpy as np
from numpy import linalg as LA
a=np.array([[1,0],[1,2]])
print("original 2-d array:")
print(np.linalg.det(a))
#########################################################
#write a numpy program to compute the eigenvalues and right eigenvector
#to given squre array
#igen value calculate heat intensity
import numpy as np
m=np.mat("3-2;1 0")
print("original matrix:")
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eigenvalues of the said matrix",w)
print("Eigenvalues of the said matrix",v)   
###################################################
#write numpy program to convert inverse of given matrix
import numpy as np
m=np.array([[1,2],[3,4]])
print("original matrix:")
print(m)
result=np.linalg.inv(m)
print("inverse of matrix is:")
print(result)                                                    