# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 01:44:47 2019

@author: DELL
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from statistics import mean


#dışardan veriseti dahil etme
def veriseti():
    data = pd.read_csv('Salary_Data.csv') 
    X=data["YearsExperience"].values
    Y=data["Salary"].values
    return X,Y

#veriyi koda gömme
def manuelveri():
    X = np.array([60,61,62,63,65], dtype=np.float64)
    Y = np.array([3.1,3.6,3.8,4.0,4.1], dtype=np.float64)
    return X,Y

#klavyeden veri girişi
def veriekleme():
    X=np.array([], dtype=np.float64)
    Y=np.array([], dtype=np.float64)
    i=int(input("Kaç adet veri gireceksiniz: "))
    for j in range(0,i):
        x=float(input("X: "))
        X=np.append(X,x)
        
    for k in range(0,i):
        y=float(input("Y: "))
        Y=np.append(Y,y)
    return X,Y

#normalizasyon
def normalizasyon(norm):
    normed = (norm - min(norm)) / (max(norm) - min(norm))
    return normed
    
#doğrusal regresyon
def regresyon(x, y):
    print("""\nDoğrusal Regresyon Formülü: y=ax+b\n
a(eğim)=mean(x)*mean(y)-mean((x * y))/(mean(x)^2-mean(x^2))\n
b(sabit)=mean(y)-(a*mean(x))""")
    a = ((np.mean(x) * np.mean(y)) - np.mean((x * y))) / (np.mean(x)**2 - np.mean(x**2))#eğim
    b = np.mean(y) - (a * np.mean(x))#sabit
    return a, b

#grafik    
def sekil(a,x,b,y):
    line = [(a * x) + b for x in range(0, 30)]
    plt.scatter(x, y,color='b')
    plt.plot(line, color='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    
def main(X,Y):
    xnorm=normalizasyon(X)
    print("\nX için normalize edilmiş veriler\n{}".format(xnorm))
    
    ynorm=normalizasyon(Y)
    print("\nY için normalize edilmiş veriler\n{}".format(ynorm))
    
    a,b=regresyon(X,Y)
    print("\nNormalizasyon uygulanmadan önceki Regresyon sonucu a:{}, b:{}".format(a,b))
    sekil(a,X,b,Y) 
    
    a,b=regresyon(xnorm,ynorm)
    print("\nRegresyon sonucu a:{}, b:{}".format(a,b))
    
    sekil(a,xnorm,b,ynorm)
    
    while True:
        sec=input("1-X değeri verildiğinde Y=?\n2-Y değeri verildiğinde X=?\n3-Çıkış\nSeçim yapınız: ")
        if sec=="1":
            x=int(input("X:"))
            y=a*x+b
            print("X:{} için Y:{}".format(x,y))
      
        elif sec=="2":
            y=int(input("Y:"))
            x=(y-b)/a
            print("Y:{} için X:{}".format(y,x))
      
        elif sec=="3":
            break
        else:
            print("\nHatalı Giriş!")
        
#X,Y=manuelveri()    
X,Y=veriseti()
#X,Y=veriekleme()
main(X,Y)

