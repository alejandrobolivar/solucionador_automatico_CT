'''
Biblioteca para la identificación de variables dependientes e independientes en una oración

'''

def analizar_oracion(oracion, unidades_trab, descripción, unidades_si, variable, dep, indep):

    '''
    input:
        oracion: oración del enunciado a revisar, es una lista de palabras
        unidades_trab: unidades de trabajo de las variables según el enunciado
        descripción: nombre de trabajo de la variable
        unidades_si: unidad según el SI
        variable: nombre de la variable según el SI

    output:
        dep: lista de variables dependientes conformada por     [simbolo_si,simbolo_trab,unidad_si]
        indep: lista de variables independientes conformada por [simbolo_si,simbolo_trab,valor,unidad_trab,unidad_si]

    funciones:
        es_numero
        es_var_independiente
        get_indice_simbolo_trab
        get_indice_unidad_trab
        llenarlistadatos
        set_var_indep
        set_var_dep

    '''
    # global caso

    # oracion=enunciado[contoracion].split() # Oración del enunciado

    contpalabra = 0

    print(f'oracion = {oracion}')
    # input('analizar_oracion')
    while (contpalabra <= len(oracion)-1): # Recorre todas las parabras de las lista de palabras de la oración
        print(oracion[contpalabra])
        # input()
        
        '''
        print(get_indice_simbolo_trab(oracion[contpalabra].replace('.',''), descripción) != -1)
        print(contpalabra < len(oracion)-1 and get_indice_simbolo_trab(f"{oracion[contpalabra]} {oracion[contpalabra+1].replace('.', '')}", descripción) != -1)
        print(es_numero(oracion[contpalabra]) and oracion[contpalabra-1] not in ['figura', 'tabla'] and 
        contpalabra < len(oracion)-1 and get_indice_unidad_trab(oracion[contpalabra+1].replace('.', ''), unidades_trab) != -1)
        '''
        
        if (get_indice_simbolo_trab(oracion[contpalabra].replace('.',''), descripción) != -1 or 
            (contpalabra < len(oracion)-1 and get_indice_simbolo_trab(f"{oracion[contpalabra]} {oracion[contpalabra+1].replace('.', '')}", descripción) != -1) or
            (es_numero(oracion[contpalabra]) and oracion[contpalabra-1] not in ['figura', 'tabla'] and 
            contpalabra < len(oracion)-1 and get_indice_unidad_trab(oracion[contpalabra+1].replace('.', ''), unidades_trab) != -1)
            ):

            lstDatos = ['','','','','','']
            lstDatos = llenarlistadatos(lstDatos, oracion, contpalabra, descripción)
            # print(contpalabra,len(oracion),oracion)
            print('lstDatos->', lstDatos)
            # input()
            caso = es_var_independiente(lstDatos, unidades_trab, descripción)
            print(f'caso = {caso}')

            if caso != -1: # Variable independiente
                set_var_indep(caso, contpalabra, lstDatos, unidades_trab, oracion, variable, unidades_si, indep, descripción)
            else: # Variable dependiente
                set_var_dep(dep, oracion, contpalabra, descripción, unidades_si, variable)

            # print(oracion)
            contpalabra -= 1
        contpalabra += 1 # Cuenta cada palabra de la lista oración
    # contoracion=contoracion+1 # Cuenta cada oración del enunciado


# devuelve la cantidad de elementos que son comunes en ambas listas

def conteo(lst1, lst2):
    '''
    conteo, devuelve la cantidad de elementos que son comunes en ambas listas.
    Input:
        lst1, lista anidada de variables de referencia
        lst2, lista anidada de variables identificadas
    Output
        c: cantidad de coincidencias entre las listas

    '''
    #Referencia lst1
    #Identificado lst2
    #if len(lst2)>len(lst1):
        #print('Identificación en exceso')
    #elif len(lst2)<len(lst1):
        #print('Identificación deficiente')

    c = 0 # Cantidad de elementos que son comunes en ambas listas
    i = 0
    # nl1=len(lst1)
    while i < len(lst1): # Referencia

        j = 0

        while j < len(lst2):  # Recorre toda lst2
            lst2[j][2] = lst2[j][2].strip()
            if lst1[i] == lst2[j]:

                lst1.pop(i)
                lst2.pop(j)
                c += 1
                i -= 1
                break

            j += 1

        i += 1

    # if c==len(lst1):
        # print('Todos acertados')
    # else:
        #print(nl1-c,' desaciertos')
    # print(c, ' aciertos')
    return c


def convertir_str_list(cad, n):
    '''
    convertir_str_list, Convierte una cadena cad en una lista de listas, donde
    cada lista interna esta conformada por n elementos.
    Input:
        cad, cadena a convertir en una lista de listas.
        n, cantidad de elementos de la lista interna.
    '''
    cad = cad.replace('[', '')
    cad = cad.replace(']', '')
    cad = cad.replace('\'', '')
    cad = cad.replace(' ', '')
    lst = cad.split(',')
    lst3 = []

    i = 0
    j = 0
    # print(lst)
    for i in range(len(lst) // n):

        lst2 = []

        while j < (i + 1) * n:
            lst2.append(lst[j])
            j += 1

        lst3.append(lst2)

    # print(l3)
    return(lst3)


def es_numero(cad):
    '''
    es_numero, verifica si cad es un número entero o real o ninguno
    Input:
        cad, es la cadena a verificar si es un número válido entero o real.
    Output:
        True, es un número.
        False, no es un número
    '''
    try:
        float(cad) # for int, long and float
        return True
    except ValueError:
        return False


def es_unidad_simbtrab(unid, unid_simb_trab):
    '''
    es_unidad_simbtrab, verifica si el parámetro unid es una unidad válida
    buscándola en la lista unid_simb_trab que contiene todas las unidades
    de medida relaciondas al identificador de la variable.

    Input:
        unid, es la unidad a buscar.
        unid_simb_trab, lista de unidades de trabajo válidas.
    Output:
        True: es una unidad válida
    '''

    return unid in unid_simb_trab


def es_var_independiente(lista_datos,unidades_trab,descripción):
    '''
    es_var_independiente, verifica si la lista lista_datos corresponde a la 
    estructura de una variable independiente.
    Parámetro:
        lista_datos, es una lista que contiene los probables elementos de una 
        variable independiente nombre,nombre,valor,unidad,nombre,nombre.
    '''
    caso = -1
    if es_numero(lista_datos[2]) and get_indice_unidad_trab(lista_datos[3],unidades_trab)!=-1:        
        if (get_indice_simbolo_trab(lista_datos[0]+' '+lista_datos[1],descripción)!=-1):            
            if (es_unidad_simbtrab(lista_datos[3],unidades_trab[get_indice_simbolo_trab(lista_datos[0]+' '+lista_datos[1],descripción)])):
                caso = 0
        elif get_indice_simbolo_trab(lista_datos[1],descripción)!=-1:
            if (es_unidad_simbtrab(lista_datos[3],unidades_trab[get_indice_simbolo_trab(lista_datos[1],descripción)])):
                caso = 1
        else:            
            if get_indice_simbolo_trab(lista_datos[4]+' '+lista_datos[5],descripción)!=-1 and (es_unidad_simbtrab(lista_datos[3],unidades_trab[get_indice_simbolo_trab(lista_datos[4]+' '+lista_datos[5],descripción)])):
                caso = 2
            elif get_indice_simbolo_trab(lista_datos[4],descripción)!=-1 and (es_unidad_simbtrab(lista_datos[3],unidades_trab[get_indice_simbolo_trab(lista_datos[4],descripción)])):
                caso = 3
            else:
                caso = 4
    return caso



def file_to_dict(file_name):
    result_dict = {}
    with open(file_name) as f:
        for line in f:
            #print(line)
            key, val = line.strip().split(':')
            result_dict[key.strip()] = val.strip()
    return result_dict


def filtros2(e, dict):  # sourcery skip: avoid-builtin-shadow
    ''''
    Devuelve los enunciados con los símbolos de unidades,
    caracteres especiales y palabras compuestas reemplazados
    por la descripción según el sistema internacional de unidades
    '''

    for i in range(len(e['enunciados'])):  # Recorre todos los enunciados
        for key, val in dict.items():  # Recorre el diccionario de variables
            e['enunciados'][i] = e['enunciados'][i].replace(key, val)

        print ('Simplificación ortografica %s \n',i,') ', e['enunciados'][i])
        print("\n")


def get_indice_simbolo_trab(cad_descripcionvartrab, descripción):
    '''
    get_indice_simbolo_trab, Devuelve el índice donde se encuentra
    cad_descripcionvartrab en el pandas.core.series.Series descripción o -1
    si no lo encuentra.

    Parámetro:
        cad_descripcionvartrab, es una cadena conformada por uno o dos nombres
        de una posible variable.
        descripción, es una lista que contiene nombrevar_simbolotrab extraído de listadevariables2.csv

    for i, desc in enumerate(descripcion):
        simbolos_trab = [var.split(':')[0] for var in desc.split(',')]
        if cad_descripcionvartrab in simbolos_trab:
            return i
    return -1
    '''
    for i, desc in enumerate(descripción):
        pairs = desc.split(',')
        for pair in pairs:
            key, value = pair.split(':')
            if cad_descripcionvartrab == key:
                return i
    return -1


def get_indice_unidad_trab(unid, unidades_trab):
    '''
    get_indice_unidad_trab, devuelve el indice según la unidad de trabajo unid,
    o -1 si no la encuentra.
    Parámetro:
        unid, es la unidad de medida que se verifica si es una unidad de
        trabajo válida
    '''
    for i in range(len(unidades_trab)):
        for u in unidades_trab[i].split(','):
            if unid == u.lower():
                return i
    return -1


def get_simbolo_trab(cad_descripcionvartrab, descripción):
    '''
    get_simbolo_trab, Devuelve el símbolo de la variable de trabajo,
    dada la descripción de la variable cad_descripcionvartrab, o -1 si no
    lo encuentra.
    Parámetro:
        cad_descripcionvartrab, es el nombre de la posile variable a la cual se le
        busca el símbolo de trabajo respectivo.
    '''
    i = 0
    j = 0
    for i in range(len(descripción)):
        for j in range(len(descripción[i].split(','))):
            if cad_descripcionvartrab == descripción[i].split(',')[j].split(':')[0]:
                return descripción[i].split(',')[j].split(':')[1]
    return -1


def llenarlistadatos(lstDatos, oracion, contpalabra, descripción):
    '''
    llenarlistadatos, devuelve una lista con los elementos correspondientes
    para identificar a una variable independiente.
    Parámetros:
        lstDatos, lista con los elementos de una posible variable independiente
        oracion, segmento del enunciado para buscar posibles variables
        independientes
        contpalabra, contador de palabras
    '''
    # Caso 0
    if (contpalabra < len(oracion) - 3 and get_indice_simbolo_trab(f'{oracion[contpalabra]} {oracion[contpalabra + 1]}', descripción) != -1):
        lstDatos = [oracion[contpalabra], oracion[contpalabra+1], oracion[contpalabra+2], oracion[contpalabra+3].replace('.', ''), '', '']
    elif (contpalabra < len(oracion)-2 and (get_indice_simbolo_trab(oracion[contpalabra], descripción) != -1)):
        lstDatos = ['', oracion[contpalabra], oracion[contpalabra+1], oracion[contpalabra+2].replace('.',''), '','']
    elif (contpalabra < len(oracion)-3 and (es_numero(oracion[contpalabra]))):
        lstDatos = ['', '', oracion[contpalabra], oracion[contpalabra+1].replace('.', ''), oracion[contpalabra+2], oracion[contpalabra+3]]
    elif (contpalabra < len(oracion)-2 and (es_numero(oracion[contpalabra]))):
        lstDatos = ['', '', oracion[contpalabra], oracion[contpalabra+1].replace('.', ''), oracion[contpalabra+2],'']
    elif (contpalabra < len(oracion)-1 and (es_numero(oracion[contpalabra]))):
        lstDatos = ['', '', oracion[contpalabra], oracion[contpalabra+1].replace('.', ''), '', '']

    return lstDatos


def print_resultados_enunciados(contninguno, conttotal, contindep, contdep,
                                contambos, lstNinguno, lstFallaIndep, lstFallaDep):
    print('\nAnálisis de enunciados:')
    print(f'Total de enunciados analizados=\t {conttotal}')
    print('Desacierto en ambos y porcentaje=\t %d \t %.2f ' % (contninguno, (contninguno / conttotal * 100)),'%')
    print('Porcentaje Aciertos Var Indep =\t %d \t %.2f ' % (contindep, (contindep / conttotal * 100)),'%')
    print('Porcentaje Aciertos Var Dep =\t %d \t %.2f ' % (contdep, (contdep / conttotal * 100)),'%')
    print('Total de aciertos en ambos y porcentaje=\t %d \t %.2f' % (contambos, (contambos / conttotal * 100)),'%')

    print(f'Enunciados con Falla en ambos=\t {lstNinguno}')
    print(f'Enunciados con Falla en Independientes=\t {lstFallaIndep}')
    print(f'Enunciados con Falla en Dependientes=\t {lstFallaDep}')


def print_resultados_variables(contaciertosindep, conttotalvarindep, contaciertosdep, conttotalvardep):
    print('\nAnálisis por variable')
    print('Variable independientes acertadas, Total y porcentaje=\t %d \t %d \t %.2f ' % (contaciertosindep, conttotalvarindep, (contaciertosindep * 100 / conttotalvarindep)), '%')
    print('Variable dependientes acertadas, Total y porcentaje=\t %d \t %d \t %.2f ' % (contaciertosdep, conttotalvardep, (contaciertosdep * 100 / conttotalvardep)),'%')
    print(f'Total de variables analizadas=\t {conttotalvarindep + conttotalvardep}')
    print('Total de variables acertadas y porcentaje=\t %d \t %.2f ' % ((contaciertosindep + contaciertosdep), ((contaciertosindep + contaciertosdep) * 100 / (conttotalvarindep + conttotalvardep))), '%')


def set_simbolo_trab(lstDatos, caso, contpalabra, oracion, descripción):
    '''
    asignarsimbolo_trab, devuelve el simbolo de trabajo correspondiente a la variable.
    Parámetros:
        caso: depende de la estructura de la variable
        simbolo_trab: es el símbolo de trabajo de la variable según se refiere en el enunciado
        oracion, segmento del enunciado para buscar posibles variables independientes
        contpalabra, contador de palabras
        lstDatos, lista con los elementos de una posible variable independiente
    '''

    if caso == 0:
        simbolo_trab = get_simbolo_trab(f'{lstDatos[0]} {lstDatos[1]}', descripción)
        oracion.pop(contpalabra + 3)
        oracion.pop(contpalabra + 2)

    elif caso == 1:
        simbolo_trab = get_simbolo_trab(lstDatos[1],descripción)
        oracion.pop(contpalabra + 2)

    elif caso == 2:
        simbolo_trab = get_simbolo_trab(f'{lstDatos[4]} {lstDatos[5]}', descripción)
        oracion.pop(contpalabra + 3)
        oracion.pop(contpalabra + 2)

    elif caso == 3:
        simbolo_trab = get_simbolo_trab(lstDatos[4],descripción)
        oracion.pop(contpalabra + 2)

    else: # sin  símbolo de trabajo, se asigna el símbolo del SI
        simbolo_trab = ''

    oracion.pop(contpalabra + 1)
    oracion.pop(contpalabra)

    return simbolo_trab


def set_var_dep(dep,oracion,contpalabra,descripción,unidades_si,variable):
    # Se verifica que el identificador de dos palabras corresponda a una variable válida
    if contpalabra<len(oracion)-1 and get_indice_simbolo_trab(oracion[contpalabra]+' '+oracion[contpalabra+1].replace('.',''),descripción)!=-1:
        simbolo_trab=get_simbolo_trab(oracion[contpalabra]+' '+oracion[contpalabra+1].replace('.',''),descripción)
        unidad_si=unidades_si[get_indice_simbolo_trab(oracion[contpalabra]+' '+oracion[contpalabra+1].replace('.',''),descripción)]
        simbolo_si=variable[get_indice_simbolo_trab(oracion[contpalabra]+' '+oracion[contpalabra+1].replace('.',''),descripción)]
        oracion.pop(contpalabra+1)
        oracion.pop(contpalabra)
    else:
        simbolo_trab=get_simbolo_trab(oracion[contpalabra].replace('.',''),descripción)
        unidad_si=unidades_si[get_indice_simbolo_trab(oracion[contpalabra].replace('.',''),descripción)]
        simbolo_si=variable[get_indice_simbolo_trab(oracion[contpalabra].replace('.',''),descripción)]
        oracion.pop(contpalabra)
    dep.append([simbolo_si,simbolo_trab,unidad_si])
    #print(simbolo_si, ' ', simbolo_trab,' =?',' ', unidad_si,'\n')



def set_var_indep(caso, contpalabra, lstDatos, unidades_trab, oracion, variable, unidades_si,indep, descripción):
    # print(' Buscar Ind ', valor, '  ' , unidad_trab)
    # Verificar si en verdad tiene unidad de trabajo

    # global simbolo_trab

    unidad_trab = lstDatos[3]
    valor = lstDatos[2]
    simbolo_si = variable[get_indice_unidad_trab(unidad_trab, unidades_trab)]
    unidad_si = unidades_si[get_indice_unidad_trab(unidad_trab, unidades_trab)]
    simbolo_trab = ''

    if unidad_trab == unidad_si.lower():
        unidad_trab = unidad_si
    # print(caso)
    # print(contpalabra)
    simbolo_trab = set_simbolo_trab(lstDatos, caso, contpalabra, oracion, descripción)
    indep.append([simbolo_si, simbolo_trab, valor, unidad_trab, unidad_si])
    # print(simbolo_si, ' ', simbolo_trab, ' =', valor, ' ', unidad_trab,' ',unidad_si,'\n')


def detectar_vars(data, dfvar, dict):
    ################## Detección de Variables ################################

    #data = pd.read_csv('enunciados.csv',sep='|',encoding = "ISO-8859-1")
    #print ('Texto Original\n',data['enunciados'][0])
    #print("\n")
    filtros2(data, dict)
    '''
    La estructura del archivo  listadevariables2.csv, es la siguiente:
    nombrevar_simbolotrab|unidad_trab|simbolo_si|unidad_si|
    tiempo:t,tarda:t,tiempo vuelo:tv,tiempo máximo:tmax|s,min,h|t|s
    ...
    De la misma forma se hace con las diversas variables.
    '''
    print(data['enunciados'])
    descripción = dfvar['nombrevar_simbolotrab'] # Nombre de la variable
    unidades_trab = dfvar['unidad_trab'] # Unidades de trabajo
    variable = dfvar['simbolo_si'] # Símbolo según el SI
    unidades_si = dfvar['unidad_si'] # Unidades según el SI

    #dictdesc = {}
    contdep = 0
    contindep = 0
    contambos = 0
    conttotal = 0
    contninguno = 0
    contaciertosindep = 0
    contaciertosdep = 0
    conttotalvarindep = 0
    conttotalvardep = 0
    lst_ninguno = []
    lst_fallaindep = []
    lst_falladep = []
    lst_enunciado = []  # Lista de oraciones en el enunciado
    lst_oracion = []  # Lista de palabras de la oración en el enunciado

    #for line in descripción:
    #    for t in line.split(','):
            # diccionario con el nombre de la variable de trabajo y el símbolo de trabajo
    #        dictdesc[t.split(":")[0]] = t.split(":")[1]

    #print(dictdesc)

    #sys.exit()

    for contenunciado in range(len(data['enunciados'])): # Recorre cada enunciado

        # Enunciado convertido en lista cuyos elementos son oraciones.
        lst_enunciado = data['enunciados'][contenunciado].split('. ')
        #print(contenunciado,lst_enunciado)

        contoracion = 0
        lst_dep = []  # Lista para almacenar variables dependientes
        lst_indep = []  # Lista para almacenar variables in dependientes
        for contoracion in range(len(lst_enunciado)): # Recorre cada oración del enunciado
            #print('Siguiente oración',contoracion)
            #input()

            # Oración convertida en lista de palabras.
            lst_oracion = lst_enunciado[contoracion].split()
            analizar_oracion(lst_oracion, unidades_trab, descripción,unidades_si, variable, lst_dep, lst_indep)

        print('Referencia')
        print(contenunciado,'Datos de Entrada:\n',data['varindep'][contenunciado])
        print('Calcular:\n',data['vardep'][contenunciado])
        print('Identificados')
        print('Datos de Entrada:\n',lst_indep)
        print('Calcular:\n',lst_dep)
        #input()
        #lista_estadisticas

        if (str(lst_indep) != data['varindep'][contenunciado]
        and str(lst_dep) != data['vardep'][contenunciado]):
            contninguno += 1
            #print('No Acerto Ninguno', contninguno)
            lst_ninguno.append(contenunciado)
            lst_falladep.append(contenunciado)
            lst_fallaindep.append(contenunciado)
            #input()

        if (str(lst_indep) == data['varindep'][contenunciado]
        and str(lst_dep) == data['vardep'][contenunciado]):
            contindep += 1
            contdep += 1
            contambos += 1
            #print('Acerto ambos',contambos)

        elif (str(lst_indep) == data['varindep'][contenunciado]):
            contindep += 1
            #print('Acerto Var Ind', contindep)
            lst_falladep.append(contenunciado)
            #input()

        elif (str(lst_dep) == data['vardep'][contenunciado]):
            contdep += 1
            #print('Acerto Var Dep', contdep)
            lst_fallaindep.append(contenunciado)
            #input()

        conttotal += 1
        conttotalvarindep += len(convertir_str_list(data['varindep'][contenunciado], 5))
        conttotalvardep += len(convertir_str_list(data['vardep'][contenunciado], 3))
        contaciertosindep += conteo(convertir_str_list(data['varindep'][contenunciado], 5), lst_indep)
        contaciertosdep += conteo(convertir_str_list(data['vardep'][contenunciado], 3), lst_dep)
        #input('Siguiente enunciado')
    print_resultados_variables(contaciertosindep, conttotalvarindep, contaciertosdep, conttotalvardep)
    print_resultados_enunciados(contninguno, conttotal, contindep, contdep, contambos, lst_ninguno, lst_fallaindep, lst_falladep)


def test():
    import pandas as pd
    # Load the data from a CSV file
    data = pd.read_csv('../dataset/enunciadosCT1.csv',sep='|')
    dfvar = pd.read_csv('../dataset/listadevariables2.csv', sep='|')
    dict_text_to_descrip = file_to_dict("../dataset/convert_text_to_descripcion_SI.txt")

    filtros2(data, dict_text_to_descrip)

    descripción = dfvar['nombrevar_simbolotrab'] # Nombre de la variable
    unidades_trab = dfvar['unidad_trab'] # Unidades de trabajo
    variable = dfvar['simbolo_si'] # Símbolo según el SI
    unidades_si = dfvar['unidad_si'] # Unidades según el SI

    lst_enunciado = []  # Lista de oraciones en el enunciado
    lst_oracion = []  # Lista de palabras de la oración en el enunciado

    lst_dep = []  # Lista para almacenar variables dependientes
    lst_indep = []  # Lista para almacenar variables in dependientes

    # Enunciado convertido en lista cuyos elementos son oraciones.
    lst_enunciado = data['enunciados'][0].split('. ')

    contoracion = 0
    for contoracion in range(len(lst_enunciado)):
        lst_oracion = lst_enunciado[contoracion].split()
        analizar_oracion(lst_oracion, unidades_trab, descripción,
                         unidades_si, variable, lst_dep, lst_indep)

    print('Identificados')
    print('Datos de Entrada:\n',lst_indep)
    print('Calcular:\n',lst_dep)
    #input()
    
if __name__ == '__main__ ':
    test()
