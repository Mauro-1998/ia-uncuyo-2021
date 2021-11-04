# Predicción de Precios de Criptomonedas Utilizando Series de Tiempo

## PPCUTS

# Integrantes

- Molina, Mauro

- Flores, Daniel Emiliano

# Descripción

## Explicación de la idea y de algunos conceptos previos

Gracias a los grandes avances tecnológicos de los últimos años se ha revolucionado la actividad financiera, generando un nuevo concepto de dinero: las criptomonedas.
Una criptomoneda es una moneda virtual creada como modelo de cambio alternativo al dinero tradicional.
Nuestro proyecto se centra en la idea de encontrar un patrón de comportamiento del valor de estas monedas a través de series temporales. Esto nos puede servir para detectar manipulaciones con un aumento y disminución de precios, por ejemplo, con una estrategia Pump and Dump.

Además dijimos que utilizaríamos Series Temporales pero, ¿Qué es una Serie Temporal?
Una serie temporal es un conjunto de muestras tomadas a intervalos de tiempo regulares, es decir, es una serie de datos indexados cronológicamente y espaciados uniformemente en el tiempo.
Las Series Temporales tienen 2 características principales:
    1. Es dependiente del tiempo: Por lo que sus observaciones dependen de ciertos parámetros en un instante de tiempo.
    2. Suelen tener algún tiempo de estacionalidad, crecer o decrecer: Por ejemplo, las ventas de una heladería se incrementan en verano y disminuyen en invierno, por lo que si tomamos series temporales de 3 meses, veremos funciones estrictamente crecientes o decrecientes, pero con fluctuaciones entre medio.

El problema de predecir el precio de criptomonedas puede describirse como un problema de pronóstico de series temporales, donde la serie de datos cronológicamente indexados es el precio y el objetivo es extrapolar para predecir su comportamiento en el futuro.

El análisis clásico de las series de tiempo, se basa en la suposición de que los valores que toma la variable de observación es la consecuencia de cuatro componentes, cuya actuación conjunta da como resultado los valores medidos, estas componentes son:

- Componente tendencia: Es el movimiento a largo plazo de la Serie Temporal. Es usual encontrarse con series temporales que presentan un movimiento sostenido en la misma dirección durante un amplio período de tiempo, con independencia de pequeñas oscilaciones al alza o a la baja. Podemos encontrarla bajo 2 enfoques:
    - Ajuste de curvas: En primer lugar, se puede “ajustar” una curva suave que recoja el perfil de la serie, dando lugar a tendencias lineales, polinómicas, exponenciales, etc. Este planteamiento presenta la ventaja de proporcionar una ecuación analítica que permite extrapolar dicha tendencia a un futuro próximo, proporcionando una primera aproximación a la predicción de los valores de la serie. 
Por el contrario, la elección de la forma funcional determina drásticamente dicha extrapolación, por lo que una mala elección se traduce directamente en la mala calidad de las predicciones. 

    - Filtrado de series: En segundo lugar, se puede intentar eliminar de la serie las componentes no deseadas, “filtrando” los datos originales. Dentro de este amplio campo, los filtros más utilizados por su sencillez son los lineales, que presentan buenos resultados cuando se trata de calcular la tendencia o de hacer predicciones a corto plazo. 

- Componente Estacional: Muchas series de tiempo presentan cierta periodicidad a lo largo del tiempo (por ejemplo, las ventas de una heladería aumenta con la llegada de la primavera y el verano). Estos efectos son fáciles de entender y se pueden medir explícitamente o incluso se pueden eliminar de la serie de datos, a este proceso se le llama des-estacionalización de la serie.

- Variación Cíclica: Estudia las oscilaciones producidas en un periodo de medio a largo plazo.
      
- Ruido: Esta componente no responde a ningún patrón de comportamiento, sino que es el resultado de factores fortuitos o aleatorios que inciden de forma aislada en una serie de tiempo.

Luego, nuestro modelo queda representado por la siguiente manera: 

        XT = TT + ET + CT + εT donde:
        - TT es la tendencia 
        - ET  es la componente estacional
        - CT es la variación cíclica (nótese que esta componente puede no existir)
        - εT es la componente aleatoria o el “ruido”

Luego, existen métodos para descomponer las series temporales en sus componentes y poder analizar cada una de ellas por separado.



## Limitaciones del proyecto

### TEORÍA DEL CAMINO ALEATORIO

La teoría del paseo aleatorio afirma que todo cambio, o evolución existente en los mercados financieros, no es medible y estimable. Ello se debe a la aleatoriedad. 
Además señala que no es posible realizar predicciones fiables del precio de activos, estudiando únicamente su evolución pasada.


### LA ALEATORIEDAD DE LOS PRECIOS

Según la teoría de paseo aleatorio, los precios de mercado se comportan de manera aleatoria y no dependiente de series temporales anteriores. Esto hace que su medición o estimación sea más complicada. Es por ello que esta metodología de estimación está más extendida en cálculos de evoluciones en el corto plazo, donde la aleatoriedad es menor que al pasar más tiempo y observar el largo plazo. Es importante destacar que la aleatoriedad de los precios se propone cuando los mercados son eficientes, ya que incluso la teoría del paseo aleatorio admite algunas ineficiencias de mercado.

### CRÍTICAS A LA TEORÍA DEL PASEO ALEATORIO
Recientemente han aparecido otros puntos de vista que afirman que sí que es posible mejorar carteras de inversión y «ganar» al mercado, especialmente por la existencia de mercados no eficientes (con comportamientos no aleatorios al menos en el corto plazo).

Los analistas técnicos argumentan que los humanos tendemos a comportarnos de la misma manera ante las mismas situaciones, por lo que ante situaciones idénticas (bajadas o subidas de precios), las reacciones serán las mismas y los movimientos de precios seguirán unos patrones.

### Formas de evaluación:

- Predicciones a los 5, 10, 30 minutos; 1, 4, 8, 12, 24 horas.

- Desempeño en al menos dos criptomonedas.

- Disminución progresiva del ratio de error.

- Menor error en periodos cortos.

# Justificación

Las características inherentes al problema indican un contexto tremendamente fluctuante, que depende de muchísimos factores que escapan de la observación de gráficas y se extiende a variables como un nombre, un aspecto tecnológico, o una pandemia.

La mayoría de los mortales tienen la capacidad de converger estos factores pero es muy improbable que sean capaces de acertar con alto grado de precisión un resultado, siquiera con un margen de error aceptable. Este tipo de comportamiento es el límite entre un algoritmo no inteligente y un algoritmo que aprende. Consideramos que estar por debajo del nivel de acierto humano mayoritario es alcanzable por un algoritmo no inteligente, mientras que un rendimiento igual o superior es alcanzable únicamente por un algoritmo de IA.

Un algoritmo de rendimiento semejante, y no superior, es factible en el análisis cortoplacista del problema a tratar. El margen de error en una predicción humana podría expresarse en función del tiempo como un límite que tiende a cero a medida que la diferencia de tiempo tambien tiende a cero. En otras palabras, la expresión diferencial del error es un objetivo acorde y semejante para un algoritmo que resuelva este problema.

El problema se vuelve prácticamente intratable en el análisis a medio y largo plazo. La tolerancia al error desafortunadamente se amplía. Sin embargo, ha ocurrido que expertos se han aventurado a dar resultados concretos con alta precisión. Este curioso y envidiable hecho solo sigue abriendo interrogantes, ¿es solo la ínfima probabilidad cumplida? ¿las máquinas resolverán lo que hoy no somos capaces de ver ni entender?. A fin de cuentas, para eso estamos aquí.

# Actividades

Inicio: 18 de Diciembre de 2021
Finalización estimada: 14 de Enero de 2022

1. Recopilación y lectura de artículos relevantes para adquirir un panorama amplio del problema (2 días)

2. Lectura de artículos y libros más especializados y práctica con herramientas a utilizar (5 días)

3. Búsqueda del dataset y una interfaz de comunicación (2 días)

4. Implementación base, estructuras, bibliotecas (2 días)

5. Implementación del algoritmo general (3 a 5 días)

6. Análisis de resultados (1 día)

7. Refinamiento (2 días)

8. Escritura de informe final (7 días)

9. Opcional: implementacion con deep learning.


FUENTES: 
https://www.colibri.udelar.edu.uy/jspui/bitstream/20.500.12008/20471/1/tg-gonzalez-federico.pdf
http://190.169.30.62/bitstream/10872/19752/1/PrincipalTEG.pdf
https://eprints.ucm.es/id/eprint/50312/1/TFG%20definitivo.pdf
