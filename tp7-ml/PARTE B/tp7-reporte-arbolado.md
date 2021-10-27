# PARTE B
### Descripción del proceso
    1- Importamos los archivos de entrenamiento y de prueba

    2- Limpiamos los datos de cada conjunto, nos quedamos con:
      - especie
      - altura
      - circ_tronco_cm
      - diametro_tronco
      - seccion
      - nombre_seccion
      - circ_tronco_cm_cat --> Esta variable fue creada a partir de 4 puntos equidistantes del promedio
      - inclinacion_peligrosa --> Este atributo solo está presente en el conjunto de entrenamiento
     
    3- Realizamos la configuración del algoritmo para que utilice Cross Validation con 10 folds
    
    4- Probamos varios algoritmos:
      - Vecinos Cercanos
      - Naive Bayes
      - Random Forest

### Resultados obtenidos sobre el conjunto de validación
[envio (4).csv](https://github.com/Mauro-1998/ia-uncuyo-2021/files/7426808/envio.4.csv)

### Resultados obtenidos por Kaggle

![Captura de pantalla de 2021-10-27 11-09-22](https://user-images.githubusercontent.com/63267942/139082623-49766808-40db-465e-95bc-e45879b27c9d.png)

### Descripción detallada del algoritmo propuesto

Una vez que importamos los conjuntos de prueba y entrenamiento, la idea es limpiar un poco los conjuntos, para quedarnos con la información importante y que los mismos datos no nos estropeen las mediciones. Nos quedamos con los siguientes datos.
especie
  - altura
  - circ_tronco_cm
  - diametro_tronco
  - seccion
  - nombre_seccion
  - circ_tronco_cm_cat --> Esta variable fue creada a partir de 4 puntos equidistantes del promedio
  - inclinacion_peligrosa --> Este atributo solo está presente en el conjunto de entrenamiento

El problema que tenemos ahora es que vamos a clasificar según la inclinación peligrosa (cuántos árboles con inclinación peligrosa hay y cuantos sin inclinación peligrosa). Cuando analizamos los datos, hay un claro desbalanceo de las cargas respecto de este parametro, por lo que procedemos a bifurcarlo en 2 conjuntos diferentes.

Una vez que separamos los conjuntos, procedemos a balancearlos. Para ello, creamos una partición del conjunto de los árboles sin inclinación peligrosa de forma tal que abarque a todas las especies de árboles y la cantidad total sea mas balanceada con respecto al otro conjunto.

El siguiente paso es unir los conjuntos y aplicarles un Merge, para mezclarlos entre todos.

Finalmente, entrenamos al algoritmo utilizando Random Forest y Cross Validation para luego exponerlo a casos que no había visto previamente.
