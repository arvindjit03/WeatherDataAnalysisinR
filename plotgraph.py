#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:06:24 2020

@author: madhusharma
"""

# importing the required module 

import pandas as pd

df = pd.read_excel ("Weather_Data.xlsx")
#print (df)
for col in df.columns: 
    print(col)
# add a sequence of numbers to df
num_rows = len(df.index)

#print(num_rows)


import matplotlib.pyplot as plt 
 # Create a list in a range of 10-20 
My_list = [*range(1, num_rows+1, 1)] 

# Print the list 
#print(My_list) 
 
# x axis values 
x = My_list
x= x[:100]
# corresponding y axis values 
y = df['Max Temperature'].tolist()
y = y[:100] 
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('Maximum Temperature plot') 
  
# function to show the plot 
plt.show() 