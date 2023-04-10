# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:08:55 2021

@author: bolivar
"""
import pandas as pd
 
data = pd.read_csv('emv/dataset/enunciadosCT_ciclo_3.csv',sep='|')  # ,encoding = "ISO-8859-1")


for i in data:
    print(data[0],'  ',data[1])
