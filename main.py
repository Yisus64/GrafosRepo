from SRC.practica1 import *
from SRC.practica2 import *
from SRC.practica3 import *
def main():
    grafo = lee_grafo_archivo("test")
    print(encuentra_camino_abierto(grafo, 'A', 'D'))
    
if __name__ == '__main__':
    main()
