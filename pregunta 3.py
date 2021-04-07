#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:32:10 2021

@author: sebas
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('titanic.csv')
#columna variables dependientes
x = dataset.iloc[:, :3].values 
#columna variable independiente
y = dataset.iloc[:, 3].values

#Realizamos la transformación de cadena a valores númericos para los calculos matemáticos
from sklearn.preprocessing import LabelEncoder
labelencoder_x = LabelEncoder()
for i in range(3):
    x[:,i] = labelencoder_x.fit_transform(x[:,i])
 
#Realizamos el completado de los datos faltantes en el dataset
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:,1:3]) 


labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#Convertimos las variables categoricas a una matriz sin peso en los valores
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
onehot = OneHotEncoder(sparse=False)
x = onehot.fit_transform(x)

