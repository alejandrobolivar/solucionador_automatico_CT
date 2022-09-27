'''
Programa para la resolución de problemas mediante la matriz de relaciones
'''
# Importar modulos
import numpy as np
from sympy import symbols, solve
import pandas as pd
from librerias.lib_cal_mat_rel import init_mat, conv_strtofloat, total_row, total_col, resta_unidad_col, leer_datos


def main():
    '''Función principal'''
    # Lectura de datos
    data_ec = pd.read_csv('Ec_Cinematica.csv')
    lista_ec = data_ec['ecuaciones'].astype(str).values.tolist()

    # Lectura de datos
    data_unid = pd.read_csv('Unidades.csv', sep=',', encoding="ISO-8859-1")
    unidades = np.array(data_unid.astype(str).values.tolist())

    # Obtención de la cantidad de variables y ecuaciones
    dim = np.shape(unidades)
    n_var = dim[0]
    n_ec = len(lista_ec)

    # Conversión de variables en variables simbólicas
    variables = list(unidades[:, 0])
    variables = symbols(variables)

    # Creación e inicializacion de la matriz
    matriz = np.zeros((n_ec + 8, n_var + 2))
    #dimensiones = matriz.shape
    #filas = range(1, dimensiones[0])
    #columnas = range(1, dimensiones[1])

    # Conversión de la matriz numí©rica en matriz de cadenas
    matriz = matriz.astype(dtype = str)

    # Asignación de variables, ecuaciones y unidades
    matriz[0, 1: n_var + 1] = unidades[:, 0].T
    matriz[1: n_ec+1, 0] = lista_ec
    matriz[n_ec + 2: n_ec + 5, 1: n_var + 1] = unidades[:, 1: 4].T

    # Asignación del resto de celdas de cadenas
    matriz[0, 0] = 'Relación'
    matriz[n_ec + 1, 0] = 'Ocurrencias de v'
    matriz[n_ec + 2, 0] = 'Unidades de trabajo'
    matriz[n_ec + 3, 0] = 'Unidades SI'
    matriz[n_ec + 4, 0] = 'Sí­mbolo estándar'
    matriz[n_ec + 5, 0] = 'Valor'
    matriz[n_ec + 6, 0] = 'Secuencia de dato'
    matriz[n_ec + 7, 0] = 'Nº de Ecuación'
    matriz[0, n_var + 1] = 'Variables desconocidas'
    matriz[n_ec + 2: n_ec + 8, n_var + 1] = ''

    # Asignar uno si la variable está presente en una ecuación determinada
    init_mat(matriz, n_ec, n_var)

    # Extracción de la submatriz superior e inferior
    submat = conv_strtofloat(matriz, 1, 1, n_ec + 1, n_var + 1)
    submat2 = conv_strtofloat(matriz, n_ec + 5, 1, n_ec + 7, n_var)

    # Ciclo para obtener la columna de variables desconocidas
    for i in range(0, n_ec):
        submat = total_row(submat, i, n_var - 1)

    # Ciclo para obtener las ocurrencias de variables desconocidas
    for i in range(0, n_var):
        submat = total_col(submat, i, n_ec - 1)

    # Inicialización de variables
    cvc = 1 # cantidad de variables conocidas
    col_var = []
    fila_ec = []
    secuencia = 0 # secuencia en que se conocen las variabes
    lista_indices = []
    var_no_disp_user = []
    lista_val = []
    lista_ind = []
    pares = 1
    contador = 0
    edicion = False

    # Ejecutar el ciclo mientras existan variables desconocidas (cvc es el contador de variables desconocidas)
    while cvc > 0:
        
        hay_uno = False

        # Determinar si existe una ecuación que posea sólo una incógnita, y, de existir, determinar además el índice de dicha incógnita
        for i in range(0, n_ec): # se revisa toda la última columna en busqueda de ecuaciones con cálculo pendiente
            if submat[i, n_var] == 1: # un valor de 1 significa que es la variable a calcular.
                hay_uno = True
                fila_ec = i
                for j in range(0, n_var): # se busca en toda la fila el í­ndice de la variable incógnita.
                    if submat[i, j] == 1:
                        col_var = j

        # Despeje de una incógnita de una ecuación determinada
        if hay_uno:

            # Crear una lista de variables independientes y una lista de valores de variables independientes de una ecuación determinada
            lista_var, lista_val = [], []
            for i in range(0, n_var):
                if unidades[i, 0] in lista_ec[fila_ec]:
                    if not (col_var == i):
                        lista_var.append(variables[i])
                        lista_val.append(submat2[0, i])
            diccionario = dict(zip(lista_var, lista_val))

            # Obtener una ecuación en función de la variable dependiente
            expr = solve(lista_ec[fila_ec],variables[col_var])

            # Sustitución de los valores de las variables independientes en la expresión anterior
            submat2[0, col_var] = expr[0].evalf(subs=diccionario)

            # Actualizar submat una vez calculada una variable dependiente
            resta_unidad_col(submat, col_var, n_ec)
            total_col(submat, col_var, n_ec - 1)
            for i in range(0, n_ec):
                submat = total_row(submat, i, n_var - 1)

            # Contador para asignar la secuencia del dato (calculado por el programa)
            secuencia += 1
            submat2[1, col_var] = secuencia

            # Asigna el número de la ecuación empleada para el cálculo a la fila "Número de relación"
            submat2[2, col_var] = fila_ec + 1

            # Actualizar la lista de í­ndices de variables conocidas (suministradas por el usuario o calculadas)
            lista_indices.append(col_var)
            
        else:

            # Modo de recepción de datos
            if pares == 1 and not(edicion):
            
                # Lectura de datos
                datos = leer_datos(unidades, n_var, lista_indices, var_no_disp_user, submat2)

                # Si se produjo un error al leer los datos, solicitarlos nuevamente hasta que no se produzca ningún error
                while datos[1] == False:
                    datos = leer_datos(unidades, n_var, lista_indices, var_no_disp_user, submat2)

                # Almacenamiento de la variable booleana que indica si hubo o no edición de datos en una variable temporal
                edicion = datos[4]
                    
                # Número de pares de datos (un par está constituí­do por el í­ndice de una variable y su respectivo valor)
                pares = len(datos[5])
                pares_iniciales = len(datos[5])

                # Lista de valores e í­ndices de las variables correspondientes
                lista_val = datos[6]
                lista_ind = datos[5]

                # Actualizar la lista de variables introducidas por el usuario (no disponibles)
                if not(edicion):
                    var_no_disp_user.append(unidades[lista_ind[0], 0])

                # Eliminar el í­ndice de una variable de la lista de í­ndices
                if datos[7]:
                    lista_indices.remove(datos[2])

                # Introducir la variable suministrada por el usuario y actualizar las submatrices
                if edicion == False:
                    submat2[0, lista_ind[0]] = lista_val[0]
                    resta_unidad_col(submat, lista_ind[0], n_ec)
                    total_col(submat, lista_ind[0], n_ec - 1)
                    for i in range(0, n_ec):
                        submat = total_row(submat, i, n_var - 1)

                    # Contador para asignar la secuencia del dato (suministrado por el usuario)
                    secuencia = secuencia + 1
                    submat2[1, lista_ind[0]] = secuencia

                    # Actualizar la lista de í­ndices de variables conocidas (suministradas por el usuario o calculadas)
                    if edicion == False:
                        lista_indices.append(lista_ind[0])

            # Modo de edición de datos
            if edicion:

                # Inicializar la matriz principal y las submatrices. Sólo se hace cuando se comienza a procesar un conjunto de datos
                if pares == pares_iniciales:
                    secuencia = 0
                    contador = 0

                    matriz[1 : n_ec + 8, 1 : n_var + 2] = 0
                    matriz[n_ec + 2: n_ec + 5, 1: n_var + 1] = unidades[:, 1: 4].T
                    matriz[n_ec + 2: n_ec + 8, n_var + 1] = ''

                    init_mat(matriz, n_ec, n_var)
                    submat = conv_strtofloat(matriz, 1, 1, n_ec + 1, n_var + 1)
                    submat2 = conv_strtofloat(matriz, n_ec + 5, 1, n_ec + 7, n_var)

                    # Ciclo para obtener la columna de variables desconocidas
                    for i in range(0, n_ec):
                        submat = total_row(submat, i, n_var - 1)

                    # Ciclo para obtener las ocurrencias de variables desconocidas
                    for i in range(0, n_var):
                        submat = total_col(submat, i, n_ec - 1)
                    
                # Lista de valores e í­ndices de las variables correspondientes    
                lista_val = datos[6]
                lista_ind = datos[5]

                # Actualización de submatrices
                submat2[0, lista_ind[contador]] = lista_val[contador]
                resta_unidad_col(submat, lista_ind[contador], n_ec)
                total_col(submat, lista_ind[contador], n_ec - 1)
                for i in range(0, n_ec):
                    submat = total_row(submat, i, n_var - 1)

                # Contador para asignar la secuencia del dato (suministrado por el usuario)
                secuencia = secuencia + 1
                submat2[1, lista_ind[contador]] = secuencia

                # Control de la salida del modo de edición
                if pares == 1:
                    edicion = False

                # Actualización del número de pares
                elif pares > 1:
                    pares -= 1

                # Actualización del contador de pares
                contador += 1
            
        # Actualizar la última columna (sumatoria de variables)
        total_col(submat, n_var, n_ec - 1)
        cvc = submat[n_ec, n_var]

    # Actualización de la matriz principal
    matriz[1 : n_ec + 2, 1: n_var + 2] = submat
    matriz[n_ec + 5: n_ec + 8, 1: n_var + 1] = submat2

    # Muestra de resultados
    print('', 'La matriz final es: ', sep='\n')
    print(matriz,'\n')


if __name__ == '__main__': 
    main()