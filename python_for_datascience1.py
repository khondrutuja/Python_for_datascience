# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:34:16 2023

@author: Dell
"""
#serise- is model one dimenstional data like 
#difference bet list and series and arrays \IMP
import pandas as pd
songs2= pd.Series([145,142,38,13],name='counts')
    #it is easy to inspect index of series
songs2.index
# the index can be string based as well
#in which case pandas indicates that the data type for the index
#is object
#how to see thst table-click variable explorar and click series
songs3=pd.Series([145,142,38,13],name='counts',
index=['paul','john','georg','ringo'])
songs3.index
songs3
#######################################################
#the(not number NaN) null value
#and is usally egnor arthmatic opration
#when we are going use csv file then use read_csv
#if working directry not selected then give absolute path
#using relative path
#when we write the path of file the always use frunt slash
#when we use relative path the select the 1 python folder and then 
#just write the name of that file.
import pandas as pd
f1=pd.read_csv('age.csv')
f1
#########################
#using absolute path
import pandas as pd
f1=pd.read_csv('C:/DATA/1-python/age.csv')
f1

#######################################
#import excel file
import pandas as pd
df=pd.read_excel('C:/DATA/1-python/Bahaman.xlsx')
df
#############################################
#difference bet list and series
#numpy array
import numpy as np
numpy_ser=np.array([145,142,38,13])
songs3[1]
numpy_ser[1]
#same procedure to access the number from array  and series

songs3.mean()
numpy_ser.mean()
##################################################
#pandas series data structure
#support for the basic CURD
#creation
george=pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'], 
name='george song')
george
##############################
#reading # retry
#to reade select the data from series
george=pd.Series(['1968'])
george=pd.Series(['1970'])
#we can iterate over data
#as well iterating over saries
for items in george:
    print(items)
#updating value in series
george['1969']=68 #retry
george['1969']
#deletion
#the deletion statment appears to have
#problem with dublicate index
s = pd.Series([2,3,4],index=[1,2,3])
del s[1]
s
################################################
#convert type
#data not nulll then only convert it
#string use.astype(str)
#numeric use pd.to_numeric
#note that this will be fail with NaN
#datetime use pd.to_datetime
import pandas as pd
songs_66=pd.Series([3,None,11,9],name='counts')
index=['george','ringo','john','paul']
songs_66.dtypes
#dtype (float64)
pd.to_numeric(songs_66.apply(str))
#there will be error
pd.to_numeric(songs_66.astype(str),errors='coerce') #sta is exicute but data type is not change
#if we pass error=coerce
#we can see that it supports many formate
songs_66.dtypes
#dealing with None
#the fillna method will replace them with a given value
songs_66.fillna(-1)
#Nan value can be dropped from
#from the series using dropna
#dropna is last method apply drop na from last
songs_66.dropna() 
#############################################
#Append,combining and joining two series
songs_69=pd.Series([7,16,21,39],
                   index=['ram','sham','ghansham','krishna'],
                   name='counts')
#To soncatinate two series together,simply use the
songs=songs_66.append(songs_69) #retry
###############################################
#ploting  series #line plot
import matplotlib.pyplot as plt
#matplotlib-module pyplot-submodule
fig=plt.figure() #it open canvas
songs_69.plot()  #plot songs_69 series
plt.legend()
############################
#barplot
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()
###############################
#Histogram #retry
import numpy as np
data = pd.Series(np.random.randn(500),name='500 randoms')
fig =plt.figure() 
ax=fig.add_subplot(111) 
data.hist()
####################################################               
# what ispandas dataframe?

###############################################
#to check the version of pandas
import pandas as pd
pd.__version__
################################################
#create using constructor
#create pandas datagrame from list
import pandas as pd
technologies =[['spark','20000','30days'],
               ['pandas','20000','40days']
               ]
df=pd.DataFrame(technologies) # dataframe = always d capital and also f is also capital.
print(df)
#####################################
#since we have not given name to column and index,data frame by
# defalt assign
#increamental seqence no as lable
#to both rows and colums,these are called index.
#add column and row lable to the dataframe
column_names=["courses","fees","duration"]
row_lables=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_lables)
df
#############################################
df.dtypes
###########################################
#we use dictionary
#you can also assign custom 
#data type to columns.
import pandas as pd
technologies={'courses':["spark","pyspark","hadoop","pandas","oracle","java"],
               'fees':[20000,25000,22000,24000,21000,22000],
               'duration':['30day','40day','40day','60day','50day','55day'],
               'discount':[11.8,23.7,13.4,15.7,12.5,25.4]
}
df=pd.DataFrame(technologies) # dataframe = always d capital and also f is also capital.
print(df.dtypes)
############################################
#convert all data types to best possible types
#convert object
df2=df.convert_dtypes()
print(df2.dtypes)
#changes all column to same type
df=df.astype(str)
print(df.dtypes)
#change type for one or multiple columns \IMP
df = df.astype({"fees":int,"discount":float})
print(df.dtypes)
####################################################
#convert data type for all columns in a list
import pandas as pd
df = pd.DataFrame(technologies)
df.dtypes
cols=['fees','discount']
df[cols]=df[cols].astype('float')
df.dtypes
####################################################
#Ignores error
df=df.astype({"courses":int},errors='ignore')
df.dtypes
#generate error
df=df.astype({"courses":int},errors='raise')
df.dtypes
#######################################################
#convert feed column to numeric type


