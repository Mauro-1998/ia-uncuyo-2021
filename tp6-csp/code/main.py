import time

def BackTracking(solucion,etapa,n,states,index):
  inicio = time.time()
  global estadosBT
  global timesBT
  if etapa>=n: # si la etapa es mayor que n, entonces devolvemos falso
	  return False
	#solucion.append(0)
  exito = False # inicializamos exito a False
  while True:
    
    if (solucion[etapa] < n):# si el valor de la columna para la fila es mayor o igual que n, entonces no seguimos incrementando, con esto evitamos indices fuera del array.
      solucion[etapa] = solucion[etapa] + 1 # incrementamos el valor de columna para la reina i-esima de la fila i-esima.
      states += 1 # Incrementamos el estado que visitó
    if (Valido(solucion,etapa)): # si la reina i-esima de la fila i-esima de la columna j en la etapa k no entra en conflicto con otra reina, proseguimos.
      if etapa != n-1: # si aun no hemos acabado todas las etapas, procedemos a la siguiente etapa.
        exito = BackTracking(solucion, etapa+1,n,states,index)
        if exito==False: # si del valor devuelto de Reinas tenemos falso, ponemos a 0 el valor de la etapa + 1 para asi descartar los nodos fracaso.
          solucion[etapa+1] = 0
      else:
        fin = time.time()
        timesBT.append(fin-inicio)
        estadosBT.append(states)
        print(solucion)
        exito = True
        #return
    if (solucion[etapa]==n or exito==True):         # si el valor de la columna j de la etapa k es igual a n o exito es igual a True, salimos del bucle y devolvemos exito.
      break
  return exito

def Valido(solucion,etapa):
	# Comprueba si el vector solucion construido hasta la etapa es 
	# prometedor, es decir, si la reina se puede situar en la columna de la etapa
	for i in range(etapa):
		if(solucion[i] == solucion[etapa]) or (ValAbs(solucion[i],solucion[etapa])==ValAbs(i,etapa)):
			return False
	return True

def ValAbs(x,y):
	if x>y:
		return x - y
	else:
		return y - x

def generarPosiciones(tablero):
  posiciones = [[i for i in range(1,len(tablero)+1)] for r in range(0,len(tablero))]
  if([] in posiciones):
    return posiciones
  else:
    for i in range(0,len(tablero)):
      row = tablero[i]
      col = i+1

      # Eliminamos filas
      for o in range(col,len(posiciones)):
        if(row in posiciones[o]):
          posiciones[o].remove(row)
      
      # Eliminamos diagonales descendentes
      contador = 1
      while(row+contador <= len(tablero) and col+contador <= len(tablero)):
        if(row+contador in posiciones[col+contador-1]):
          posiciones[col+contador-1].remove(row+contador)
        contador += 1
      
       # Eliminamos las diagonales ascendentes
      contador = 1
      while(row-contador >= 0 and col+contador <= len(tablero)):
        if(row-contador in posiciones[col+contador-1]):
          posiciones[col+contador-1].remove(row-contador)
        contador += 1

  return posiciones



def ForwardChecking(solucion,etapa,n,states,index):
  inicio = time.time()
  if(etapa>=n): # si la etapa es mayor que n, entonces devolvemos falso
	  return False
  else:
    l = generarPosiciones(solucion) # Construimos los proximos valores suponiendo que colocamos
    exito = False
    if(l[etapa] == []):
      return False
    else:
      if(etapa == n-1):
        solucion[etapa] = l[etapa][0]
        fin = time.time()
        timesFC.append(fin-inicio)
        estadosFC.append(states)
        print(solucion)
        #exito = True
        #print(solucion)
        return True
      for i in l[etapa]:
        solucion[etapa] = i
        exito = ForwardChecking(solucion, etapa+1,n,states+1,index)
        if(exito or solucion[etapa]==n):
          break
          
  return exito

n = [4,8,10,12,15]
estadosBT = []
timesBT = []
estadosFC = []
timesFC = []

index = 0
for i in n:  
  print("---------- SOLUCIONES CON BACKTRACKING SOLO ----------")
  BackTracking([0]*i,0,i,0,index)
  print("---------- SOLUCIONES CON FORWARD CHECKING ----------")
  ForwardChecking([0]*i,0,i,0,index)
  #print("\n\n")
  index += 1
  print("\n")
print("\n\n")
print("ESTADOS BACKTRACKING: " + str(estadosBT))
print("TIEMPOS BACKTRACKING: " + str(timesBT))
print("\n")
print("ESTADOS FORWARD CHECKING: " + str(estadosFC))
print("TIEMPOS FORWARD CHECKING: " + str(timesFC))

# Vemos que el algoritmo de ForwardChecking tarda más tiempo que el Backtracking común, y esto es porque ForwardChecking calcula la cantidad de posiciones futuras en base a las reinas ya colocadas, por lo que requiere de más tiempo, pero en consecuencia, visita mucho menos estados 
