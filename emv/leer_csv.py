# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:08:55 2021

@author: bolivar
"""
import pandas as pd

data = pd.read_csv('dataset/enunciadosCT_ciclo_3.csv',sep='|')

print(data(['enunciados']))

for i in data:
    print(data[i])



