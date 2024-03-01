# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 14:17:13 2023

@author: Dell
"""
#write pandfas program to count the numper of rows column
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
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count
###########################################
#OR
total_rows=len(df.axes[0])
total_col=len(df.axes[1])
print("no of rows:"+str(total_rows))
print("no of columns:"+str(total_col))
################################################
#write pandas program to select the rows where the score is missing
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[12.5,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df 
print("row where score is missing")
df2=(df[df['score'].isnull()])
df2
#################################
#write pandas program to select rows score where number between 15 and 20
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[12.5,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
df2=df[df['score'].between(15,20)]
df2
######################################
#pandas program to select rows where the number of attempt in examination
#less than two and score is greate than 15
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
print("number of attempt in examination is less than 2 or score is greater than 15")
print(df[(df['attempts']<2) & (df['score']>15)])
##############################################
#write pandas program to change the row d to 11.5
#d-row name  'score'-column name
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
print("change the score in row d to 11.5:")
df.loc[3,'score']=11.5
print(df)
#########################################
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
print("change the score in row d to 11.5:")
df.loc['d','score']=11.5
print(df)
###########################################
#write pandas program to calculate the sum of the examination
#attpemts by the student
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
print("sum of examinations attepts by student")
print(df['attempts'].sum())
##############################################
#write pandas program to calucate mean of student
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
df
print("mean of the student")
print(df['score'].mean())
############################################
#write pandas program to append the new row 6
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)

print("original rows:")
print(df)
print("\n append a new row:")
df.loc['6']=['suresh','20.5','2','yes','k']
print("all record insert after new record")
print(df)
###########################################
#write the pandas program to store the  dataframe first by "name" in decinding
#and score will be asending order
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
print("original dataframe")
print(df)
print("sort the data frame first by name in decending order")
print(df)
df=df.sort_values(by=['name'],ascending=[False])
print(df)
df=df.sort_values(by=['name'],ascending=[True])
##############################################
#write pandas program to replace qualify col contained values yse and no with true and false
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
print("original dataframe")
print(df)
print("replace the qualify column contacts the values yes and no")
df['qualify']=df['qualify'].map({'yes':True,'no':False})
print(df)
################################################
#write pandas program to change the name rutuja to james column of the dataframe
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
print("original dataframe")
print(df)
print("\n change the name rohit to james:")
df['name']=df['name'].replace('rutuja','james')
print(df)
##############################################
#write program to insert new column in existing dataframe
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
print("original dataframe")
print(df)
color=['red','blue','orange','red','white','blue']
df['color']=color
print("\n new dataframe after inserting the column")
print(df)
##############################################
#write a search pandas program to iterate over rows in a dataframe
import pandas as pd
import numpy as np
exam_data={'name':['Ram','sham','ghansham','babubhai','krishana','rutuja'],
           'score':[18,9,16.5,np.nan,9,14.5],
           'attempts':[1,3,2,3,5,6],
           'qualify':['yes','no','yes','yes','no','yes'],
           'row_lables':['a','b','c','d','e','f']
 }
df=pd.DataFrame(exam_data)
print("original dataframe")
print(df)
for index,row in df.iterrows():
    print(row['name'],row['score'])
###################################################    
