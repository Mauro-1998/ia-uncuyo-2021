import numpy as np
import random


class AgentAleatory:
  def __init__(self,env):
    self.env = env
    self.current_posX = env.init_posX
    self.current_posY = env.init_posY
    self.movements = 1000
    self.cleaned = 0

  def __init__(self,env):
    self.env = env
    self.current_posX = env.init_posX
    self.current_posY = env.init_posY
    self.movements = 1000
    self.cleaned = 0
  
  def clean(self):
    actions = ["R","L","U","D","C","N"]
    if(self.env.dirt_boxes > 0):
      while(self.movements > 0 and self.cleaned/self.env.dirt_boxes < 1):
        mov = actions[random.randint(0,len(actions)-1)]
        if(self.env.accept_action(mov,[self.current_posX,self.current_posY])):
          if(mov == "R"):
            self.current_posX += 1
          elif(mov == "L"):
            self.current_posX -= 1
          elif(mov == "U"):
            self.current_posY -= 1
          elif(mov == "D"):
            self.current_posY += 1
          elif(mov == "C"):
            if(self.env.map[self.current_posX][self.current_posY] == 1):
              self.cleaned += 1
            self.env.map[self.current_posX][self.current_posY] = 0
          self.movements -= 1
  
  def getPerformance(self):
    if(self.env.dirt_boxes > 0):
      return self.cleaned/self.env.dirt_boxes
    else:
      return 0





class Agent:
  def __init__(self,env):
    self.env = env
    self.current_posX = env.init_posX
    self.current_posY = env.init_posY
    self.movements = 1000
    self.cleaned = 0
    #env.map[self.current_posX][self.current_posY] = 2
    #env.print_environment()


  def returnInitPosition(self):
    #print("VOLVEMOS A LA POSICION INICIAL")
    #print("POS X: " + str(self.env.init_posX))
    #print("POS Y: " + str(self.env.init_posY))
    #self.env.print_environment()
    #input("")
    o = self.current_posY
    i = self.current_posX

    #self.env.map[o][i] = 0


    while(self.env.init_posX < self.current_posX and self.movements > 0):
      self.env.map[self.current_posX][self.current_posY] = 0
      self.current_posX -= 1
      if(self.env.map[self.current_posX][self.current_posY] == 1): # Quizas encontramos una casilla sucia en el trayecto de vuelta a la posicion inicial
        self.cleaned += 1
        self.movements -= 1
      self.env.map[self.current_posX][self.current_posY] = 2
      #self.env.print_environment()
      self.movements -= 1
      
    while(self.env.init_posX > self.current_posX and self.movements > 0):
      self.env.map[self.current_posX][self.current_posY] = 0
      self.current_posX += 1
      if(self.env.map[self.current_posX][self.current_posY] == 1): # Quizas encontramos una casilla sucia en el trayecto de vuelta a la posicion inicial
        self.cleaned += 1
        self.movements -= 1
      self.env.map[self.current_posX][self.current_posY] = 2
      #self.env.print_environment()
      self.movements -= 1

    while(self.env.init_posY < self.current_posY and self.movements > 0):
      self.env.map[self.current_posX][self.current_posY] = 0
      self.current_posY -= 1
      if(self.env.map[self.current_posX][self.current_posY] == 1): # Quizas encontramos una casilla sucia en el trayecto de vuelta a la posicion inicial
        self.cleaned += 1
        self.movements -= 1
      self.env.map[self.current_posX][self.current_posY] = 2
      #self.env.print_environment()
      self.movements -= 1

    while(self.env.init_posY > self.current_posY and self.movements > 0):
      self.env.map[self.current_posX][self.current_posY] = 0
      self.current_posY += 1
      if(self.env.map[self.current_posX][self.current_posY] == 1): # Quizas encontramos una casilla sucia en el trayecto de vuelta a la posicion inicial
        self.cleaned += 1
        self.movements -= 1
      self.env.map[self.current_posX][self.current_posY] = 2
      #self.env.print_environment()
      self.movements -= 1
    
    
          
  def think(self):
    # Vamos a determinar para donde comviene encarar (segun la probabilidad y la posición actual del agente)
    # El movimiento será siempre lineal iterando las filas y por cada una, las columnas, recorriendo la matriz, vamos a determinar si nos conviene ir hacia arriba o hacia abajo y si nos conviene ir de izquierda a derecha o viceversa
    # Para ello obtenemos las dimensiones del mapa
    dim = np.shape(self.env.map)
    dim = [dim[0]-1,dim[1]-1]
    countR = len(self.env.map[self.current_posY])-1 - self.current_posY
    countL = dim[1]-countR
    #print("CURRENT POSITION: (" + str(self.current_posX) + "," + str(self.current_posY) + ")")
    if(countL >= countR): # Nos conviene recorrer de derecha a izquierda, ya que hay más casillas de ese lado, por ende, hay mas probabilidad de encontrar casillas sucias
      countD = dim[1]-self.current_posX
      countU = dim[1]-countD 
      if(countD >= countU): # Nos conviene recorrer de derecha a izquierda y de arriba hacia abajo
        return "LD"
      else:
        return "LU"
    else: # Nos conviene recorrer de izquierda a derecha
      countD = dim[1]-self.current_posX
      countU = dim[1]-countD 
      if(countD >= countU): # Nos conviene recorrer de izquierda a derecha y de arriba hacia abajo
        return "RD"
      else:
        return "RU"
  
  
  
  def clean(self):
    directions = self.think()
    #self.env.print_environment()
    #print("Directions: " + str(directions))
    #input("")
    complete = False
    dim = np.shape(self.env.map)
    if(self.env.dirt_boxes == 0):
      return
    else:  
      while(self.movements > 0 and self.cleaned/self.env.dirt_boxes < 1):
        #print(self.cleaned/self.env.dirt_boxes)
        if(directions == "RD"):
          self.RD()
          #print("LIMPIADOS: " + str(self.cleaned))
          #print("Porcentaje: " + str(self.cleaned/self.env.dirt_boxes))
          if(self.cleaned/self.env.dirt_boxes < 1): # No terminamos de limpiar todo el mapa 
            self.returnInitPosition()
            if(self.cleaned/self.env.dirt_boxes < 1): # Como aún hay partes del mapa que están sucias, debemos hacer la dirección contraria a la que fuimos
              self.LU()
            #self.env.print_environment()
            
            
            #break
        elif(directions == "RU"):
          self.RU()
          if(self.cleaned/self.env.dirt_boxes < 1): # No terminamos de limpiar todo el mapa 
            self.returnInitPosition()
            if(self.cleaned/self.env.dirt_boxes < 1): # Como aún hay partes del mapa que están sucias, debemos hacer la dirección contraria a la que fuimos
              self.LD()


            #self.env.print_environment()
            
        elif(directions == "LD"):
          self.LD()
          if(self.cleaned/self.env.dirt_boxes < 1): # No terminamos de limpiar todo el mapa 
            self.returnInitPosition()
            if(self.cleaned/self.env.dirt_boxes < 1): # Como aún hay partes del mapa que están sucias, debemos hacer la dirección contraria a la que fuimos
              self.RU()

            
        elif(directions == "LU"):
          self.LU()
          if(self.cleaned/self.env.dirt_boxes < 1): # No terminamos de limpiar todo el mapa 
            self.returnInitPosition()
            if(self.cleaned/self.env.dirt_boxes < 1):
              # Como aún hay partes del mapa que están sucias, debemos hacer la dirección contraria a la que fuimos
              self.RD()
            #self.env.print_environment()

        
        
      #print("Porcentaje de Limpieza: " + str((self.cleaned/self.env.dirt_boxes)*100))
      #self.env.print_environment()

  
  def RD(self):
    visits = []
    dim = np.shape(self.env.map)
    o = self.current_posY # Selecciona la columna
    i = self.current_posX # Selecciona la fila
    direction = "R"
    if(self.current_posY%2 == 0):
      cant_vueltas = dim[0]
    else:
      cant_vueltas = dim[0]-1
    while(i < cant_vueltas and self.movements > 0):
      while(direction == "R" and self.movements > 0): # Mientras nos podamos mover a la derecha, lo hacemos
        #self.env.print_environment()
        if(self.cleaned/self.env.dirt_boxes == 1):
          i = cant_vueltas
          break
        else:
          if(i == dim[0]-1 and o == dim[0]-1) or (i == dim[0]-1 and o == 0): # Llegamos a una esquina inferior
            if not([i,o]) in visits: # La esquina no fue previamente visitada
              visits.append([i,o])
            if(len(visits) == 2): # Visitamos ambas esquinas pero no completamos la limpieza
              i = cant_vueltas
              break
        self.env.map[i][o] = 0
        if(o == dim[1]-1): # Llegamos al limite lateral derecho, debemos volver hacia la izquierda
          i += 1
          o -= 1
          direction = "L"
        o += 1
        self.current_posX = i
        self.current_posY = o
        #self.env.map[i][o] = 2
        if(self.env.map[i][o] == 0): # Podemos movernos a la proxima casilla sin ningun problema
          #print("Entra")
          self.env.map[i][o] = 2
        else:
          self.cleaned += 1
          self.env.map[i][o] = 2
          self.movements -= 1
        self.movements -= 1
      while(direction == "L" and self.movements > 0):
        #self.env.print_environment()
        if(self.cleaned/self.env.dirt_boxes == 1):
          i = cant_vueltas
          break
        else:
          if(i == dim[0]-1 and o == dim[0]-1) or (i == dim[0]-1 and o == 0): # LLegamos a una esquina inferior
            if not([i,o]) in visits: # La esquina no fue previamente visitada
              visits.append([i,o])
            if(len(visits) == 2): # Visitamos ambas esquinas
              i = cant_vueltas
              break
        self.env.map[i][o] = 0
        if(o == 0): # LLegamos al limite lateral izquierdo, debemos volver hacia la izquierda
          i += 1
          o += 1
          direction = "R"
        o -= 1
        self.current_posX = i
        self.current_posY = o
        if(self.env.map[i][o] == 0): # Podemos movernos a la proxima casilla sin ningun problema
          #print("Entra")
          self.env.map[i][o] = 2
        else:
          self.cleaned += 1
          self.env.map[i][o] = 2
          self.movements -= 1
        self.movements -= 1

 
  def RU(self):
    visits = []
    dim = np.shape(self.env.map)
    o = self.current_posY # Selecciona la columna
    i = self.current_posX # Selecciona la fila
    direction = "R"
    if(self.current_posY%2 == 0):
      cant_vueltas = dim[0]
    else:
      cant_vueltas = dim[0]-1
    while(i <= cant_vueltas and self.movements > 0):
      while(direction == "R" and self.movements > 0): # Mientras nos podamos mover a la derecha, lo hacemos
        #self.env.print_environment()
        if(self.cleaned/self.env.dirt_boxes == 1):  # Cumplimos con el grado de aceptación de la limpieza
          i = cant_vueltas+1
          break
        else:
          if(i == 0 and o == dim[1]-1) or (i == 0 and o == 0): # Llegamos a una esquina superior
            if not([i,o]) in visits: # La esquina no fue previamente visitada
              visits.append([i,o])
            if(len(visits) == 2): # Visitamos ambas esquinas pero no completamos la limpieza
              i = cant_vueltas+1
              break
        self.env.map[i][o] = 0
        if(o == dim[1]-1): # Llegamos al limite lateral derecho, debemos volver hacia la izquierda
          i -= 1
          o -= 1
          self.movements -= 2
          direction = "L"
        o += 1
        self.current_posX = i
        self.current_posY = o
        #self.env.map[i][o] = 2
        if(self.env.map[i][o] == 0): # Podemos movernos a la proxima casilla sin ningun problema
          #print("Entra")
          self.env.map[i][o] = 2
        else:
          self.cleaned += 1
          self.env.map[i][o] = 2
          self.movements -= 1
        self.movements -= 1
      while(direction == "L" and self.movements > 0):
        #self.env.print_environment()
        if(self.cleaned/self.env.dirt_boxes == 1):  # Cumplimos con el grado de aceptación de la limpieza
          i = cant_vueltas+1
          break
        else:
          if(i == dim[0]-1 and o == dim[0]-1) or (i == dim[0]-1 and o == 0): # LLegamos a una esquina inferior
            if not([i,o]) in visits: # La esquina no fue previamente visitada
              visits.append([i,o])
            if(len(visits) == 2): # Visitamos ambas esquinas
              i = cant_vueltas+1
              break
        self.env.map[i][o] = 0
        if(o == 0): # LLegamos al limite lateral izquierdo, debemos volver hacia la izquierda
          i -= 1
          o += 1
          self.movements -= 2
          direction = "R"
        o -= 1
        self.current_posX = i
        self.current_posY = o
        if(self.env.map[i][o] == 0): # Podemos movernos a la proxima casilla sin ningun problema
          #print("Entra")
          self.env.map[i][o] = 2
        else:
          self.cleaned += 1
          self.env.map[i][o] = 2
          self.movements -= 1
        self.movements -= 1
  
  
  def LU(self):
    visits = []
    dim = np.shape(self.env.map)
    o = self.current_posY # Selecciona la columna
    i = self.current_posX # Selecciona la fila
    direction = "L"
    if(self.current_posY%2 == 0):
      cant_vueltas = dim[0]
    else:
      cant_vueltas = dim[0]-1
    while(i <= cant_vueltas and self.movements > 0):
      while(direction == "R" and self.movements > 0): # Mientras nos podamos mover a la derecha, lo hacemos
        #self.env.print_environment()
        if(self.cleaned/self.env.dirt_boxes == 1): # Cumplimos con el grado de aceptación de la limpieza
          i = cant_vueltas + 1
          break
        else:
          if(i == 0 and o == dim[1]-1) or (i == 0 and o == 0): # Llegamos a una esquina superior
            if not([i,o]) in visits: # La esquina no fue previamente visitada
              visits.append([i,o])
            if(len(visits) == 2): # Visitamos ambas esquinas pero no completamos la limpieza
              i = cant_vueltas + 1
              break
        self.env.map[i][o] = 0
        if(o == dim[1]-1): # Llegamos al limite lateral derecho, debemos volver hacia la izquierda
          i -= 1
          o -= 1
          self.movements -= 2
          direction = "L"
        o += 1
        self.current_posX = i
        self.current_posY = o
        #self.env.map[i][o] = 2
        if(self.env.map[i][o] == 0): # Podemos movernos a la proxima casilla sin ningun problema
          #print("Entra")
          self.env.map[i][o] = 2
        else:
          self.cleaned += 1
          self.env.map[i][o] = 2
          self.movements -= 1
        self.movements -= 1
      while(direction == "L" and self.movements > 0):
        #self.env.print_environment()
        if(self.cleaned/self.env.dirt_boxes == 1):  # Cumplimos con el grado de aceptación de la limpieza
          i = cant_vueltas + 1
          break
        else:
          if(i == 0 and o == dim[1]-1) or (i == 0 and o == 0): # LLegamos a una esquina superior
            if not([i,o]) in visits: # La esquina no fue previamente visitada
              visits.append([i,o])
            if(len(visits) == 2): # Visitamos ambas esquinas
              i = cant_vueltas + 1
              break
        self.env.map[i][o] = 0
        if(o == 0): # LLegamos al limite lateral izquierdo, debemos volver hacia la derecha
          i -= 1
          o += 1
          self.movements -= 2
          direction = "R"
        o -= 1
        self.current_posX = i
        self.current_posY = o
        if(self.env.map[i][o] == 0): # Podemos movernos a la proxima casilla sin ningun problema
          #print("Entra")
          self.env.map[i][o] = 2
        else:
          self.cleaned += 1
          self.env.map[i][o] = 2
          self.movements -= 1
        self.movements -= 1
  

   
  def LD(self):
    visits = []
    dim = np.shape(self.env.map)
    o = self.current_posY # Selecciona la columna
    i = self.current_posX # Selecciona la fila
    direction = "L"
    if(self.current_posY%2 == 0):
      cant_vueltas = dim[0]
    else:
      cant_vueltas = dim[0]-1
    while(i < cant_vueltas and self.movements > 0):
      while(direction == "R" and self.movements > 0): # Mientras nos podamos mover a la derecha, lo hacemos
        #self.env.print_environment()
        if(self.cleaned/self.env.dirt_boxes == 1):
          i = cant_vueltas
          break
        else:
          if(i == dim[0]-1 and o == dim[0]-1) or (i == dim[0]-1 and o == 0): # Llegamos a una esquina inferior
            if not([i,o]) in visits: # La esquina no fue previamente visitada
              visits.append([i,o])
            if(len(visits) == 2): # Visitamos ambas esquinas pero no completamos la limpieza
              i = cant_vueltas
              break
        self.env.map[i][o] = 0
        if(o == dim[1]-1): # Llegamos al limite lateral derecho, debemos volver hacia la izquierda
          i += 1
          o -= 1
          self.movements -= 2
          direction = "L"
        o += 1
        self.current_posX = i
        self.current_posY = o
        #self.env.map[i][o] = 2
        if(self.env.map[i][o] == 0): # Podemos movernos a la proxima casilla sin ningun problema
          #print("Entra")
          self.env.map[i][o] = 2
        else:
          self.cleaned += 1
          self.env.map[i][o] = 2
          self.movements -= 1
        self.movements -= 1
      while(direction == "L" and self.movements > 0):
        #self.env.print_environment()
        if(self.cleaned/self.env.dirt_boxes == 1):
          i = cant_vueltas
          break
        else:
          if(i == dim[0]-1 and o == dim[0]-1) or (i == dim[0]-1 and o == 0): # LLegamos a una esquina inferior
            if not([i,o]) in visits: # La esquina no fue previamente visitada
              visits.append([i,o])
            if(len(visits) == 2): # Visitamos ambas esquinas
              i = cant_vueltas
              break
        self.env.map[i][o] = 0
        if(o == 0): # LLegamos al limite lateral izquierdo, debemos volver hacia la izquierda
          i += 1
          o += 1
          self.movements -= 2
          direction = "R"
        o -= 1
        self.current_posX = i
        self.current_posY = o
        if(self.env.map[i][o] == 0): # Podemos movernos a la proxima casilla sin ningun problema
          #print("Entra")
          self.env.map[i][o] = 2
        else:
          self.cleaned += 1
          self.env.map[i][o] = 2
          self.movements -= 1
        self.movements -= 1


  def getPerformance(self):
    if(self.env.dirt_boxes > 0):
      return self.cleaned/self.env.dirt_boxes
    else:
      return 0





class Environment:
  def __init__(self,sizeX,sizeY,dirt_rate):
    self.sizeX = sizeX
    self.sizeY = sizeY
    self.dirt_rate = dirt_rate
    self.dirt_boxes = int((sizeX*sizeY)*dirt_rate)
    self.init_posX = random.randint(0,sizeX-1) # Selecciona la fila
    self.init_posY = random.randint(0,sizeY-1) # Selecciona la columna
    if(self.dirt_rate == 1):
      self.map = np.ones((sizeX, sizeY))
    else:
      self.map = np.zeros((sizeX, sizeY))
    self.map[self.init_posX][self.init_posY] = 2
    i = 0
    #self.print_environment()
    while(i < self.dirt_boxes):
      casilla = [random.randint(0,sizeX-1),random.randint(0,sizeY-1)]
      if(self.map[casilla[0]][casilla[1]] == 0):
        self.map[casilla[0]][casilla[1]] = 1
        #self.print_environment()
        i += 1
    
  # Mostramos el mapa con los lugares limpios (0), los lugares sucios (1)
  
  def print_environment(self):
    print("\n")
    for i in range(0,len(self.map)):
      print(self.map[i])
    

  # Definimos las acciones aceptadas por el autómata con respecto a la posición actual
  def accept_action(self,action,position):
    dim = np.shape(self.map)
    longX = dim[0]-1
    longY = dim[1]-1
    if(action == "R" and position[0] == longX): # Estamos en el limite derecho del mapa y nos queremos mover a la derecha
      return False
    elif(action == "L" and position[0] == 0): # Estamos en el limite izquierdo del mapa y nos queremos mover a la izquierda
      return False
    elif(action == "U" and position[1] == 0): # Estamos en el limite superior del mapa y nos queremos mover hacia arriba
      return False
    elif(action == "D" and position[1] == longY): # Estamos en el limite inferior del mapa y nos queremos mover hacia abajo
      return False
    else:
      return True
  
  #def get_performance(self,agent):

  
# El agente recibirá una matriz que representa al mapa.
# Las casillas con 0 estarán limpias mientras que las que tienen 1 estaran sucias
# Ademas, el agente partirá de una posicion inicial en la que comenzará a aspirar
# Dada una posición aleatoria, no podemos saber la suciedad en las celdas contiguas pero podemos determinar para donde nos conviene arrancar, por ejemplo, si estamos en la penultima celda de la matriz, nos conviene ir hacia la izquierda y hacia arriba, ya que hay más probabilidad de encontrar celdas sucias

#rows = 0
#cols = 0
#while(rows <= 0 or cols<=0):
  #rows = int(input("Ingrese el numero de filas del mapa: "))
  #cols = int(input("Ingrese el numero de columnas del mapa: "))

print("Agente Reflexivo Simple\nDimension/Porcentaje de Suciedad/Eficiencia")
suciedad = [0.1,0.2,0.4,0.8]
dimensiones = [2,4,8,16,32,64,128]
indexDimensiones = 0
indexSuciedad = 0
resultados = np.zeros((len(dimensiones)*len(suciedad),3))

for i in range(0,len(resultados)):
  for o in range(0,len(resultados[i])):

    if(o == 0):
      resultados[i][o] = dimensiones[indexDimensiones]
    elif(o == 1):
      resultados[i][o] = suciedad[indexSuciedad]
      indexSuciedad += 1
    else:
      map = Environment(dimensiones[indexDimensiones],dimensiones[indexDimensiones],suciedad[indexSuciedad])
      agent = Agent(map)
      agent.clean()
      #print("TERMINO DE LIMPIAR")
      resultados[i][o] = int(agent.getPerformance()*100)
    
    if(indexSuciedad == len(suciedad)):
      indexSuciedad = 0
      indexDimensiones += 1

    if(indexDimensiones == len(dimensiones)):
      indexDimensiones = 0

np.set_printoptions(suppress = True)
for i in resultados:
  print(i)
print("\n\n")



print("Agente Reflexivo Aleatorio\nDimension/Porcentaje de Suciedad/Eficiencia")
suciedad = [0.1,0.2,0.4,0.8]
dimensiones = [2,4,8,16,32,64,128]
indexDimensiones = 0
indexSuciedad = 0
resultados = np.zeros((len(dimensiones)*len(suciedad),3))

for i in range(0,len(resultados)):
  for o in range(0,len(resultados[i])):

    if(o == 0):
      resultados[i][o] = dimensiones[indexDimensiones]
    elif(o == 1):
      resultados[i][o] = suciedad[indexSuciedad]
      indexSuciedad += 1
    else:
      map = Environment(dimensiones[indexDimensiones],dimensiones[indexDimensiones],suciedad[indexSuciedad])
      agent = AgentAleatory(map)
      agent.clean()
      #print("TERMINO DE LIMPIAR")
      resultados[i][o] = int(agent.getPerformance()*100)
    
    if(indexSuciedad == len(suciedad)):
      indexSuciedad = 0
      indexDimensiones += 1

    if(indexDimensiones == len(dimensiones)):
      indexDimensiones = 0

np.set_printoptions(suppress = True)
for i in resultados:
  print(i)
print("\n\n")
