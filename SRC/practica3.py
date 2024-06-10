from SRC.practica2 import *
from SRC.practica1 import *


def valida_nodo_en_grafo(grafo_lista, nodo):
    '''
    Dado un grafo en representacion de lista, y un nodo, me devuelve True si el nodo está en el Grafo
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
  'F'
    Ejemplo formato salida: 
        False
    '''
    V, _ = grafo_lista
    return (nodo in V)


def encuentra_vecinos(grafo, vertice):
    _, E = grafo
    vecinos = set()
    for (v1, v2) in E:
        if v1 == vertice:
            vecinos.add(v2)
        if v2 == vertice:
            vecinos.add(v1)

    if vertice in vecinos:
        vecinos.remove(vertice)
    return list(vecinos)


def vertices_en_camino(camino):
    return set(camino)


EXTRAINFO_ENCUENTRA_CAMINO_ABIERTO = True


def encuentra_camino_abierto(grafo_lista, nodo_ini, nodo_fin):
    '''
    Dado un grafo en representacion de lista, el nodo inicial y final de un camino
    Me devuelve una lista con los vértices del camino, o vacio si no existe
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
  a
  b
    Ejemplo retorno: 
        ['a','b','d','c','e','d','b']
    '''

    vecinos = encuentra_vecinos(grafo_lista, nodo_ini)
    caminos = [nodo_ini]
    caminos_ant = []
    while vertices_en_camino(caminos) != vertices_en_camino(caminos_ant):
        if EXTRAINFO_ENCUENTRA_CAMINO_ABIERTO: print(caminos)
        caminos_ant = caminos
        caminos = []

        for camino in caminos_ant:
            ver_relevante = camino[-1]
            if (ver_relevante == nodo_fin):
                return list(camino)
            vecinos = encuentra_vecinos(grafo_lista, ver_relevante)
            for vecino in vecinos:
                caminos.append(camino + vecino)

    return []


def encuentra_camino_cerrado(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
  a
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''

    vertices, aristas = grafo_lista
    vecinos = encuentra_vecinos(grafo_lista, nodo)
    for vecino in vecinos:
        camino = encuentra_camino_abierto(grafo_lista, vecino, nodo)
        if camino != []:
            return [nodo] + camino

    return []


EXTRAINFO_ENCUENTRA_RECORRIDO = True


def encuentra_recorrido(grafo_lista, nodo_ini, nodo_fin):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
  b
  f
    Ejemplo retorno: 
        ['b','c','d','e','c','f']
    '''
    vertices, aristas = grafo_lista

    vecinos = encuentra_vecinos(grafo_lista, nodo_ini)
    if EXTRAINFO_ENCUENTRA_RECORRIDO: print(vecinos)

    for vecino in vecinos:
        ## Caso Base Positivo
        if vecino == nodo_fin:
            return [nodo_ini, nodo_fin]

        ## Llamada Recursiva
        aristas_reducidas = [
            a for a in aristas
            if a != (nodo_ini, vecino) and a != (vecino, nodo_ini)
        ]
        grafo_reducido = (vertices, aristas_reducidas)

        camino = encuentra_recorrido(grafo_reducido, vecino, nodo_fin)

        ## Vuelta Positiva
        if camino != []:
            return [nodo_ini] + camino

    return []


def encuentra_circuito(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
  d
    Ejemplo retorno: 
        ['d','a','b','d','c','e','d']
    '''
    vertices, aristas = grafo_lista
    vecinos = encuentra_vecinos(grafo_lista, nodo)
    for vecino in vecinos:
        aristas_reducidas = [
            a for a in aristas if a != (nodo, vecino) and a != (vecino, nodo)
        ]
        grafo_reducido = (vertices, aristas_reducidas)
        camino = encuentra_recorrido(grafo_reducido, vecino, nodo)
        if camino != []:
            return [nodo] + camino

    return []


EXTRAINFO_ENCUENTRA_CAMINO_SIMPLE = True


def encuentra_camino_simple(grafo_lista, nodo_ini, nodo_fin):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
  d
    Ejemplo retorno: 
        ['a','b','c','d']
    '''
    vertices, aristas = grafo_lista

    vecinos = encuentra_vecinos(grafo_lista, nodo_ini)

    if EXTRAINFO_ENCUENTRA_CAMINO_SIMPLE: print(vecinos)

    for vecino in vecinos:
        ## Caso Base Positivo
        if vecino == nodo_fin:
            return [nodo_ini, nodo_fin]

        ## Llamada Recursiva
        vertices_reducidos = [v for v in vertices if v != nodo_ini]
        aristas_reducidas = [(v1, v2) for (v1, v2) in aristas
                             if v1 != nodo_ini and v2 != nodo_ini]
        grafo_reducido = (vertices_reducidos, aristas_reducidas)

        camino = encuentra_camino_simple(grafo_reducido, vecino, nodo_fin)

        ## Vuelta Positiva
        if camino != []:
            return [nodo_ini] + camino

    return []


def encuentra_ciclo(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
    d
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    vertices, aristas = grafo_lista
    vecinos = encuentra_vecinos(grafo_lista, nodo)

    if EXTRAINFO_ENCUENTRA_CAMINO_SIMPLE: print(vecinos)

    for vecino in vecinos:
        aristas_reducidas = [
            a for a in aristas if a != (nodo, vecino) and a != (vecino, nodo)
        ]

        grafo_reducido = (vertices, aristas_reducidas)
        camino = encuentra_camino_simple(grafo_reducido, vecino, nodo)
        if camino != []:
            return [nodo] + camino

    return []


def determina_aristas(camino_lista):
    aristas = []
    i = 0
    index = len(camino_lista)

    while i < index - 1:
        if (len(aristas) + 1) == len(camino_lista):
            continue
        else:
            aristas.append((camino_lista[i], camino_lista[i + 1]))
        i += 1

    return aristas


def determina_caminos(camino_lista):
    '''
    Dado una lista que representa un camino, camino cerrado, recorrido, circuito, camino simple o ciclo,
    me devuelva de qué se trata
    Ejemplo Entrada: 
        ['d','a','b','d','c','e','d']
    Ejemplo formato salida: 
        Circuito

    '''
    aristas = determina_aristas(camino_lista)
    index = len(camino_lista)
    i = -1
    mismo_ini_fin = False
    repetidos_nodos = False
    repetidos_aristas = False

    if camino_lista[0] == camino_lista[index - 1]:
        mismo_ini_fin = True

    for nodo in camino_lista:
        i += 1
        if camino_lista.count(nodo) > 1 and i != 0 and i != index - 1:
            repetidos_nodos = True
        else:
            continue

    for arista in aristas:
        if aristas.count(arista) > 1 or aristas.count(arista[::-1]) >= 1:
            repetidos_aristas = True
        else:
            continue

    if aristas == []:
        return 'nada'
    elif len(camino_lista) == 1:
        return 'Un solo nodo'
    elif len(camino_lista) == 2:
        return 'Dos nodos'
    elif mismo_ini_fin == True:
        if repetidos_nodos and repetidos_aristas:
            return 'Camino Cerrado'
        elif repetidos_nodos and not repetidos_aristas:
            return 'Circuito'
        else:
            return 'Ciclo'
    elif mismo_ini_fin == False:
        if repetidos_nodos and repetidos_aristas:
            return 'Camino Abierto'
        elif repetidos_nodos and not repetidos_aristas:
            return 'Recorrido'
        else:
            return 'Camino Simple'
    else:
        return 'No se que hiciste'
