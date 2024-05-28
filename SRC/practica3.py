def valida_nodo_en_grafo(grafo_lista, nodo):
    '''
    Dado un grafo en representacion de lista, y un nodo, me devuelve True si el nodo está en el Grafo
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
	'F'
    Ejemplo formato salida: 
        False
    '''
    vertices = grafo_lista[0]
    return (nodo in vertices)
def encuentra_camino(grafo_lista, nodo_ini, nodo_fin):
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
    inicio = nodo_ini
    fin = nodo_fin
    
    if not valida_nodo_en_grafo(grafo_lista, inicio) or not valida_nodo_en_grafo(grafo_lista, fin):
        return []
    
    if inicio == fin:
        return [inicio]
    
    
    
    pass

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