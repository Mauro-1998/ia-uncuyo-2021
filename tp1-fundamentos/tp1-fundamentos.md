Ejercicio 1:
A partir del capítulo 26 de AIMA, desarrollar un resumen sobre los conceptos más importantes volcados en el capítulo. El mismo deberá contener al menos 2000 palabras y ser escrito utilizando el formato markdown provisto por github https://github.com.

El documento debe incluir:

    a) Al menos 3 secciones correspondientes a las tres partes principales capítulo:
      i. Inteligencia Artificial Débil.
      ii. Inteligencia Artificial Fuerte.
      iii. La ética y los riesgos de desarrollar Inteligencia Artificial.

    b) Un mapa mental de los conceptos y sus relaciones. (Para esto es posible utilizar una herramienta como Xmind, Freemind, o alguna otra aplicación en línea). Ver ejemplo de un mapa mental en la figura de abajo.

    c) Una sección de discusión donde se indique una opinión personal sobre los enfoques tratados en el capítulo, su alcance, su viabilidad, etc. Se debe justificar las opiniones vertidas en esta sección.

Ejercicio 2:

    1. Crear un repositorio en github con el nombre de ia-uncuyo-2021 y dentro del mismo crear una carpeta con el nombre tp1-fundamentos. 

    2. Dentro de dicha carpeta colocar un archivo con el nombre tp1-fundamentos.md con el texto de acuerdo a lo especificado en la sección 1.

    3. Incluir en dicha carpeta las imágenes que considere necesarias. 

# RESPUESTAS

## 1-a) Resumen del capítulo 26

### Fundamentos Filosóficos
  Los filósofos han existido desde hace mucho más tiempo que las computadoras y se han planteado preguntas relacionadas como las siguientes. 
    1. ¿Cómo trabaja la mente?
    2. ¿Es posible que las máquinas actúen inteligentemente en la misma forma que la gente lo hace?
    3. Y si lo hicieran, ¿Tendrían mentes?

  Una definición puede ser: **La inteligencia artificial es el campo de la informática que busca que las máquinas desarrollen un comportamiento aparentemente inteligente. Y decimos que es aparentemente inteligente porque depende de lo que consideremos como inteligencia (esto abarca tanto a las IA capaces de razonar tal cual lo hacen las personas como a aquellas IA que solo buscan una solución óptima a un problema sencillo).**

  La idea es que, desde el punto de vista de un observador externo, se pueda apreciar que una máquina resuelva una tarea con cierta inteligencia.
	 
   #### Inteligencia Artificial Débil
      La idea o fundamento teórico de la inteligencia artificial débil es que las máquinas pueden actuar como si fueran inteligentes. Es decir, a la hipótesis de que las máquinas pueden actuar replicando comportamiento inteligente se la denomina inteligencia artificial débil.
      La pregunta clave para determinar si se trata de una IA débil es: ¿Pueden las máquinas actuar con inteligencia?
  
  Claramente, si la IA es posible o no, depende de cómo se defina esta misma.
  
  Otra definición puede ser la siguiente: **(...)”Definimos a la IA como la búsqueda del mejor programa agente dada una determinada arquitectura”(...)**

  Bajo esta definición, la IA es posible para cualquier arquitectura digital de **_k_** bits, y lo único que debemos hacer es probar las **_2^k_** posibles combinaciones y quedarnos con la que mejor desempeño nos haya dado.
  Esto no es muy práctico desde el punto de vista de la algoritmia.
      Alan Turing propuso que, en lugar de preguntarnos si las máquinas pueden pensar, deberíamos preguntarnos si las máquinas pueden pasar una prueba de inteligencia conductual, que se denominó “Test de Turing”. 

Este test consiste en entablar una conversación entre un interrogador y una máquina (a través de mensajes mecanografiados o de una consola) durante 5 minutos. Si el interrogador no puede discernir si se trata de una persona o una máquina, podemos afirmar que la máquina pasó el test de Turing.
      El propio Alan Turign examinó una amplia variedad de posibles objeciones que se pueden realizar con el fin de determinar si una máquina es inteligente o no. Por ejemplo:
      
#### El argumento de la incapacidad
Este argumento afirma que “una máquina nunca podrá X” siendo X una variable que toma valores de un conjunto. 
Por ejemplo:
  - Una máquina nunca podrá ser amable
  - Una máquina nunca podrá ser ingeniosa
  - Una máquina nunca podrá enamorarse

Está claro que las computadoras pueden realizar muchas tareas de gran complejidad mucho mejor que los humanos, incluso tareas que requieren ingenio y comprensión humana.
Esto no significa que las computadoras utilicen el conocimiento y la compresión humana para realizar las tareas.

El punto a mostrar es que la primera suposición sobre los procesos mentales necesarios para producir una determinada conducta suele ser errónea.

#### Objeción Matemática
Es sabido, por Gödel y Turing, que ciertas cuestiones matemáticas son, en principio, incontestables. Dicho en otras palabras: **(…)”Hay afirmaciones o hechos matemáticos que nunca van a poder ser probados”(…)**

El teorema de la incompletitud afirma que para cualquier axioma “F” lo suficientemente poderoso para desarrollar una aritmética, es posible construir una sentencia G(F) con las siguientes propiedades:
 - G(F) es una oración de F, pero no puede probarse dentro de F.
 - Si F es consistente, entonces G(F) es verdadero.

Básicamente, lo que queremos decir es que, para cualquier conjunto de axiomas, siempre es posible hacer enunciados que, a partir de esos axiomas, no pueden demostrarse.
      
De esto, se puede deducir que, por el teorema de la incompletitud, las máquinas son mentalmente inferiores a los humanos, ya que son sistemas formales limitados por este teorema. Pero esta inferencia tiene algunas falencias:
 - Primero, el teorema de incompletitud de Gödel se aplica solo a sistemas formales que son poderosos suficiente para generar una aritmética. Esto incluye las máquinas de Turing, y la afirmación anterior se basa, en parte, sobre la afirmación de que las computadoras son máquinas de Turing. Esta es una buena aproximación, pero no es muy cierto. Las máquinas de Turing son infinitas, mientras que las computadoras son finitas, y cualquier computadora puede por lo tanto, ser descrito como un sistema (muy grande) en la lógica proposicional, que no está sujeto a Teorema de incompletitud de Gödel. 
 - Segundo, un agente no debe avergonzarse de no poder establecer la veracidad de una sentencia que otros agentes si pueden demostrar.
 - Tercero, incluso si admitimos que las computadoras tienen limitaciones sobre lo que pueden probar, los humanos no estamos exentos de ello. 

#### El argumento de la informalidad
Esta afirmación nos dice en que el comportamiento humano es demasiado complejo para poder captarse mediante un conjunto de reglas y como las computadoras solo pueden seguir reglas o hechos, no pueden generar un comportamiento tan inteligente como el de los hombres. Esto se denomina **problema de cualificación**. 
  #### Inteligencia Artificial Fuerte
      Denominamos inteligencia artificial fuerte a la prueba o afirmación de que las máquinas pueden actuar inteligentemente y no solo replicar el comportamiento. Es decir, la máquina piensa por si misma y no simula un comportamiento. Tiene una conciencia propia, sensibilidad y autoconocimiento de si misma y del mundo que la rodea.

Muchos filósofos han afirmado que una máquina que pasa el Test de Turing no quiere decir que esté realmente pensando, sería solamente una simulación de la acción de pensar.

Ahora considerando la siguiente definición, no podemos afirmar que puedan haber inteligencias artificiales: 

**_(...)”Hasta que una máquina pueda escribir un soneto o componer un concierto porque sienta los pensamientos y las emociones, y no porque haya una lluvia de símbolos, podría reconocer que la máquina iguala al cerebro, es decir, no sólo escribirlo sino que sepa que lo ha hecho.”(…)_**

Esto se conoce como **argumento de la conciencia**, es decir, la máquina tiene que ser consciente de lo que hace. Poder dar explicaciones de porqué hizo lo que hizo (por así decir).

La **teoría del funcionalismo** dice que un estado mental es cualquier condición causal inmediata entre la entrada y la salida. Es decir, que el estado mental es resultado de las experiencias previas.
Entonces, bajo esta teoría, dos sistemas con procesos causales isomórficos deberían llegar al mismo estado mental final, ergo, un programa informático podría tener los mismos estados mentales que una persona.

_Es decir, esta teoría se basa desde el punto de vista de los autómatas._

En contraste, la teoría del **naturalismo biológico** dice que los estados mentales son características emergentes de alto nivel originadas por procesos neurológicos de bajo nivel en las neuronas, y lo que importa son las propiedades (no especificadas) de las neuronas. Así pues, los estados mentales no se pueden duplicar justo en la base de algún programa que tiene la misma estructura funcional con el mismo comportamiento de entrada y salida; necesitaríamos que el programa se ejecutara en una arquitectura con la misma potencia que las neuronas.

### Ética y Riesgos de desarrollar IA
Hasta ahora solo nos hemos enfocado en si podemos o no desarrollar la IA, pero debemos también tener en cuenta las consecuencias que implica desarrollarla. Es decir, debemos analizar y comprobar que los beneficios de desarrollar la IA sean mayores que sus desventajas.
Por ejemplo:
1. El motor de combustión interna indujo a los gases de efecto invernadero, que derivó en el calentamiento global
2. La fisión nuclear produjo el desastre de Chernobyl

Realizando un análisis rápido con respecto a la IA, se producen varias desventajas:

   1. **Se generarían desempleos debido a la automatización** 
        
        Las empresas podrían optar por automatizar todo con el fin de maximizar las ganancias, produciendo desempleos.

   2. **Las personas tendrían demasiado tiempo de ocio** 
        
        Alvin Toffler noto que la semana laboral se redujo un 50% a finales del siglo, por lo que predijo que volvería a pasar en el año 2000, pero esto no fue así. De hecho, se incrementó el numero de horas laborales ya que requería mayor demanda para mantener a los sistemas funcionando.
        
   3. **La utilización de los sistemas de IA podría llevar a una pérdida de responsabilidad** 
        
        Cuando un médico depende del juicio de un sistema médico experto para hacer diagnóstico, ¿quién es el culpable si el diagnóstico es erróneo? Para evitar estos conflictos, los sistemas expertos no son quienes toman la decisión final, sino que brindan apoyo, contexto y análisis al médico para que sea este quien tome la decisión final.
        
   4. **Las personas podrían perder algunos de sus derechos privados** 
        
        Las voces pueden replicarse utilizando IA, por lo que una llamada telefónica podría volverse insegura de alguna forma.
      
   5. **Las personas podrían perder el sentido de ser únicos** 
        
        La investigación en IA hace posible la idea de que los hombres sean vistos o interpretados como autómatas, una idea que produce pérdida de autonomía, libre albedrío (ya que estaríamos inconscientemente “eligiendo” algo ya establecido) y humanidad.
        
   6. **El éxito de la IA podría implicar el fin de la raza humana** 
        
        Vamos a definir una máquina ultra inteligente como una máquina que puede sobrepasar con mucho todas las actividades intelectuales de cualquier hombre, por muy inteligente que sea. Puesto que el diseño de las máquinas es una de estas actividades intelectuales, una máquina ultra inteligente podría diseñar máquinas incluso mejores; entonces existiría incuestionablemente una “explosión de inteligencia”, y la inteligencia del hombre quedaría bastante atrás.

#### Resumen
Para resumir un poco, consideramos IA débil a aquella inteligencia que busca replicar o imitar el comportamiento de las personas.
Llamamos IA fuerte a aquella que es capaz de tener conciencia por sí misma y no busca imitar un comportamiento, sino que lo razona o deduce por su cuenta.
El paso de una IA débil a una IA fuerte se da a través del aprendizaje. Algo que resulta relativamente sencillo, como jugar al 3 en línea, puede resultar sumamente complejo cuando se contemplan todos los escenarios posibles, tan complejo que, muchas veces, su algoritmia resulta inviable.
Por ello requerimos que la máquina contemple solo los casos usuales, y cuando ocurra un caso nuevo, aprenda de él. Esto evita que deba conocer hasta los casos imposibles. Esto se conoce como Maching Learning.



## 1-b) Mapa mental


![image](https://user-images.githubusercontent.com/63267942/128918314-ca320be1-b9e4-4eb1-bbdd-3e86e6811e67.png)






## 1-c) Personalmente creo que la Inteligencia Artificial tiene muchas ventajas y gran desarrollo a futuro. 
A corto plazo veo mucho mas útil una inteligencia artificial débil, ya que tenemos métodos para crearlas y para determinar que se trata de una IA débil. Por ejemplo, podríamos crear (junto con la robótica) partes del cuerpo para las personas que lo necesiten, asistentes médicos para pronósticos de enfermedades, firmwares inteligentes para evitar ataques cibernéticos, automatizar tareas simples (como el aspirado de una casa) para no perder tiempo en hacerlo, autos autónomos para evitar accidentes de tráfico, etc. 

Por otro lado, veo más importante el desarrollo de una IA fuerte, ya que podría superar la mente humana y procesar los datos mucho mas rápidos, incluso, pudiendo crear a otras IA fuertes que sean superiores y comenzar una cadena evolutiva de inteligencias, para descubrir cosas que para el hombre, hoy día son impensadas.

Opino que es una buena herramienta a desarrollar pero que hay que contemplar la ética y un análisis de costo/beneficio antes de desarrollarlas, para mitigar el impacto negativo que puedan tener en la sociedad.
