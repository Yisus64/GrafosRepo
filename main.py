from SRC.practica1 import *
from SRC.practica2 import *

def main():
    grafo = lee_grafo_archivo("test")
    grados = vertice_aislado(grafo)
    print(grados)
    
if __name__ == '__main__':
    main()
