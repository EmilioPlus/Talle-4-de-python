import numpy as np

# 1) Crear un vector con valores dentro del rango 10 a 49

valores = [12,35,40,18,27,45,22,14,41,30]

vector = np.array(valores)

print(vector)

# 2) Invertir el vector

vectorInvertido = np.flip(vector)

# 3) Crear una matriz 3x3 con valores de 0 a 8
filas = 3
columnas= 3
ma = []
elem = 0
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(elem)
        elem += 1
    ma.append(fila)

print(ma)


# 4) Encontrar los indices que no son ceros del arreglo [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]
Array = np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
print(Array)
print(Array[np.where(Array != 0)])

# 5) Crear una matriz identidad de 6x6
filas = 6
columnas= 6
ma = []
elem = 0
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(elem)
        elem += 1
    ma.append(fila)

print(ma)

# 6) Crear una matriz con valores al azar con forma 3x3x3
array = np.random.randint(0, 20, [3, 3, 3])
print(array)


# 7) Encontrar los indices de los valores minimos y maximos de la anterior matriz
max_element = np.max(array) 
min_element = np.min(array) 

print('maximum element in the array is:',  
    max_element) 
print('minimumm element in the array is:', 
    min_element)

# 8) Crear una matriz de 10x10 con 1's en los bordes y 0 en el interior (con rangos de indices)
Matriz = np.zeros((10, 10), dtype=int)
vector = Matriz[::2,1::2]
print(vector)

# 9) Crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4
Ren = np.zeros((5, 5))
Ren += np.arange(0, 5)
print(Ren)

# 10) Crear dos arreglos al azar A y B, verificar si son iguales
a = np.random.randint(0, 2, 4)
print(a)
b = np.random.randint(0, 2, 4)
print(b)

np.allclose(a, b)


''' 11) Escribir un programa que pregunte al usuario por las ventas de un rango de
años y muestre por pantalla un diagrama de líneas con la evolución de las
ventas, genere una gráfica completamente bien detallada con todos los datos'''
#import matplotlib.pyplot as plt

#inicio = int(input('Introduce el año inicial: '))
#fin = int(input('Introduce el año final: '))
#ventas = {}
#for i in range(inicio, fin+1):'''Bucle iterativo para preguntar las ventas de cada año y guardarlas en el diccionario
#i toma como valores los años desde el año de inicio hasta el año final'''
# Preguntamos por las ventas del año i 
#ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
#fig, ax = plt.subplots()
#ax.plot(ventas.keys(), ventas.values())
#plt.show()

# 12) Escribir una función que reciba un diccionario con las notas de las asignaturas...
import matplotlib.pyplot as plt

def Diagram(Notas, Color):
    fig, a = plt.subplots()
    a.bar(Notas.keys(), Notas.values(), Color = Color)
    return a

    Notas = {"Quimica":10, "Astronomia":7, "inteligencia artificial":5, "Mecánica cuántica":2}
    Diagram(Notas, "blue")
    plt.show()






