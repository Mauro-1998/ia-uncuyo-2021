**2.10 Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.7, en el que se penalice al agente con un punto en cada movimiento.**
  
  *a. ¿Puede un agente reflexivo simple ser perfectamente racional en este medio? Explíquese.*
  
  Por definición de agente racional, es aquel que maximiza la función de desempeño, por ende, podría intentar serlo sin poder lograrlo. 
  Por ejemplo: Considerando la funcion de desempeño ***Fd = casillas limpiadas/casillas sucias***, podríamos definir a nuestro agente para que, respecto de la posición inicial y conociendo el mapa, comienze a recorrer el mapa hacia donde más casillas hay (con el fin
  de recorrer más casillas y tener más probabilidad de encontrar casillas sucias, pero como estas se distribuyen de forma aleatoria, puede no encontrar ninguna.
  
  Por ende no puede ser perfectamente racional, ya que no estaría maximizando la funcion de desempeño (se puede quedar sin bateria antes)
  
  *b. ¿Qué sucedería con un agente reflexivo con estado? Diseñe este agente.*
  
   Sería una implementación mas inteligente, ya que el agente podría deducir que casillas visitar y cuales no, ya que un estado puede llevarme a otros estados que no visitados previamente (una casilla puede llevarme a otra casilla que no he visitado antes )
  
  *c. ¿Cómo se responderían las preguntas a y b si las percepciones proporcionan al agente información sobre el nivel de suciedad/limpieza de todas las cuadrículas del entorno?*
  
  En este caso, una posible implementacion del agente podría seer la de generar un arbol de recubrimiento minimo que abarquen a todas las ubicaciones sucias y solo visitar las mínimas indispensables que no esten sucias, con el fin de optimizar la funcion de desempeño, y podría decirse que es un agente racional mas completo

**2.11 Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.8, en el que la geografía del entorno (su extensión, límites, y obstáculos) sea desconocida, así como, la disposición inicial de la suciedad. (El agente puede ir hacia arriba, abajo, así como, hacia la derecha y a la izquierda.)**

  *a. ¿Puede un agente reflexivo simple ser perfectamente racional en este medio? Explíquese.*
  
  No puede ser perfectamente racional, ya que el agente no podrá determinar adonde se encuentra la suciedad y podría visitar zonas que previamente ha visitado.
  
  *b. ¿Puede un agente reflexivo simple con una función de agente aleatoria superar a un agente reflexivo simple? Diseñe un agente de este tipo y medir su rendimiento en varios medios.*

  Segun muestran las tablas de desempeño de los agentes programados en Python, no, puede comportarse de igual forma si el mapa es pequeño, pero cuando se agranda dicho mapa, la performance del agente aleatorio cae drásticamente
  
  *c. ¿Se puede diseñar un entorno en el que el agente con la función aleatoria obtenga una actuación muy pobre? Muestre los resultados.*
  
  Si se puede diseñar dicho mapa, de hecho, en los mapas de 64x64 y 128x128 la performance del agente aleatorio cae drásticamente
  
  *d. ¿Puede un agente reflexivo con estado mejorar los resultados de un agente reactivo simple? Diseñe un agente de este tipo y medir su eficiencia en distintos medios. ¿Se puede diseñar un agente racional de este tipo?*
  
  El agente reflexivo con estado es una mejora del agente reflexivo simple, ya que este podría recordar en un estado su ubicación inicial
