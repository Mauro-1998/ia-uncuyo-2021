class Node():
  tablero = None
  parent = None
  priority = None
  

class PriorityQueue:
  def __init__(self):
    """ Crea una cola vacía. """
    # La cola vacía se representa por una lista vacía
    self.items=[]

  def isEmpty(self):
    """ Devuelve True si la cola esta vacía, False si no."""
    return self.items == []
	
  def enqueue(self, L, priority):
    node = Node()
    node.tablero = L
    node.priority = priority
    if(len(self.items) == 0):
      self.items.append(node)
    else:
      for i in range(0,len(self.items)):
        if(node.priority < self.items[i].priority):
          self.items.insert(i, node)
          break
        else:
          if(i == len(self.items)-1):
            self.items.insert(i+1, node)

  def dequeue(self):
    """ Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError. """
    try:
        return self.items.pop(0)
    except:
        raise ValueError("La cola está vacía")
	
  def length(self):
    return len(self.items)


  def search(self,L):
    for e in self.items:
      if(e == L):
        return e
    return None

  def delete(self,item):
    self.remove(item)


  
  def printQueue(self):
    for x in self.items:
      if(x == self.items[-1]):
        print(x.tablero)
      else:
        print(str(x.tablero) + " - ", end="")
