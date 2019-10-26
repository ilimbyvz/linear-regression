# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 01:44:47 2019

@author: DELL
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from statistics import mean


# inclusion external data 
def dataset():
    data = pd.read_csv('Salary_Data.csv') 
    X=data["YearsExperience"].values
    Y=data["Salary"].values
    return X,Y

#embed data into code 
def manueldata():
    X = np.array([60,61,62,63,65], dtype=np.float64)
    Y = np.array([3.1,3.6,3.8,4.0,4.1], dtype=np.float64)
    return X,Y

#data input with keyboard
def addata():
    X=np.array([], dtype=np.float64)
    Y=np.array([], dtype=np.float64)
    i=int(input("How many will you input data?"))
    for j in range(0,i):
        x=float(input("X: "))
        X=np.append(X,x)
        
    for k in range(0,i):
        y=float(input("Y: "))
        Y=np.append(Y,y)
    return X,Y

#normalization
def normalization(norm):
    normed = (norm - min(norm)) / (max(norm) - min(norm))
    return normed
    
#linear regression
def regresyon(x, y):
    print("""\Linear Regression Formula: y=ax+b\n
a(slope)=mean(x)*mean(y)-mean((x * y))/(mean(x)^2-mean(x^2))\n
b(constant)=mean(y)-(a*mean(x))""")
    a = ((np.mean(x) * np.mean(y)) - np.mean((x * y))) / (np.mean(x)**2 - np.mean(x**2))#slope
    b = np.mean(y) - (a * np.mean(x))#constant
    return a, b

#graphic    
def shape(a,x,b,y):
    line = [(a * x) + b for x in range(0, 30)]
    plt.scatter(x, y,color='b')
    plt.plot(line, color='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    
def main(X,Y):
    xnorm=normalization(X)
    print("\nNormalized data for X \n{}".format(xnorm))
    
    ynorm=normalization(Y)
    print("\nNormalized data for Y\n{}".format(ynorm))
    
    a,b=regresyon(X,Y)
    print("\n Regression result before normalization a:{}, b:{}".format(a,b))
    sekil(a,X,b,Y) 
    
    a,b=regresyon(xnorm,ynorm)
    print("\nRegression result a:{}, b:{}".format(a,b))
    
    shape(a,xnorm,b,ynorm)
    
    while True:
        choose=input("1-X  when x value is given Y=?\n2- when y value is given X=?\n3-Exit\nPlease choose: ")
        if choose=="1":
            x=int(input("X:"))
            y=a*x+b
            print("X:{} için Y:{}".format(x,y))
      
        elif choose=="2":
            y=int(input("Y:"))
            x=(y-b)/a
            print("Y:{} için X:{}".format(y,x))
      
        elif choose=="3":
            break
        else:
            print("\nIncorrect entry!")
        
#X,Y=manueldata()    
X,Y=dataset()
#X,Y=addata()
main(X,Y)

