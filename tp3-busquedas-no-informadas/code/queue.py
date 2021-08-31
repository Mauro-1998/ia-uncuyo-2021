class Node:
  row = None
  col = None
  parent = None

class Queue:
  def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.items=[]

  def isEmpty(self):
    """ Devuelve True si la cola esta vacía, False si no."""
    return self.items == []
	
  def enqueue(self, row, col, parent):
    """ Agrega el elemento x como último de la cola. """
    if(self.search(row,col) == None):
      node = Node()
      node.row = row
      node.col = col
      node.parent = parent
      self.items.append(node)

    

  def dequeue(self):
    """ Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError. """
    try:
        return self.items.pop(0)
    except:
        raise ValueError("La cola está vacía")
	
  def length(self):
    return len(self.items)

  def search(self,row,col):
    for e in self.items:
      if(e.col == col and e.row == row):
        return e
    return None

  
  def printQueue(self):
    for x in self.items:
      if(x == self.items[-1]):
        print("[" + str(x.row) + "-" + str(x.col) + "]")
      else:
        print("[" + str(x.row) + "-" + str(x.col) + "] - ", end="")
