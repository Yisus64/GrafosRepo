#! /usr/bin/python

# 1ra Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys

def lee_grafo_stdin(grafo):
    """
    Recibe como argumento un grafo representado como una lista de tipo:
    Ejemplo Entrada: 
       ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    
    donde el 1er elemento se corresponde a la cantidad de vertices,
    y por ultimo las aristas existentes.

    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    """
    
    largo = grafo[0]
    largo = int(largo)
    vertices = grafo[1:largo+1]
    raw_aristas = grafo[largo+1:]

    aristas: List[Tuple[chr, chr]] = []
    for raw_arista in raw_aristas:
        arista = (raw_arista[0], raw_arista[2])
        aristas.append(arista)
    
    return (vertices, aristas)
    



def lee_grafo_archivo(file_path):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    with open(file_path, "r") as f:
        raw = []
        for line in f:
            line = line[:-1]
            raw.append(line)
        
        return lee_grafo_stdin(raw)



def imprime_grafo_lista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    print(grafo)

#################### FIN EJERCICIO PRACTICA ####################
def lee_entrada_1():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    '''
    data_input = []
    
    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            data_input.append(line.strip())
            
    return data_input

    
def lee_entrada_2():
    count = 0
    try:
        while True:
            line = input()
            count = count + 1
            print ('Linea: [{0}]').format(line)
    except EOFError:
        pass
    
    print ('leidas {0} lineas').format(count)
