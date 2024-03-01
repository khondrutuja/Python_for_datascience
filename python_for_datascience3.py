# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:29:04 2023

@author: Dell
"""
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
##############################
df1=df.drop(['r1','r2'])
df1
####################################
df1=df.drop(df.index[1])
df1
###################################
df1=df.drop(df.index[[1,3]])
df1 #delete row index wise 1 & 3
######################################
df1=df.drop(df.index[3:])
df1 #delete index 3 rows
#######################################
#when yodf.dropu have defalt index for rows
df=df.drop(0)
df  #not understand
#########################################
#to detelet the certain row which are not consecative
df1=df.drop(range(1,3))
df1 #not exixute
################################################
import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","pandas","oracle","java","math"],
               'fees':[20000,25000,22000,24000,np.nan,21000,22000],
               'duration':['30day','40day','40day','60day'," ",'50day','55day'],
               'discount':[11.8,23.7,13.4,15.7,12.5,25.4,22.4]
             })
row_lables=['r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies)
print(df)
#Drop  column by name \IMP
#Drop 'fees'column
df2=df.drop(['fees'],axis=1)
print(df2)
######################################
#explicitly using parameter name 'lables'
df2=df.drop(labels=['fees'],axis=1)
df2
#####################################
df2=df.drop(columns=['fees'],axis=1)
df2
###################################
#drop column by index
print(df.drop(df.columns[1],axis=1))
#############################################

df=pd.DataFrame(technologies)
#when you are going to use inplace=True ? |IMP
#ans:- when we work on original dataframe then we use inplace =true
df.drop(df.columns[2],axis=1,inplace=True) #this line delete
print(df) #the second index column
############################################
#drop two or more column by label name
df=pd.DataFrame(technologies)
df2=df.drop(["courses","fees"],axis=1)
df2
#############################################

##drop two or more column by index
df=pd.DataFrame(technologies) # always reinitialize dataframe
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
##########################################
#Drop column from list of columns
df=pd.DataFrame(technologies)
liscol=["courses","fees"]
df2=df.drop(liscol,axis=1)
df2
###################################
#remove column from dataframe iself
#########################################
#\IMP
#loc and iloc are called slicing oprator
#labels=name=loc
#index=iloc
#syntax-df.iloc[startrow:endrow,startcol:endcol]
#e.g-

df=pd.DataFrame(technologies,index=row_lables)
#below are quik example
df2=df.iloc[:,0:2]  #display 0 and 1 index column
df2
#this line use theslicing oprator to get dataframe
#item by index
#the first slice return [:]indicate all rows.
#the second slice specified by only columns
#between 0 to 2 (excluding 2)
 
##############################################
df2=df.iloc[0:2:, :]
df2
#############################################
#slicing specific rows and specific columns
df3=df.iloc[1:2,1:3] #excluding 2 and 3
df3
##############################################
df2=df.iloc[2]  #select row by index
df2
df2=df.iloc[[2,3,6]] 
df2#select row by index list
df2=df.iloc[1:5]
df2#select row by integer index range
df2.iloc[:1]#select first row
df2.iloc[:3]#select first 3 rows
df2.iloc[-1:]#select last row
df2.iloc[-3:]#select last 3 row
df2.iloc[::2]#select alternate row
#[::]=alternate row 
####################################################
#select row by index labels
df=pd.DataFrame(technologies,index=row_lables)
df2=df.loc['r2']#select row by label
df2
df2.loc[['r2','r3','r5']]#select row by label index range
df2.loc['r1':'r5']#select row by labels# r1 to r5,r5 also display
df2.loc['r1':'r5':2]#select alternet rows
##################################################
#using loc[] to take column slices
#loc[] syntax-
#df.loc[:,start:stop:step]
#select the multiple column
df=pd.DataFrame(technologies,index=row_lables)
df2=df.loc[["courses","fees","duration"]]
df2
#select ramdom column
df2=df.loc[:,["courses","fees","duration"]]
df2
#select columns between two columns
df2=df.loc[:,"fees":"discount"] #not understand
df2
#select column by range
df2=df.loc[:,"duration":] #not understand
df2
#select column by range
#all the column up to duration
df2=df.loc[:,:"duration"] #not understand
df2
#####################################################
#Query
#pandas dataframe.query() by example
#when we want to displya specific row then we use Query
df2=df.query("courses=='spark'")
print(df2)
#################################
#how to add column to the data frame
import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","pandas","oracle","java","math"],
               'fees':[20000,25000,22000,24000,np.nan,21000,22000],
               'duration':['30day','40day','40day','60day'," ",'50day','55day'],
               'discount':[11.8,23.7,13.4,15.7,12.5,25.4,22.4]
             })
df=pd.DataFrame(technologies)
print(df)
##how to add column to the data frame
tutors=['Ram','sham','Ghansham','Ganesh','Ramesh','rutuja','rohini']
df2=df.assign(TutorsAssigned=tutors)
print(df2)

#OR
name=['rutuja','rohit','rohan','rohini','radhika','radha','nisha']
df2=df.assign(Name=name)
print(df2)
###########################
#how to add multiple column
MNCCompanies=['TATA','HCL','Infosys','Google','Amazon','AWS','Microsoft']
df2=df.assign(MNC=MNCCompanies,tutors=tutors)
df2
################################3
#IMP
#dirive new column from the existing column using lambda function
df=pd.DataFrame(technologies)
df2=df.assign(discount_percent=lambda x:x.fees*x.discount/100)
print(df2)
#x= x is a row , lambda function take each row and multiply it to fees column
#and divide by zero
##########################################
#append column to exixting DtataFrame
#add new column to exixting dataframe
df=pd.DataFrame(technologies)
df['MNCCompanies']=MNCCompanies
print(df)
#######################################
#add new column at specific location
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
print(df)
##############################################
#find out the number of rows in dataframe
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count
###############################################
#find the number of row count and col count
df=pd.DataFrame(technologies)
row_count=df.shape[0]
col_count=df.shape[1]
print(row_count)
print(col_count)
##########################################
#Assignment
#1) write pandas program to create dataframe using dictionary and
#displya it sample data is given
#{'x'=[10,20,30,40],'y'=[50,60,70,80],'z'=[40,50,60,70]}
import pandas as pd
d={'x':[10,20,30,40],'y':[50,60,70,80],'z':[40,50,60,70]}
df=pd.DataFrame(d)
df
#####################################
#2) create dataframe
#exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja']}
#'score':[12.5,9,16.5,np.non,9,20,14.5]
#'attempts':[1,3,2,3,5,6]
#'qualify':['yes','no','yes','yes','no','yes']
#'lables':['a','b','c','d','e','f']
import pandas as pd
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[12.5,9,16.5,'np.non',9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
#################################
#write pandas program to displya the summary of information 
import pandas as pd
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[12.5,9,16.5,'np.non',9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
print("summary of the basic information about dataframe")
print(df.info())
df.discribe()
##########################################
#write  pandas program to get fist 3 rows in dataframe
import pandas as pd
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[12.5,9,16.5,'np.non',9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
df.head(3)#displya first 3 rows
df.iloc[:3]
###############################################3
#write python program to select name and 'score' column from dataframe
import pandas as pd
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[12.5,9,16.5,'np.non',9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
print(df[['name','score']])
#######################################
#write python program to select specific column and row
#sample output:-
#   score  qualify
#  b   9.0    no
#  d   NaN    no 
#  f   20.0   yes
#  g   14.5   yes
import pandas as pd
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[12.5,9,16.5,'np.non',9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
df.iloc[1::2,1::2]
####################################
#write pandas program to select rows where the no of 
#attempt in examination is greater than two
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[12.5,9,16.5,'np.non',9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
print("number of attempt in examination is greater than two")
print(df[df['attempts']>2])
################################
df2=df.loc[df.attempts>2]
df2
#####################################
