# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:55:47 2023

@author: Dell
"""

import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
#######################################
#find out the number of rows in dataframe
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count
#############################################
#write pandas program to displya the summary of information 
import pandas as pdsss
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
print("summary of the basic information about dataframe")
print(df.info())
print(df.discribe())
###########################################
##write  pandas program to get fist 3 rows in dataframe
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
df.head(3)
################################################
#write python program to select name and 'score' column from dataframe
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
print(df[['Area','Compactness']])
##############################################
#write pandas program to select rows where the no of 
#attempt in examination is greater than two
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/2-dataset/seeds_data.csv")
df
print("number of attempt in examination is greater than two")
print(df[df['Assymetry_coeff']>2])
#################################################
#write pandas program to select the rows where the score is missing
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
print("row where score is missing")
df2=(df[df['Area'].isnull()])
##########################################################
#write pandas program to select rows between 15 and 20
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
df2=df[df['Area'].between(15,20)]
df2
########################################################
#write pandas program to change the row d to 11.5
#d-row name  'score'-column name
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:DATA/2-dataset/seeds_data.csv")
df
print("change the score in row d to 11.5:")
df.loc[3,'Area']=11.5
print(df)
##################################################
#write pandas program to calculate the sum of the examination
#attpemts by the student
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/2-dataset/seeds_data.csv")
df
print("sum of examinations attepts by student")
print(df['Area'].sum())
################################################
#write pandas program to calucate mean of student
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
print("mean of the student")
print(df['Area'].mean())
#####################################
#write the pandas program to store the  dataframe 
##write the pandas program to store the  dataframe first by "name" in decinding
#and score will be asending order
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
print("original dataframe")
print(df)
print("sort the data frame first by name in decending order")
print(df)
df=df.sort_values(by=['Area'],ascending=[False])
print(df)
df=df.sort_values(by=['Area'],ascending=[True])
##########################################
#write a search pandas program to iterate over rows in a dataframe
import pandas as pd
import numpy as np
#create dataframe from csv
df=pd.read_csv("c:/DATA/2-dataset/seeds_data.csv")
df
print("original dataframe")
print(df)
for index,row in df.iterrows():
    print(row['Area'],row['Assymetry_coeff'])
#################################################
