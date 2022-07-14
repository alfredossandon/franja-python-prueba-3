#Escribir un programa que escriba 20 numeros aleatorios entre 100 y 1000 en un archivo llamado numeros_prueba.txt. 
# Luego debe leer desde el archivo esos números y agregarlos a una lista, 
# modifique o cree una nueva lista que contenga solo los numeros impares. 
# Finalmente con numpy determinar la dimensión de la lista. 
# Imprimir por consola la lista final y su dimensión.

import numpy as np
import random as rd

def imprimir_archivo():
    nombre_fichero = "./numeros_prueba.txt"
    with open(nombre_fichero, 'w', encoding="utf-8") as file:
        for i in range(20):
            numero_aleatorio = rd.randint(100,1000)
            linea = str(numero_aleatorio)

            file.write(linea)
            file.write("\n")
def leer():
    numeros = []
    with open("./numeros_prueba.txt","r") as file:
        for linea in file: 
            numeros.append(int(linea))
    numeros_impar = []
    for x in numeros:
        if x %2 !=0:
            numeros_impar.append(x)
    return numeros_impar
def main():
    imprimir_archivo()
    numeros_impar=leer()
    print(numeros_impar)
    arreglar = np.array(numeros_impar)
    print(arreglar.ndim)

if __name__ == '__main__':
    main()
