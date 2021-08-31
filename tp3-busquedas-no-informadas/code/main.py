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



  def BFS(self,i):
    origen = str(self.fila)+","+str(self.columna)
    adyacentes = Queue()
    visitados = {}
    first = Node()
    first.row = self.fila
    first.col = self.columna
    visitados[origen] = first
    adyacentes.enqueue(self.fila,self.columna,None)
    find = False

    while(adyacentes.length() > 0):
      elemento = adyacentes.dequeue()
      move = ["U","D","R","L"]
      for e in move:
        if(e == "U" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row-1)+","+str(elemento.col)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row-1,elemento.col,elemento)
            if(self.env.map[elemento.row-1][elemento.col] == 2):
              find = True
              break
          

        if(e == "D" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row+1)+","+str(elemento.col)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row+1,elemento.col,elemento)
            if(self.env.map[elemento.row+1][elemento.col] == 2):
              find = True
              break

        if(e == "R" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row)+","+str(elemento.col+1)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row,elemento.col+1,elemento)
            if(self.env.map[elemento.row][elemento.col+1] == 2):
              find = True
              break

                
        if(e == "L" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row)+","+str(elemento.col-1)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row,elemento.col-1,elemento)
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
      datosBFS[i] = len(path)
      return
    else:
      return None
    
  


  def DFS(self,i):

    origen = str(self.fila)+","+str(self.columna)
    adyacentes = Stack()
    visitados = {}
    first = Node()
    first.row = self.fila
    first.col = self.columna
    visitados[origen] = first
    adyacentes.push(self.fila,self.columna,None)
    find = False

    while(adyacentes.length() > 0):
      elemento = adyacentes.pop()
      move = ["U","D","R","L"]
      for e in move:
        if(e == "U" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row-1)+","+str(elemento.col)
          if(visitados.get(next, None) == None):
            adyacentes.push(elemento.row-1,elemento.col,elemento)
            if(self.env.map[elemento.row-1][elemento.col] == 2):
              find = True
              break
          
        if(e == "D" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row+1)+","+str(elemento.col)
          if(visitados.get(next, None) == None):
            adyacentes.push(elemento.row+1,elemento.col,elemento)
            if(self.env.map[elemento.row+1][elemento.col] == 2):
              find = True
              break

        if(e == "R" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row)+","+str(elemento.col+1)
          if(visitados.get(next, None) == None):
            adyacentes.push(elemento.row,elemento.col+1,elemento)
            if(self.env.map[elemento.row][elemento.col+1] == 2):
              find = True
              break

        if(e == "L" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row)+","+str(elemento.col-1)
          if(visitados.get(next, None) == None):
            adyacentes.push(elemento.row,elemento.col-1,elemento)
            if(self.env.map[elemento.row][elemento.col-1] == 2):
              find = True
              break
      #adyacentes.printStack()
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
      datosDFS[i] = len(path)
      return
    else:
      return None
    
  
  



  def UniformSearch(self,i):
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
            adyacentes.enqueue(elemento.row-1,elemento.col,elemento.priority+1,elemento)
            if(self.env.map[elemento.row-1][elemento.col] == 2):
              find = True
              break

        if(e == "D" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row+1)+","+str(elemento.col)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row+1,elemento.col,elemento.priority+1,elemento)
            if(self.env.map[elemento.row+1][elemento.col] == 2):
              find = True
              break

        if(e == "R" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row)+","+str(elemento.col+1)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row,elemento.col+1,elemento.priority+1,elemento)
            if(self.env.map[elemento.row][elemento.col+1] == 2):
              find = True
              break
                
        if(e == "L" and self.env.accept_action(e,[elemento.row, elemento.col])):
          next = str(elemento.row)+","+str(elemento.col-1)
          if(visitados.get(next, None) == None):
            adyacentes.enqueue(elemento.row,elemento.col-1,elemento.priority+1,elemento)
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
      datosUS[i] = len(path)
      return
    else:
      return None
  



global datosBFS
global datosDFS
global datosUS

datosBFS = [0]*30
datosDFS = [0]*30
datosUS = [0]*30


print("Creando los objetos e hilos necesarios...")
for i in range(0,30):
  entorno = Environment(100,100)
  agente = Agent(entorno)
   
  threadBFS = threading.Thread(target=agente.BFS(i))
  threadBFS.start()
  threadDFS = threading.Thread(target=agente.DFS(i))
  threadDFS.start()
  threadUS = threading.Thread(target=agente.UniformSearch(i))
  threadUS.start()
  
  threadBFS.join()
  threadDFS.join()
  threadUS.join()



print("BFS: " + str(datosBFS))
print("DFS: " + str(datosDFS))
print("US: " + str(datosUS))




mediaBFS = 0
mediaDFS = 0
mediaUS = 0
for i in range(0,30):
  mediaBFS += datosBFS[i] 
  mediaDFS += datosDFS[i] 
  mediaUS += datosUS[i]
#print("MEDIA BFS SIN DIVIDIR: " + str(mediaBFS))
estadosBFS = mediaBFS
estadosDFS = mediaDFS
estadosUS = mediaUS
mediaBFS /= len(datosBFS)
mediaDFS /= len(datosDFS)
mediaUS /= len(datosUS)

print("Media BFS: " + str(mediaBFS))
print("Media DFS: " + str(mediaDFS))
print("Media UniformSearch: " + str(mediaUS))
print("\n")

distBFS = 0
distDFS = 0
distUniformSearch = 0
for i in range(0,len(datosBFS)):
  distBFS += abs((datosBFS[i] - mediaBFS)**2)
  distDFS += abs((datosDFS[i] - mediaDFS)**2)
  distUniformSearch += abs((datosUS[i] - mediaUS)**2)

  
print("Desviación Típica BFS: " + str(math.sqrt(distBFS/len(datosBFS))))
print("Desviación Típica DFS: " + str(math.sqrt(distDFS/len(datosDFS))))
print("Desviación Típica Uniform Search: " + str(math.sqrt(distUniformSearch/len(datosUS))))
print("\n")


 
## Declaramos valores para el eje x
eje_x = ['Media', 'Desviación Estándar', 'Estados Explorados']
## Declaramos valores para el eje y
eje_y = [mediaBFS,math.sqrt(distBFS/len(datosBFS)),estadosBFS]
## Creamos Gráfica
plt.bar(eje_x, eje_y)
## Título de Gráfica
plt.title('Agloritmo BFS')
## Mostramos Gráfica
plt.show()


## Declaramos valores para el eje x
eje_x = ['Media', 'Desviación Estándar', 'Estados Explorados']
## Declaramos valores para el eje y
eje_y = [mediaDFS,math.sqrt(distDFS/len(datosDFS)),estadosDFS]
## Creamos Gráfica
plt.bar(eje_x, eje_y) 
## Título de Gráfica
plt.title('Agloritmo DFS')
## Mostramos Gráfica
plt.show()


## Declaramos valores para el eje x
eje_x = ['Media', 'Desviación Estándar', 'Estados Explorados']
## Declaramos valores para el eje y
eje_y = [mediaUS,math.sqrt(distUniformSearch/len(datosUS)),estadosUS]
## Creamos Gráfica
plt.bar(eje_x, eje_y) 
## Título de Gráfica
plt.title('Agloritmo Uniform Search')
## Mostramos Gráfica
plt.show()


