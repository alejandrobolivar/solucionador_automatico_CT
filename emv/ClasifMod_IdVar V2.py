"""
Created on Sun Dec 17 22:40:58 2017


"""
#pip install keras
#pip install tensorflow

# Se importa las librerias requeridas

import pandas as pd

#from librerias.lib_ClasifMod import clasificador
from librerias.lib_IdVar import detectar_vars, file_to_dict

# This code was tested with matplotlib 2.1.0, numpy 1.16.5
# pandas 1.0.3, keras 2.1.2, sklearn 0.24.1

# print("numpy version", np.__version__)
# print("pandas version", pd.__version__)
print("Leyendo datos de entrenamiento...")
data = pd.read_csv('dataset/enunciadoscinematica2.csv',sep=';')  # ,encoding = "ISO-8859-1")
'''
clasificador(data)
'''
dfvar = pd.read_csv('dataset/listadevariables2.csv', sep='|')
dict = file_to_dict("dataset/convert_text_to_descripcion_SI.txt")

from librerias.lib_ClasifMod import filtros1

filtros1(data)
# Esta data2 debe tener las variables dependientes e independientes para comparar
data2 = data.copy()

detectar_vars(data2, dfvar, dict)
