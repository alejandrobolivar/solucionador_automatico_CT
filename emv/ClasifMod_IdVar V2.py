"""
Created on Sun Dec 17 22:40:58 2017


"""
#pip install keras
#pip install tensorflow

# Se importa las librerias requeridas

import pandas as pd

from librerias.lib_ClasifMod import clasificador
# from librerias.lib_IdVar import detectar_vars, file_to_dict

# This code was tested with
# pandas 1.4.0, numpy 1.21.5+mkl, scikit-learn 1.0.2, nltk 3.6.7
# matplotlib 3.2.2, keras 2.10.0, tensorflow 2.10.0

# print("numpy version", np.__version__)
# print("pandas version", pd.__version__)
print("Leyendo datos de entrenamiento...")
data = pd.read_csv('dataset/enunciadosCT.csv',sep=';')  # ,encoding = "ISO-8859-1")
clasificador(data)

input('<<< Pulse una tecla para continuar >>>')
'''
dfvar = pd.read_csv('dataset/listadevariables2.csv', sep='|')
dict = file_to_dict("dataset/convert_text_to_descripcion_SI.txt")

from librerias.lib_ClasifMod import filtros1

filtros1(data)
# Esta data2 debe tener las variables dependientes e independientes para comparar
data2 = data.copy()

detectar_vars(data2, dfvar, dict)
'''