from SRC.practica1 import *
from SRC.practica2 import *
from SRC.practica3 import *


def main():
    grafo = lee_grafo_archivo("testciclo")
    print(encuentra_ciclo(grafo, 'A'))


if __name__ == '__main__':
    main()
