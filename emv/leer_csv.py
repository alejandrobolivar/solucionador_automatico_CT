# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:08:55 2021

@author: bolivar
"""
import pandas as pd

data = pd.read_csv('dataset/enunciadosCT.csv',sep='|',usecols=['enunciados','modelos'])

data(['enunciados'])

'''
for i in data:
    print(data[i] )

resp = input('Pulse una tecla para finalizar...')
'''
