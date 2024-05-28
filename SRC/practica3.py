from SRC.practica2 import conectado_con

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
    
    vertices, aristas = grafo_lista

    vecinos = encuentra_vecinos(grafo_lista, nodo_ini)

    for vecino in vecinos:
        ## Caso Base Positivo
        if vecino == nodo_fin:
            return [nodo_ini, nodo_fin]
        
        ## Llamada Recursiva
        vertices_reducidos = [v for v in vertices if v != nodo_ini]
        aristas_reducidas = [(v1, v2) for (v1, v2) in aristas if v1 != nodo_ini and v2 != nodo_ini]
        grafo_reducido = (vertices_reducidos, aristas_reducidas)

        camino = encuentra_camino_abierto(grafo_reducido, vecino, nodo_fin)

        ## Vuelta Positiva
        if camino != []:
            return [nodo_ini] + camino
    
    return []

def encuentra_camino_cerrado(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	a
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    pass

def encuentra_recorrido(grafo_lista, nodo_ini, nodo_fin):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	b
	f
    Ejemplo retorno: 
        ['b','c','d','e','c','f']
    '''
    pass

def encuentra_circuito(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['d','a','b','d','c','e','d']
    '''
    pass 	 	

def encuentra_camino_simple(grafo_lista, nodo_ini, nodo_fin):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d']
    '''
    pass

def encuentra_ciclo(grafo_lista, nodo):
    '''
    Ejemplo Entrada: 
        (['a','b','c','d','e','f'],[('a','b'),('a','d'),('b','d'),('b','c'),('c','d'),('c','e'),('d','e'),('c','f')])
	d
    Ejemplo retorno: 
        ['a','b','c','d','a']
    '''
    pass

def determina_caminos(camino_lista):
    '''
    Dado una lista que representa un camino, camino cerrado, recorrido, circuito, camino simple o ciclo,
    me devuelva de qué se trata
    Ejemplo Entrada: 
        ['d','a','b','d','c','e','d']
    Ejemplo formato salida: 
        Circuito

    '''
    pass