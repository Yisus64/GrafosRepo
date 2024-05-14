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

def conectado_con(grupo: set, aristas):
    for v1, v2 in aristas:
        if v1 in grupo:
            grupo.add(v2)
        if v2 in grupo:
            grupo.add(v1)
    
    return grupo
    
def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    V, E = grafo_lista
    aristas = E
    componentes = list()
    v_usados = set()
    for v in V:
        if v in v_usados:
            continue
        grupo = {v}
        nuevo_g = conectado_con(grupo, aristas)
        while nuevo_g != grupo:
            grupo = nuevo_g
            nuevo_g = conectado_con(grupo, aristas)
        
        componentes.append(list(grupo))
        v_usados = v_usados | grupo
    
    return componentes







def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    return (len(componentes_conexas(grafo_lista)) == 1)
