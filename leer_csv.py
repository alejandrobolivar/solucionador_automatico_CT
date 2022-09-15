# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:08:55 2021

@author: bolivar
"""
import pandas as pd

data = pd.read_csv('dataset/enunciadosCT.csv',sep='|')

for i in data:
    print(data[0],'  ',data[1])

