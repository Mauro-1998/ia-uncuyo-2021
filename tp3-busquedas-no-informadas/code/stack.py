class Node:
  row = None
  col = None
  parent = None

class Stack:
  """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

  def __init__(self):
    """ Crea una pila vacía. """
    # La pila vacía se representa con una lista vacía
    self.items=[]
  
  def push(self, row, col, parent):
    """ Agrega el elemento x a la pila. """
    # Apilar es agregar al final de la lista.
    if(self.search(row,col) == None):
      node = Node()
      node.row = row
      node.col = col
      node.parent = parent
      self.items.append(node)
  
  def pop(self):
    """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción. """
    try:
      return self.items.pop()
    except IndexError:
      raise ValueError("La pila está vacía")

  def length(self):
    return len(self.items)


  def search(self,row,col):
    for e in self.items:
      if(e.col == col and e.row == row):
        return e
    return None

  def printStack(self):
    for x in self.items:
      if(x == self.items[-1]):
        print("[" + str(x.row) + "-" + str(x.col) + "]")
      else:
        print("[" + str(x.row) + "-" + str(x.col) + "] - ", end="")
