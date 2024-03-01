# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:12:02 2023

@author: Dell
"""
#

import pandas as pd
import numpy as np
data={ "A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
    }
df=pd.DataFrame(data)
df
def add_3(x):
     return x+3
df2=df.apply(add_3)
df2
df2=((df.A).apply(add_3))
df2
#######################
#apply function for single column
def add_4(x):
    return x+4
df['B']=df['B'].apply(add_4)
df['B']  # add in to original dataframe
 ###############################
#apply on multiple column the use double breket
#when your going to apply function on multiple column 
#then  we will have to pass list
df[['A','B']]=df[['A','B']].apply(add_4)   
df[['A','B']]
###############################
#apply lamda function to each column
#we  use anonimus function
#x-argument pass
df2=df.apply(lambda x:x+10)
df2
##################################
df[['A','B']]=df[['A','B']].apply(lambda x:x+10)
df[['A','B']] # only disply two column
print(df) # disply all
###################################
#using pandas dataframe transform( )
# to apply function column
#using dataframe.transform
def add_2(x):
    return x+2
df2=df.transform(add_2)
df2
###############################
#using pandas datafreame map() to using single column
df['A']=df['A'].map(lambda A:A/2)
df
###################################
#using numpy function on single column
#use apply() and [ ] breket
#always reinnitialize the dataframe
import numpy as np
df['A']=df['A'].apply(np.square)
df
####################################
#using numpy.square() method
df['A']=np.square(df['A'])
df
######################################
#assignment- numpy methods-numpy.org
########################################
#using groupby() methods
import pandas as pd
import numpy as np
technologies=({
            'Courses':["spark","pyspark","hadoop","python","pandas","hadoop","spark","python","NA"],
            'Fee':[22000,25000,23000,24000,26000,25000,25000,22000,15000],
            'Duration':['30day','50day','55day','40day','60day','35day','30day','50day','40day'],
            'Discount':[11.8,2300,1000,1200,2500,'nan',1400,1600,0]
    })
df=pd.DataFrame(technologies)
print(df)
#groupby() function
df2=df.groupby(['Courses','Duration']).sum()
print(df2)
#######################################
#grup by on multiple column
df2=df.groupby(['Courses','Duration']).sum()
print(df2)

df2=df.groupby(['Courses']).sum()
print(df2)

df2=df.groupby(['Duration']).sum()
print(df2)
###############################
#Add index to grouped data
#Add Row index to group by result
df2=df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)
#####################################
import pandas as pd
import numpy as np
technologies=({
            'Courses':["spark","pyspark","hadoop","python","pandas","hadoop","spark","python","NA"],
            'Fee':[22000,25000,23000,24000,26000,25000,25000,22000,15000],
            'Duration':['30day','50day','55day','40day','60day','35day','30day','50day','40day'],
            'Discount':[11.8,2300,1000,1200,2500,'nan',1400,1600,0]
    })
df=pd.DataFrame(technologies)
print(df)
df.columns
############################################
#get the list of all column name from header
##############################################
#pandas shuffle dataframe rows
import pandas as pd
import numpy as np
technologies=({
            'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
            'Fee':[22000,25000,26000,22000,24000,21000,22000],
            'Duration':['30day','40day','35day','40day','60day','50day','55day'],
            'Discount':[1000,2300,1500,1200,2500,21000,2000]
    })
df=pd.DataFrame(technologies)
print(df)
df1=df.sample(frac=1)
df1
################################
import pandas as pd
import numpy as np
technologies=({
            'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
            'Fee':[22000,25000,26000,22000,24000,21000,22000],
            'Duration':['30day','40day','35day','40day','60day','50day','55day'],
            'Discount':[1000,2300,1500,1200,2500,21000,2000]
    })
df=pd.DataFrame(technologies)
print(df)
df1=df.sample(frac=0.5)
df1
#########################################
#create new index starting from zero
df1=df.sample(frac=1).reset_index()
df1
########################################
#drop shuffle index

df1=df.sample(frac=1).reset_index(drop=True)
df1
#############################################
#Join
import pandas as pd
technologies={ 
    'Courses':["spark","pyspark","python","pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['3odays','40days','35days','50days']
    
    }
index_lables=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index_lables)
df1


technologies2={ 
     'Courses':["spark","java","python","Go"],
     
     'Discount':[2000,2300,1200,2000]
     }
index_lables2=['r1','r6','r3','r5']    
df2=pd.DataFrame(technologies2,index_lables2) 
df2
############################################
#pandas inner join- is mostly use in join
#it is use to join two data frame
#join meanse horizontaly join
#concatinate means verticaly join
##########################################
#pandas join, by default it will join the table left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)  
##########################################
#pandas inner join dataframe mostly use in join
#it is use to join two dataframe index
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3) 
##########################################
#pandas left join dataframe
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3) 
###################################################
#pandas right join data dataframe
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3) 
##########################################
#pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='inner')
print(df3)
############################################
#pandas join on columns(left)
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='left')
print(df3)
####################################
#right
df3=df1.set_index('Courses').join(df2.set_index('Courses'),how='right')
print(df3)
##########################################
#using pandas.merge for inner join
df3=pd.merge(df1,df2)
###########################
df3=df1.merge(df2)
##################################
#using pandas.concat() to concat two dataframe
import pandas as pd
df=pd.DataFrame({ 
    'Courses':["spark","pyspark","python","pandas"],
    'Fee':[20000,25000,22000,24000],
    
    })


df1=pd.DataFrame({ 
     'Courses':["pandas","hadoop","hyprion","java"],
     
     'Discount':[25000,23200,24500,24900]
     })
#using pandas concat to cancat two dataframe
data=[df,df1]
df2=pd.concat(data)
df2
###############################################
#concatinate multiple dataframe using concate()
import pandas as pd
df=pd.DataFrame({ 
    'Courses':["spark","pyspark","python","pandas"],
    'Fee':[20000,25000,22000,24000],
    
    })
df1=pd.DataFrame({ 
     'Courses':["pandas","hadoop","hyprion","java"],
     
     'Discount':[25000,23200,24500,24900]
     })
df2=pd.DataFrame({ 
     'Duration':["30day","40day","35day","60day","55day"],
     
     'Discount':[1000,2300,2500,3000,2000]
     })
#appending multiple dataframe
df3=pd.concat([df,df1,df2])
print(df3)