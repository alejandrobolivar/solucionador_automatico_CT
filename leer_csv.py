# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:08:55 2021

@author: bolivar
"""
import csv
 
with open('emv/dataset/ejemplo.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)

'''
data = pd.read_csv('emv/dataset/ejemplo.csv',sep='|')

for i in data:
    print(data[0],'  ',data[1])
'''
