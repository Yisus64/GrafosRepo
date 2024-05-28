from SRC.practica1 import *
from SRC.practica2 import *
from SRC.practica3 import *
def main():
    grafo = lee_grafo_archivo("test")
    print(valida_nodo_en_grafo(grafo, 'E'))
    
if __name__ == '__main__':
    main()
