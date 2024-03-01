# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:11:23 2023
# when we want to remove column and row using index then use double squre breaket

@author: Dell
"""

import pandas as pd
technologies={'courses':["spark","pyspark","hadoop","pandas","oracle","java"],
               'fees':[20000,25000,22000,24000,21000,22000],
               'duration':['30day','40day','40day','60day','50day','55day'],
               'discount':[11.8,23.7,13.4,15.7,12.5,25.4]
}
df=pd.DataFrame(technologies) # dataframe = always d capital and also f is also capital.
df
#########################################
#convert dataframe in to csv file
df.to_csv('data_file.csv') #above dataframe are converted in to csv file
#we can also give the absolute path 
#################################
# to create dataframe for csv file
df=pd.read_csv("data_file.csv")
df
######################################
#pandas Dataframe-basic opration
import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","pandas","oracle","java","math"],
               'fees':[20000,25000,22000,24000,np.nan,21000,22000],
               'duration':['30day','40day','40day','60day'," ",'50day','55day'],
               'discount':[11.8,23.7,13.4,15.7,12.5,25.4,22.4]
             })
row_lables=['r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_lables)
print(df)
#####################################
#DataFrame-properties
df.shape
#(7,4)
df.size
# 28
df.columns
#Index(['courses', 'fees', 'duration', 'discount'], dtype='object')
df.columns.values
#array(['courses', 'fees', 'duration', 'discount'], dtype=object)

df.index
#Index(['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7'], dtype='object')
df.dtypes
#courses      object
#fees        float64
#duration     object
#discount    float64
#dtype: object
###############################
#Aceess one column contents \IMP
df['fees']
#Accessing two columns give duble squre breaket
df[['fees','duration']]
#select certain rows and assign it to another dataframe
# df[row :column ]
df2=df[6:] # not understand
df2
#accessing certain cell  from duration
df['duration'][3]
#subtracting specific value from column
df['fee']=df['fees']-500
df['fee']
#Discribe dataframe for all numeric column
df.describe() #it will show int and float value only \IMP
df.info()
#datatype object means  charecter datatype
#####################################
#rename()
df=pd.DataFrame(technologies,index=row_lables)
#assdfign new header by seting new column name
df.columns=['A','B','C','D']
df
#rename column name using rename method \IMP
#axise=1=column,  axise=0=row
df=pd.DataFrame(technologies,index=row_lables)
df.columns=['A','B','C','D']
df2=df.rename({'A':'C1','B':'C2','C':'C3','D':'C4'},axis=1)
df2
df2=df.rename({'C':'C3','D':'C4'},axis='columns')
df2
df2=df.rename(columns={'A':'C1','B':'C2'})
df2
###########################
#project process-
#importing
#EDA
#preprocessing \ feature engineering
#decide model
#implement model
#PKL file
#deployment
#################################
#write python program to create and display a one dimentional-like
#containing array of data
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)
####################################
#write a pandas program to convert a panda module series
#to python list and its type
import pandas as pd
ds=pd.Series([2,4,6,8,10])  #series displya vertically
print("pandas series and type")
print(ds)
print(type(ds))
print("convert pandas Series to python list")
print(ds.tolist()) #list displya horizontaly
print(type(ds.tolist()))
################################################
#write pandas program to add ,subtract,multiply and
#sample Series:[2,4,6,8,10],[1,3,5,7,9]
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds = ds1+ds2
print("add two series")
print(ds)
print("subtracting two Series")
ds = ds1-ds2
print(ds)
print("multiply two series")
ds = ds1 * ds2
print(ds)
print("divide two series")
ds = ds1/ ds2
print(ds)
############################################
# write the python program to compaire the element of Series
#sample Series:[2,4,6,8,10],[1,3,5,7,9]
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
print("Series1")
print(ds1)
print("Series2")
print(ds2)
print("compare the two Series")
print("Equals:")
print(ds1==ds2)
print("greater than:")
print(ds1>ds2)
print("Less than:")
print(ds1<ds2)
#####################################
#write python program to convert a dictionary to pandas Series
#original dectionary
#{'a':100,'b':200,'c':300,'d':400,'e':800}
import pandas as pd
d1={'a':100,'b':200,'c':300,'d':400,'e':800}
print("original dictionary")
print(d1)
new_Series=pd.Series(d1)
print("converted series")
print(new_Series)
#####################################
#write pndas program to convert numpy array to pandas program
import numpy as np
import pandas as pd
n_a=np.array([10,20,30,40,50])
print("numpy array")
print(n_a)
new_Series=pd.Series(n_a)
print("converted pandas Series")
print(new_Series)
########################################################
#Write pandas program to change the datatype of a given series
import pandas as pd
s1=pd.Series(['100','200','python','13.9','400'])
print("Original series are")
print(s1)
print("change the dat type to Series to numeric")
s2=pd.to_numeric(s1,errors='coerce')
print(s2)
########################################################
#write pandas program to convert the first column of datframe as a Series
#when we use name of column=loc \IMP -import any dataframe and will axtract only one colum
#when use index-iloc
#IMP loc,iloc,converting dataframe to series
#[3:6,2:4]
#start row,end row
#start column, end column
#[:,0]-means only col

import pandas as pd
d={'col1':[1,2,3,4,7,11],
   'col2':[4,5,6,9,5,0],
   'col3':[7,5,8,12,1,11]
   }
df=pd.DataFrame(data=d)
print("original Dataframe")
print(df)
s1=df.iloc[:,]
print("1st column as a series")
s1 # retry
#############################################
#we print series in vertical manner for that we use  reset index method
#list of list multilevel index
#s1=s.apply(pd.Series)
#s2=s1.stack()
#s3=s2.reset_index(drop=True)
## Series always in vertical manner but in this program we list of list means strings
#stack function()-
import pandas as pd
s=pd.Series([['red','green','white'],
    ['red','black'],
    ['yellow']]
    )
print("original Series of list")
print(s)
s=s.apply(pd.Series).stack().reset_index(drop=True)
print("one Series")
print(s)
####################################################
#write pandas program to add data to existing series
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("original dictionary")
print(s)
print("\n data series after adding some data")
new_s=pd.concat([s,pd.Series([500,'php'])],ignore_index=True)
print(new_s)
###################################################
#write a pandas program to change the order of
# index of given series
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("original dictionary")
print(s)

new_s = pd.Series(s).sort_values()
print(new_s)
####################################
#write a pandas program to change the order of index of given series
#sample output-
'''
B     2       
A     1  
C     3
D     4     
E     5
'''
import pandas as pd
s=pd.Series(data=[1,2,3,4,5],index=['A','B','C','D','E'])
print("original series")
print(s)
s=s.reindex(index=['B','A','C','D','E'])
print("data series after changing the oredr of index:")
print(s)
###################################