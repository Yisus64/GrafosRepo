def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    V, E = grafo_lista
    grados = dict()
    for v in V:
        grados[v] = 0

    for v1, v2 in E:
        grados[v1] += 1
        grados[v2] += 1
    
    return grados

def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    grados = cuenta_grado(grafo_lista)
    aislados = []
    for vertice in grados.keys():
        if grados[vertice] == 0:
            aislados.append(vertice)
    
    return aislados

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conex
    as.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    V, E = grafo_lista
    aristas = E
    grupos = []
    while aristas:
        grupo = {}
        v1, v2 = aristas.pop()
        for arista in aristas:



def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    pass
