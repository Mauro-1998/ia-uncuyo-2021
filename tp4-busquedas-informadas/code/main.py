import numpy as np
import random
from queue import Queue
from stack import Stack
from priorityQueue import PriorityQueue
import math
import threading
import matplotlib.pyplot as plt



class Node:
  row = None
  col = None
  parent = None
  priority = None

class Environment:
  def __init__(self,sizeX,sizeY):
    self.initPosX = random.randint(0,sizeX-1)
    self.initPosY = random.randint(0,sizeY-1)
    self.destX = random.randint(0,sizeX-1)
    self.destY = random.randint(0,sizeY-1)
    while(self.destX == self.initPosX and self.destY == self.initPosY):
      self.destX = random.randint(0,sizeX-1)
      self.destY = random.randint(0,sizeY-1)

    self.map = np.zeros((sizeX, sizeY))
    obstaculos = random.randint(0,sizeY*sizeX)
    while(obstaculos > 0):
      obsX = random.randint(0,sizeX-1)
      obsY = random.randint(0,sizeY-1)
      if(self.map[obsX][obsY] == 0):
        self.map[obsX][obsY] = 1
        obstaculos -= 1


  
  def accept_action(self,action,position):
    dim = np.shape(self.map)
    fila = dim[0]-1
    columna = dim[1]-1
    if(action == "R"): 
      if(position[1]+1 > columna): # Estamos en el limite derecho del mapa y nos queremos mover a la derecha
        return False
      else:
        if(self.map[position[0]][position[1]+1] == 1):
          return False
        else:
          return True
    elif(action == "L"): 
      if(position[1]-1 < 0): # Estamos en el limite izquierdo del mapa y nos queremos mover a la izquierda
        return False
      else:
        if(self.map[position[0]][position[1]-1] == 1):
          return False
        else:
          return True
    elif(action == "U"): 
      if(position[0]-1 < 0): # Estamos en el limite superior del mapa y nos queremos mover hacia arriba
        return False
      else:
        if(self.map[position[0]-1][position[1]] == 1):
          return False
        else:
          return True  
    elif(action == "D"): # Estamos en el limite inferior del mapa y nos queremos mover hacia abajo
      if(position[0]+1 > fila):
        return False
      else:
        if(self.map[position[0]+1][position[1]] == 1):
          return False
        else:
          return True


    
   
  # Mostramos el mapa con los lugares limpios (0), los lugares sucios (1)
  def print_environment(self):
    print("\n")
    for i in range(0,len(self.map)):
      print(self.map[i])

class Agent:
  def __init__(self,environment):
    self.fila = environment.initPosX
    self.columna = environment.initPosY
    self.env = environment
    self.env.map[self.fila][self.columna] = 2
    self.env.map[self.env.destX][self.env.destY] = 2
    self.movements = 0


  def calculateHeuristic(self,row,col): # Calculamos la heurística en base a la cantidad de movimientos, yendo en rectas hasta llegar al destino, sin importar si hay un obstaculo entre medio
    initPos = [row,col]
    finishPos = [self.env.destX,self.env.destY]
    movements = 0
    while(initPos != finishPos):
      if(initPos[0] < finishPos[0]):
        initPos[0] += 1
        movements += 1
      elif(initPos[0] > finishPos[0]):
        initPos[0] -= 1
        movements += 1
      elif(initPos[1] < finishPos[1]):
        initPos[1] += 1
        movements += 1
      elif(initPos[1] > finishPos[1]):
        initPos[1] -= 1
        movements += 1

    return movements





  def A_estrella(self):
    origen = str(self.fila)+","+str(self.columna)
    adyacentes = PriorityQueue()
    visitados = {}
    first = Node()
    first.row = self.fila
    first.col = self.columna
    visitados[origen] = first
    adyacentes.enqueue(self.fila,self.columna,0,None)
    find = False

    while(adyacentes.length() > 0):
      elemento = adyacentes.dequeue()
      move = ["U","D","R","L"]
      for e in move:
        if(e == "U" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row-1)+","+str(elemento.col)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row-1,elemento.col,self.calculateHeuristic(elemento.row-1,elemento.col)+1,elemento)
            if(self.env.map[elemento.row-1][elemento.col] == 2):
              find = True
              break

        if(e == "D" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row+1)+","+str(elemento.col)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row+1,elemento.col,self.calculateHeuristic(elemento.row+1,elemento.col)+1,elemento)

            if(self.env.map[elemento.row+1][elemento.col] == 2):
              find = True
              break

        if(e == "R" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row)+","+str(elemento.col+1)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row,elemento.col+1,self.calculateHeuristic(elemento.row,elemento.col+1)+1,elemento)
            if(self.env.map[elemento.row][elemento.col+1] == 2):
              find = True
              break
                
        if(e == "L" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row)+","+str(elemento.col-1)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row,elemento.col-1,self.calculateHeuristic(elemento.row,elemento.col-1)+1,elemento)
            if(self.env.map[elemento.row][elemento.col-1] == 2):
              find = True
              break
      element = str(elemento.row)+","+str(elemento.col)
      visitados[element] = elemento


    
    if(find):
      path = []
      elemento = str(self.env.destX)+","+str(self.env.destY)
      last = visitados[elemento]
      init = str(self.env.initPosX)+str(self.env.initPosY)
      while(last.parent != None):
        path.append(str(last.row) + str(last.col))
        last = last.parent
      path.append(init)
      return path
    else:
      return None
    
  


datosA_estrella = [0]*30
mediaA_estrella = 0
for i in range(0,30):
  entorno = Environment(100,100)
  agente = Agent(entorno)
  respuesta = agente.A_estrella()
  if(respuesta != None):
    datosA_estrella[i] = len(respuesta)

print(datosA_estrella)

mediaA_estrella = np.mean(datosA_estrella)
print("MEDIA A*: " + str(mediaA_estrella))
desviacionA_estrella = np.std(datosA_estrella)
print("Desviacion Estandar A*: " + str(desviacionA_estrella))


estadosA_estrella = 0
for i in range(0,30):
  estadosA_estrella += datosA_estrella[i]
  

## Declaramos valores para el eje x
eje_x = ['Media', 'Desviación Estándar', 'Estados Explorados']
## Declaramos valores para el eje y
eje_y = [mediaA_estrella,desviacionA_estrella,estadosA_estrella]
## Creamos Gráfica
plt.bar(eje_x, eje_y)
## Título de Gráfica
plt.title('Agloritmo A*')
## Mostramos Gráfica
plt.show()



