# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:08:55 2021

@author: bolivar
"""
import pandas as pd

data = pd.read_csv('dataset/enunciadosCT.csv',sep='|')

for i in data:
    print(data['enunciados'],'  ',data['modelos'])

resp = input('Pulse una tecla para finalizar...')