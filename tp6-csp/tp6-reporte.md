# TP N°6: CSP
### 1. Describir en detalle una formulación CSP para el Sudoku.
   **Variables:** Cada celda vacía del tablero
   
   **Dominio:** Para cada celda, el dominio es el conjunto de números del 1 al 9 salvo aquellos que ya se utilizaron en la fila, columna o submatriz de 3x3.
   
   **Restricciones:** Los números no se pueden repetir en ninguna fila, columna o submatriz
   
### 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {AO=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).
![image](https://user-images.githubusercontent.com/63267942/136437736-d2554470-69b5-422d-a03c-825b0fee380e.png)

ebemos colorear AS ahora, por lo tanto aplicamos el algoritmo.

Inicialmente, poseemos una cola que contiene a todas las aristas del grafo:
A = [ {AO,TN} , {AO,AS} , {TN, AS} , {TN, Q} , {AS, Q} , {AS,NGS} , {AS,V} , {V, NGS} , {Q,NGS} ]
Extraemos la primer arista: {AO,TN}, chequeando los valores consistentes para AS, encontramos que puede ser solo VERDE, ya que poseemos otra arista ({AS,V}) donde V es AZUL

![image](https://user-images.githubusercontent.com/63267942/136437932-bfd53f1b-24ff-4f65-b1d2-20af01ce5c51.png)

Luego, TN debe ser AZUL, ya que limita con AO = ROJO y AS = VERDE

![image](https://user-images.githubusercontent.com/63267942/136437963-8feebe6e-125a-4152-8724-2203e6f9a161.png)

Ahora, Q debe ser necesariamente ROJO y a su vez NGS tambien debe ser necesariamente ROJO, por lo que se presenta una inconsistencia.

### 3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).
Si usaramos árboles estructurados, el algoritmo AC-3 que tiene una complejidad inicial de O(n^2.d^2) se ve reducida a O(n.d2), ya que se verían reducidas la cantidad de aristas hasta formar una lista, que tiene orden O(n) (en el peor caso)
Esto se logra eiminando la variable con más aristas del grafo (por eliminar la variable nos referimos a darle un valor antes que a otra variable --> Deja de ser variable para ser constante)

![image](https://user-images.githubusercontent.com/63267942/136438789-b0a21d30-c261-4dde-ab81-d8f6ae4a0f87.png)

### 4. AC-3 coloca de nuevo en la cola todo arco (Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Si por cada arco (Xk,Xi) se lleva cuenta del número de valores que quedan de Xi que sean consistentes con Xk . Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n^2.d^2)
El algoritmo AC-3 funciona de la siguiente manera.
Cada vez que se borra un valor de la cola de variables (porque se le asignó un valor), se elimina el valor asignado en la cola de valores de sus vecinos y, cuando se detecta que alguna cola de valores quedó vacía, se realiza BackTrack.

Si llevaramos cuenta del numero de posibles valores que quedan para las demás variables, podríamos:

- Por un lado, tomar el nodo que más aristas adyacentes tenga. De esta forma reducimos el faltor de ramificación, ya que se “limita” la expansión de un nodo que limita con muchos otros.

- Por otro lado, darnos cuenta que va a ocurrir una inconsistencia antes de que esta ocurra, permitiendo hacer BackTrack antes sin explorar dicha rama y podando el árbol generado por el BackTracking
       
### 5. Demostrar la correctitud del algoritmo CSP para  árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar: 

  a) Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)
  
   Mostraremos que cualquier PSR estructurado por árbol puede resolverse en tiempo lineal en el número de variables. El algoritmo tiene los siguientes pasos:

    1. Elija cualquier variable como la raíz del árbol, y ordene las variables desde la raíz a las hojas de tal modo que el padre de cada nodo en el árbol lo precede en el ordenamiento. Etiquetar las variables X1 , … , Xn en orden. Ahora, cada variable excepto la raíz tiene exactamente una variable padre.

    2. Para j desde n hasta 2, aplicar la consistencia de arco al arco (Xi , Xj ), donde Xi es el padre de Xj , quitando los valores del DOMINIO [Xi] que sea necesario.
       
    3. Para j desde 1 a n, asigne cualquier valor para Xj consistente con el valor asignado para Xi , donde Xi es el padre de Xj . 
       
   Hay dos puntos claves a destacar:
      
   - Primero, después del paso 2 el PSR es directamente arco-consistente, entonces la asignación de valores en el paso 3 no requiere ninguna vuelta atrás.  

   - Segundo, aplicando la comprobación de consistencia de arco en orden inverso en el paso 2, el algoritmo asegura que cualquier valor suprimido no puede poner en peligro la consistencia de arcos que ya han sido tratados. El algoritmo completo se ejecuta en tiempo O(nd2).
  
  b) Argumentar por qué lo demostrado en a es suficiente. 
  
### 6. Implementar una solución al problema de las n-reinas utilizando una formulación CSP

  a. Implementar una solución utilizando backtracking

  b. Implementar una solución utilizando encadenamiento hacia adelante.}
  
  c. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas.

  d. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8, 10, 12 y 15 reinas.

  e. Realizar un gráfico de cajas para los puntos c y d.
  
  BACKTRACKING
  - Estados Visitados
  
![image](https://user-images.githubusercontent.com/63267942/136440439-5b525f27-271c-4a3f-a1a1-94bbad0b99a0.png)
  
  - Tiempos Requeridos

![image](https://user-images.githubusercontent.com/63267942/136440456-d0bc265e-8169-44a1-b7e4-c062096b5ed7.png)
        

  FORWARD CHECKING
  - Estados Visitados

![image](https://user-images.githubusercontent.com/63267942/136440471-527476a7-bded-48b8-baa4-ad43a84684d6.png)

  - Tiempos Requeridos 

![image](https://user-images.githubusercontent.com/63267942/136440510-a7277d03-d1fb-44eb-be8b-eac62e8b31c7.png)
        
