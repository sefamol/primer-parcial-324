#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:29:37 2021

@author: sebas
"""

import pandas as pd


dataset = pd.read_csv('titanic.csv')
#columna variables dependientes
x = dataset.iloc[:, :3].values 
#columna variable independiente
y = dataset.iloc[:, 3].values

#Realizamos latransformación de cadena a valores númericos para los calculos matemáticos
from sklearn.preprocessing import LabelEncoder
labelencoder_x = LabelEncoder()
for i in range(3):
    x[:,i] = labelencoder_x.fit_transform(x[:,i])

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
print("media sin librerias numpy")
media1=[]
for i in range(3):
    n=len(x[:,i])
    me=sum(x[:,i])/n
    media1.append(me)
    print (media1)


print ("desviacion standart sin librerias numpy")
import math
S = 0
N = n
S1=0
desv=[]
print("--columna 0--") 
for k in range(3) :
    S1=0
    S=0
    for i in range(0,N):
        S=S+x[i,k]
    pro=S/N
    print("Promedio:", pro)
    for j in range(0,N):
        S1=S1+(x[j,k]-pro)*(x[j,k]-pro)
    vari=S1/N
    estandar=math.sqrt(vari)
    print("Varianza: ",vari)
    print("Desviacion std: ",estandar)
    desv.append(estandar)
    
print ("moda sin librerias numpy")
from collections import Counter
modP=[]
valorP=[]
for l in range(3):
    data=Counter(x[:,l]).most_common()
    tdata=len(data)
    mayor=0
    valida=True
    for i in range(tdata):
        cuenta=0
        for j in range (tdata):
            var=data[i]
            varC=data[j]
            if(var[1]==varC[1]):
                print(var[1])
                cuenta=cuenta+1
        if(cuenta==tdata):
            print("no hay moda")
            valida=False
            
        
    for i in range(tdata):
        var=data[i]
        if(var[1]==n):
            print("no hay moda")
            valida=False
    for i in range(tdata):
        var=data[i]
        if(var[1]==n):
            print("no hay moda")
            valida=False
    for i in range(tdata):
        var=data[i]
        if(var[1]==n/2):
            print("no hay moda")
            valida=False
    
    if(valida==True):
        may=0
        moda=0
        for i in range(tdata):
            var=data[i]
            if(may>var[1]):
                may=may
                moda=moda
            elif(var[1]>may):
                may=var[1]
                moda=var[0]
        modP.append(moda)
        valorP.append(may)
        print("la moda es ",moda,"con el valor ", may)

print("media ", media1)
print("Desviacion Standart", desv)
print("moda ",modP,"valor de la moda ",valorP)

