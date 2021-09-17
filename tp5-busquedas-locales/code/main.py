import random
import numpy as np
import math
import time
from priorityQueue import *
import csv
import matplotlib.pyplot as plt





class Tablero:
  def __init__(self,n):
    self.tablero = [-1]*n # Este arreglo representará al tablero
    i=0
    while(i < len(self.tablero)):
      col = random.randint(0, n-1)
      if(not(col in self.tablero)):
        self.tablero[i] = col
        i += 1
    valFitnes = 0
    for i in range(0,len(self.tablero)):
      valFitnes += len(self.objectiveFunction([self.tablero[i],i]))
    self.fitnes = valFitnes//2
      




  def objectiveFunction(self,currentPosition):
    directions = ["I","D","ARD","ARI","ABD","ABI"] # No debemos preocuparnos por las columnas, ya que estarán en columnas diferentes
    positions = []
    
    for d in directions:
      if(d == "I"):
        if(currentPosition[1] != 0):
          fila = currentPosition[0]
          columna = currentPosition[1]
          while(columna > 0):
            columna -= 1
            if(self.tablero[columna] == fila):
              if(not([fila,columna] in positions)):
                positions.append([fila,columna])
      
      elif(d == "D"):
        if(currentPosition[1] != len(self.tablero)-1):
          fila = currentPosition[0]
          columna = currentPosition[1]
          while(columna < len(self.tablero)-1):
            columna += 1
            if(self.tablero[columna] == fila):
              if(not([fila,columna] in positions)):
                positions.append([fila,columna])
      
      elif(d == "ARD"):
        if(currentPosition[0] != 0 and currentPosition[1] != len(self.tablero)-1): # Podemos movernos hacia arriba y derecha, en diagonal
          fila = currentPosition[0]
          columna = currentPosition[1]
          while(fila > 0 and columna < len(self.tablero)-1): # Mientras podamos movernos, lo hacemos
            columna += 1
            fila -= 1
            if(self.tablero[columna] == fila): # Encontramos una reina en la diagonal, debemos ver si no visitamos esa posicion antes
              if(not([fila,columna] in positions)):
                positions.append([fila,columna])
  
      elif(d == "ARI"):
        if(currentPosition[0] != 0 and currentPosition[1] != 0): # Podemos movernos hacia arriba e izquierda, en diagonal
          fila = currentPosition[0]
          columna = currentPosition[1]
          while(fila > 0 and columna > 0): # Mientras podamos movernos, lo hacemos
            columna -= 1
            fila -= 1
            if(self.tablero[columna] == fila): # Encontramos una reina en la diagonal, debemos ver si no visitamos esa posicion antes
              if(not([fila,columna] in positions)):
                positions.append([fila,columna])

      elif(d == "ABD"):
        if(currentPosition[0] != len(self.tablero)-1 and currentPosition[1] != len(self.tablero)-1): # Podemos movernos hacia abajo y derecha, en diagonal
          fila = currentPosition[0]
          columna = currentPosition[1]
          while(fila < len(self.tablero)-1 and columna < len(self.tablero)-1): # Mientras podamos movernos, lo hacemos
            columna += 1
            fila += 1
              #print("FILA: " + str(fila) + "\nCOLUMNA: " + str(columna) + "\n")
            if(self.tablero[columna] == fila): # Encontramos una reina en la diagonal, debemos ver si no visitamos esa posicion antes
              if(not([fila,columna] in positions)):
                positions.append([fila,columna])

      elif(d == "ABI"):
        if(currentPosition[0] != len(self.tablero)-1 and currentPosition[1] != 0): # Podemos movernos hacia arriba y derecha, en diagonal
          fila = currentPosition[0]
          columna = currentPosition[1]
          while(fila < len(self.tablero)-1 and columna > 0): # Mientras podamos movernos, lo hacemos
            columna -= 1
            fila += 1
            if(self.tablero[columna] == fila): # Encontramos una reina en la diagonal, debemos ver si no visitamos esa posicion antes
              if(not([fila,columna] in positions)):
                positions.append([fila,columna])
    return positions
    

  def HillClimb(self):
    global statesHC
    for i in range(0,len(self.tablero)):
      incremento = 0
      while(self.tablero[i]-incremento >= 0):
        if(len(self.objectiveFunction([self.tablero[i],i])) > len(self.objectiveFunction([self.tablero[i]-incremento,i]))):
          self.tablero[i] = self.tablero[i]-incremento
          incremento = 0
        incremento += 1
        statesHC += 1
        
      incremento = 0
      while(self.tablero[i]+incremento < len(self.tablero)):
        if(len(self.objectiveFunction([self.tablero[i],i])) > len(self.objectiveFunction([self.tablero[i]+incremento,i]))):
          self.tablero[i] = self.tablero[i]+incremento
          incremento = 0
        incremento += 1
        statesHC += 1
        
  
  

  def SimulatedAnnealing(self):
    global statesSA
    temperature = 100
    self.sch = 0.99

    for i in range(0,len(self.tablero)):
      incremento = 0
      while(self.tablero[i]-incremento >= 0):
        
        currentVal = len(self.objectiveFunction([self.tablero[i],i]))
        nextVal = len(self.objectiveFunction([self.tablero[i]-incremento,i]))
        if(currentVal > nextVal):
          self.tablero[i] = self.tablero[i]-incremento
          incremento = 0
        else:
          cost_diff = nextVal - currentVal
          if(random.uniform(0, 1) < math.exp(-cost_diff * temperature)):
            self.tablero[i] = self.tablero[i]-incremento
        incremento += 1
        statesSA += 1
        
      incremento = 0
      while(self.tablero[i]+incremento < len(self.tablero)):
        currentVal = len(self.objectiveFunction([self.tablero[i],i]))
        nextVal = len(self.objectiveFunction([self.tablero[i]+incremento,i]))
        if(currentVal > nextVal):
          self.tablero[i] = self.tablero[i]+incremento
          incremento = 0
        else:
          cost_diff = nextVal - currentVal
          if(random.uniform(0, 1) < math.exp(-cost_diff * temperature)):
            self.tablero[i] = self.tablero[i]+incremento
        incremento += 1
        statesSA += 1
      temperature *= self.sch
  


  def AG(self):
    global statesAG
    poblacion = generarPoblacion(len(self.tablero),60) # Generamos una poblacion con 60 individuos
    i=0
    while(i < 100): # Habrá 100 generaciones diferentes
      #print("I: " + str(i))
      if(poblacion.items[0].priority == 0):
        break
      seleccionados = seleccion(poblacion)
      reproducidos = reproducir(seleccionados)
      for j in range(0,reproducidos.length()):
        poblacion.enqueue(reproducidos.items[j].tablero,reproducidos.items[j].priority)
      morir(poblacion)
      i += 1
      statesAG += 1
    return poblacion.items[0]
      

def generarPoblacion(size,n): # Debemos generar un conjunto de n individuos (o posibles soluciones) que forman la poblacion inicial
  poblacion = PriorityQueue()
  while(n > 0):
    t = Tablero(size)
    poblacion.enqueue(t.tablero,t.fitnes)
    n -= 1
    #print(poblacion)
  return poblacion
    
    



def seleccion(poblacion):
  seleccionados = PriorityQueue()
  sumFitnes = 0
  for e in poblacion.items:
    sumFitnes += e.priority
  for e in poblacion.items:
    #print(e.priority/sumFitnes)
    if(random.uniform(0, 0.09) > e.priority/sumFitnes):
      seleccionados.enqueue(e.tablero, e.priority)
  return seleccionados
        
    


def reproducir(poblacion):
  nextGeneration = PriorityQueue()
  if(poblacion.length() > 1):
    tab1 = Tablero(len(poblacion.items[0].tablero))
    tab2 = Tablero(len(poblacion.items[0].tablero))
    for i in range(0,len(poblacion.items)-1):
      c=random.randint(1,len(poblacion.items))
      if(poblacion.items[i].priority == 0):# Si el fitnes es 0, ya es solucion, no hace falta reproducir
        nextGeneration.enqueue(poblacion.items[i].tablero,poblacion.items[i].priority)
      else: 
        x1 = poblacion.items[i].tablero[:c]
        #print("X COMPETE: " + str(poblacion.items[i].tablero))
        y1 = poblacion.items[i+1].tablero[c:]
        #print("Y COMPETE: " + str(poblacion.items[i+1].tablero))
        x2 = poblacion.items[i].tablero[c:]
        y2 = poblacion.items[i+1].tablero[:c]
        tab1 = Tablero(len(poblacion.items[i].tablero))
        tab2 = Tablero(len(poblacion.items[i].tablero))
        tab1.tablero = x1+y1
        
        val1 = 0
        for i in range(0,len(tab1.tablero)):
          val1 += len(tab1.objectiveFunction([tab1.tablero[i],i]))
        tab1.fitnes = val1//2

        tab2.tablero = x2+y2

        val1 = 0
        for i in range(0,len(tab2.tablero)):
          val1 += len(tab2.objectiveFunction([tab2.tablero[i],i]))
        tab2.fitnes = val1//2

        if(random.randint(0, 100) < 3): # Agregamos una probable mutacion
          tab1.tablero[random.randint(0, len(tab1.tablero)-1)] = random.randint(0, len(tab1.tablero)-1)
          tab1.tablero[random.randint(0, len(tab1.tablero)-1)] = random.randint(0, len(tab1.tablero)-1)
        
      valFitnes1 = 0
      valFitnes2 = 0
      for i in range(0,len(tab1.tablero)):
        valFitnes1 += len(tab1.objectiveFunction([tab1.tablero[i],i]))
        valFitnes2 += len(tab2.objectiveFunction([tab2.tablero[i],i]))
      tab1.fitnes = valFitnes1//2
      tab2.fitnes = valFitnes2//2
      nextGeneration.enqueue(tab1.tablero,tab1.fitnes)
      nextGeneration.enqueue(tab2.tablero,tab2.fitnes)
  return nextGeneration




def morir(poblacion):
  vueltas = int(70*len(poblacion.items)/100)
  for i in range(0,vueltas): # Mataremos al 70% de la poblacion menos buena
    #print(poblacion.items)
    #print(poblacion.items[len(poblacion.items)-1])
    poblacion.items.remove(poblacion.items[len(poblacion.items)-1])
  #poblacion.printQueue()





    
      

  
def graphics(tablero):
  for i in range(len(tablero)):
    for j in range(0,len(tablero)):
      if(j == len(tablero)-1):
        if(i == tablero[j]):
          print(" R ]")
        else:
          print(" . ]")
      elif(j == 0):
        if(i == tablero[j]):
          print("[ R", end="")
        else:
          print("[ .", end="")
      else:
        if(i == tablero[j]):
          print(" R", end="")
        else:
          print(" .", end="")


timesHC = []
timesSA = []
timesAG = []

globalOptimizacionHillClimb = 0
globalOptimizacionSimulatedAnnealing = 0
globalOptimizacionAG = 0

size = [4,8,10,12,15]

statesAG = 0
statesHC = 0
statesSA = 0

i = 0
n = 0
print("HILL CLIMB \n")
inicio = time.time()
while(i < 1000 and n < 5):
  t = Tablero(size[n])
  t.HillClimb()
  lista = []
  for j in t.tablero:
    if(len(t.objectiveFunction([t.tablero[j],j])) == 0):
      lista.append([t.tablero[j],j]) # Vamos concatenando las posiciones que no están en peligro
    else:
      break
  
  if(len(lista) == size[n]): # Si tiene la misma cantidad de elementos como tamaño del tablero, ganamos
    final = time.time()
    timesHC.append(final-inicio)
    print("GLOBAL OPTIMIZATION (HC): ", end="")
    print(t.tablero)

  if(i%200 == 0):
    n += 1
  i += 1
print(timesHC)

print("PORCENTAJE DE SOLUCIÓN HC: " + str(len(timesHC)*0.1) + "%")

if(len(timesHC) > 0):
  desviacionHC = np.std(timesHC)
  mediaHC = np.mean(timesHC)
else:
  mediaHC = 0
  desviacionHC = 0

print("MEDIA DE TIEMPOS DE EJECUCIÓN HC: " + str(mediaHC))
print("DESVIACIÓN ESTANDAR DE LOS TIEMPOS DE EJECUCIÓN HC: " + str(desviacionHC))
print("ESTADOS VISITADOS : " + str(statesHC))




i = 0
n = 0
print("\n\nSIMULATED ANNEALNG\n")
inicio = time.time()
while(i < 1000 and n < 5):
  t = Tablero(size[n])
  t.SimulatedAnnealing()
  lista = []
  for j in t.tablero:
    resPosition = t.objectiveFunction([t.tablero[j],j])
    if(len(t.objectiveFunction([t.tablero[j],j])) == 0):
      lista.append([t.tablero[j],j])
    else:
      break
 
  if(len(lista) == size[n]):
    final = time.time()
    timesSA.append(final-inicio)
    print("GLOBAL OPTIMIZATION (SA): ", end="")
    print(t.tablero)

  if(i%200 == 0):
    n += 1
  i += 1


print(timesSA)

print("PORCENTAJE DE SOLUCIÓN SA: " + str(len(timesSA)*0.1) + "%")

if(len(timesSA) > 0):
  desviacionSA = np.std(timesSA)
  mediaSA = np.mean(timesSA)
else:
  mediaSA = 0
  desviacionSA = 0
print("MEDIA DE TIEMPOS DE EJECUCIÓN SA: " + str(mediaSA))
print("DESVIACIÓN ESTANDAR DE LOS TIEMPOS DE EJECUCIÓN SA: " + str(desviacionSA))
print("ESTADOS VISITADOS : " + str(statesSA))







## ALGORITMO GENETICO
timesAG = []
i = 0
n = 0
print("\n\nALGORITMOS GENÉTICOS\n")
inicio = time.time()
while(i < 1000 and n < 5):
  t = Tablero(size[n])
  resultado = t.AG()

  if(resultado.priority == 0):
    final = time.time()
    timesAG.append(final-inicio)
    print("GLOBAL OPTIMIZATION (AG): ", end="")
    print(resultado.tablero)
  
    
  if(i%200 == 0):
    n += 1
  i += 1


print(timesAG)
print("PORCENTAJE DE SOLUCIÓN AG: " + str(len(timesAG)*0.1) + "%")
if(len(timesAG) > 0):
  mediaAG = np.mean(timesAG)
  desviacionAG = np.std(timesAG)
else:
  mediaAG = 0
  desviacionAG = 0

print("MEDIA DE TIEMPOS DE EJECUCIÓN AG: " + str(mediaAG))
print("DESVIACIÓN ESTANDAR DE LOS TIEMPOS DE EJECUCIÓN AG: " + str(desviacionAG))
print("ESTADOS VISITADOS : " + str(statesAG))

file = open("datos.csv", "w", newline='')
spamreader = csv.writer(file)
spamreader.writerow(["Hill Climb"])
spamreader.writerow(timesHC)
spamreader.writerow(["PORCENTAJE DE SOLUCIÓN: " + str(len(timesHC)*0.1)])
spamreader.writerow(["MEDIA DE LOS TIEMPOS DE EJECUCIÓN: " + str(mediaHC)])
spamreader.writerow(["DESVIACIÓN ESTÁNDAR: " + str(desviacionHC)])
spamreader.writerow(["ESTADOS VISITADOS: " + str(statesHC)])
spamreader.writerow([])
spamreader.writerow(["\n"])
spamreader.writerow(["Simulated Annealing"])
spamreader.writerow(timesSA)
spamreader.writerow(["PORCENTAJE DE SOLUCIÓN: " + str(len(timesSA)*0.1)])
spamreader.writerow(["MEDIA DE LOS TIEMPOS DE EJECUCIÓN: " + str(mediaSA)])
spamreader.writerow(["DESVIACIÓN ESTÁNDAR: " + str(desviacionSA)])
spamreader.writerow(["ESTADOS VISITADOS: " + str(statesSA)])
spamreader.writerow(["\n"])
spamreader.writerow(["Genetic Algorithms"])
spamreader.writerow(timesAG)
spamreader.writerow(["PORCENTAJE DE SOLUCIÓN: " + str(len(timesAG)*0.1)])
spamreader.writerow(["MEDIA DE LOS TIEMPOS DE EJECUCIÓN: " + str(mediaAG)])
spamreader.writerow(["DESVIACIÓN ESTÁNDAR: " + str(desviacionAG)])
spamreader.writerow(["ESTADOS VISITADOS: " + str(statesAG)])
spamreader.writerow(["\n"])

file.close()
if(len(timesHC) > 0):
  plt.boxplot(timesHC)
  plt.title("BOXPLOT HILL CLIMB")
  plt.show()
if(len(timesSA) > 0):
  plt.boxplot(timesSA)
  plt.title("BOXPLOT SIMULATED ANNEALING")
  plt.show()
if(len(timesAG) > 0):
  plt.title("BOXPLOT GENETIC ALGORITHM")
  plt.boxplot(timesAG)
  plt.show()
