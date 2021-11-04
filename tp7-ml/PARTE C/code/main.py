from id3 import ID3
import numpy as np
import csv


datos = np.genfromtxt('tennis.csv', delimiter=",", dtype="str")
test = np.genfromtxt('test.csv', delimiter=",", dtype="str")

X = datos[:, :-1]
Y = datos[:, -1]

test = test[:,:-1]

print(test)

print(X)
print("\n")
print(Y)


arbol = ID3()
arbol.entrenar(X,Y)
salida = arbol.predecir(test)
salida = np.insert(salida,0,"play")
print(salida)

print('Porcentaje de aciertos: ', 100 * sum(Y == salida)/X.shape[0])
#print(calculateEntropy(dataset))