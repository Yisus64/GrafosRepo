from SRC.practica1 import *
from SRC.practica2 import *

def main():
    grafo = lee_grafo_archivo("test")
    componentes = componentes_conexas(grafo)
    print(componentes)
    print(es_conexo(grafo))
    
if __name__ == '__main__':
    main()
