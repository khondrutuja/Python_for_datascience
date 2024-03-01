# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:17:57 2023

@author: Dell
"""
#matplotlib-matplotlib is ude for vishualization perpose

import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()
##############################################
#Multiline plots
import matplotlib.pyplot as plt
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])
plt.plot(x,[xi*3.0 for xi in x])
plt.plot(x,[xi/3.0 for xi in x])
plt.show()
###############################################
#note= matplotlib atomaticaly select the different color
#################################################
#Grid axis and lables
#Adding a grid
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()
#######################################################
#handel the axis  starting points
#give the name of x-axis and y-axis
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.axis() # show the current axis limits value
plt.axis([0,5,-1,13]) #means x axis point up to 0 to 5 and y axis
#[xmin,xmax,ymin,ymax]#point up to 0 to 13
plt.show()
###################################################
#Adding in the line
#give the name of x axis and y axis
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.xlabel("this is the x axis")
plt.ylabel("this is  the y aixs ")
plt.show()
###########################################################
#Adding a title
#matplotlib provides a simple function,plt.title()
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('simple plot')
plt.show()
#########################################################
#Adding legend
#legend means graph corner contain name of line 
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5) #when we use np. arange function then import numpy as np
plt.plot(x,x*1.5,label="Normal")
plt.plot(x,x*3.0,label='Fast')
plt.plot(x,x/3.0,label='Slow')
plt.legend()
plt.show()
########################################################
#Control colors
''' Color abbrivation
color  name
b       blue
c       cyan = light blue
g       green
k       black
m       magenta = purple
r       red
w       white
y       yellow
'''
  
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y');
plt.show()
plt.plot(y+1,'m');
plt.show()
plt.plot(y+2,'c');
plt.show()
#####################################################
#Specifying styles in multiline plots
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()
############################################3
#doted line grap
import matplotlib.pyplot as plt
import  numpy as np
y=np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':');
plt.show()
###########################################
'''
style abbrivation
-solid line
--dash line
-. dash dot line
: dotted line
'''
'''
Marker abbrivation Marker style
. point marker
, pixel marker
o Circle marker
v Triangle down
marker
^ Triangle up marker
< Triangle left marker
> Triangle right
marker
1 Tripod down
marker
2 Tripod up marker
3 Tripid left marker
4 Tripod right marker
s Square marker
p pentagoan marker
* star marker
'''
'''
Marker Abbrivation Marker style
. = point marker
, = pixel marker
o = circle marker
v = triangle down
marker





'''
####################################################
#apply disign to line
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s');
plt.show()
###############################################
#Histogram chart
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y)
plt.show()
##################################################
#bar plot
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5]);
#        x-cordinate   y-cordinate
plt.show()
#bar function is use to generet bar charts in matplotlib
#the function expect two list value
#################################################
#Scatter plot
#Scatter plot display values for two sets of data.
#the data visualization is done
#as the collection of points not connected to yhe line
#each of them has  its co-ordinste
import matplotlib.pyplot as plt
import numpy as np
x= np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()
###################################################
size = 50*np.random.randn(1000)
colors=np.random.rand(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()
##################################################
#Adding text
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-4,4,1024)
Y=.25*(X+4.)*(X+1.)*(X-2.)
plt.text(-0.5,-0.25,'Brackmard minimum')
plt.plot(X,Y,c ='k')
plt.show()
####################################################
#pip install seaborn
import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#seaborn has 18 in built dataset
#that can be found using following cammand
sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()
####################################################
#count plot
'''A count plot is helpful when dealing with categorical values
.it is uae to plot a frquency of different categories.
the column sex contain categorical data '''
sns.countplot(x='sex',data=df)
#x-the name of coumn
#data-dataframe
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')
sns.countplot(x='sex',hue='survived',data=df,palette='Set3')
#hue-the name of the categarical column to split the bar
#palette-the color palette to be use
#######################################################
#KDE plot
#karnel density estimate(KDE) plot is used
#to plot the distridusion of continuous data
sns.kdeplot(x='age',data=df,color='black')
################################################
#distribusion plot
#it is a histogram to kde plot
sns.displot(x='age',kde=True,bins=6,data=df)
#kde-set to false by default
#bins-no.of bins bar
#the lower no the wider bar and wider intervals
###############################################
sns.displot(x='age',ked=True,bins=5,
            hue=df['survived'],palette='Set1',data=df)
####################################################
#Scatter plot using matplotlib
df=sns.load_dataset('iris')
df.head()
#scatter plot helps to understand co-relation between data
sns.scatterplot(x='sepal_length',y='petal_length',
                data=df,hue='species')
#########################################################
#join plot
#join plot is use to plot the correlation between data
sns.jointplot(x='sepal_length',y='petal_length',
              data =df,kinds='reg')

sns.jointplot(x='sepal_length',y='petal_length',
              data =df,kinds='hist')

sns.jointplot(x='sepal_length',y='petal_length',
              data =df,kinds='ked')
###########################################################
''' kind- the kind of plot to be plotted.
#It can be one of the following'''
'scatter','hist','hex','reg','resid'
sns.pairplot()
####################################################
#heat map
corr=df.corr()
sns.heatmap(corr)
##################################