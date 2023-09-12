[![henrylogo.png](https://i.postimg.cc/JzjbH2sC/henrylogo.png)](https://postimg.cc/hXPJHM82)
<h1 style="color:red"><center>Yelp & Google Maps - Opiniones y Recomendaciones</center></h1>
<h1 style="color:red"><center>Proyecto Grupal</center></h1>
<h2>Integrantes:</h2>
Marles Rodríguez Iovan Dario - Data Analyst<br>
Masat Brian Emiliano - Data Engineer<br>
Pernett Garcia Alberto Mario - Supply Chain Analyst<br>
Tejerina Calalanis Juan Matias - Machine Learning Engineer<br>

<h2>Marco de Referencia:</h2>
La voz de los usuarios es una fuente de datos en constante expansión gracias a las plataformas de reseñas. La capacidad de analizar estas opiniones se ha convertido en un recurso crucial para la formulación de estrategias de mercado efectivas. Yelp, una plataforma global de reseñas que abarca diversos sectores, la cual ha democratizado la retroalimentación del consumidor. Aquí, los usuarios expresan sus vivencias y recomendaciones. Esta información es un recurso inestimable para las empresas, pues brinda perspicacia sobre la percepción del usuario, evaluando desempeño y detectando áreas de mejora. En paralelo, Google Maps, con su integrada plataforma de reseñas, desempeña un papel similar. Los usuarios confían en estas críticas para tomar decisiones sobre dónde comer, dormir, que lugares visitar y mucho más. Estos datos son una mina de oro para las empresas, ya que proporcionan una visión objetiva de su desempeño y oportunidades para optimizar sus servicios.

<h2>Rol:</h2>
Como miembros de una consultora de análisis de datos hemos sido convocados para examinar el mercado estadounidense en profundidad. Nuestro cliente pertenece a un conglomerado de negocios que abarcan la industria de restaurantes y servicios afines. Nuestra misión es llevar a cabo un análisis en profundidad de las opiniones de usuarios en Yelp y Google Maps sobre hoteles, restaurantes y otros emprendimientos turísticos y de entretenimiento. Mediante técnicas avanzadas de análisis de sentimientos, aspiramos a pronosticar las áreas de negocios que experimentarán crecimiento o declive. También deseamos identificar ubicaciones estratégicas para establecer nuevas sucursales y crear un sistema de recomendación personalizado para los usuarios de ambas plataformas. Esto permitirá a los usuarios descubrir lugares basados en las experiencias previas que han tenido otras personas.

[![position.jpg](https://i.postimg.cc/TYF7VjXs/position.jpg)](https://postimg.cc/gnyHdZjy) 

<h2>Problemática a Abordar:</h2>
Navegar por el vasto océano de opiniones de usuarios en plataformas como Yelp y Google Maps demanda tiempo que es considerado como un recurso escaso, el cual en muchas ocasiones lleva a las personas a tomar decisiones erroneas al momento de decidir a que lugar ir y a cual no. Como asesores presentamos un plan de cuatro fases para asegurar que nuestro proyecto de análisis y recomendaciones trace el camino ideal, ayudando a las personas a tomar la decisión correcta. Nuestro objetivo es la recopilación, procesamiento y análisis de datos en los cinco estados con mayor PBI total de los Estados Unidos, con el propósito de comprender las opiniones de los usuarios, anticipar tendencias de crecimiento o declive en el sector de restaurantes, seleccionar ubicaciones estratégicas y desarrollar un sistema de recomendación personalizado para los usuarios.

<h2>Fases:</h2>

<h4>Fase 1:</h4> 
Análisis de Sentimiento para Tendencias de Crecimiento y Declive: <br>
Implementaremos análisis de sentimientos para anticipar las direcciones en las que los diversos sectores de negocios pueden evolucionar. Esto nos permitirá identificar oportunidades de crecimiento y advertir sobre posibles declives, proporcionando una base sólida para decisiones estratégicas.
Para esto se plantea la creacion de un índice de sentimiento que es una medida que se utiliza para determinar la polaridad o el tono emocional de un texto. En este caso, la biblioteca NLTK (Natural Language Toolkit) proporciona una función que utiliza un enfoque basado en reglas para analizar el sentimiento de un texto.
El analizador de sentimientos de NLTK asigna puntajes a diferentes aspectos del texto, como las palabras y las frases, y luego combina estos puntajes para calcular un puntaje de sentimiento compuesto. Este puntaje compuesto oscila entre -1 y 1, donde los valores cercanos a 1 indican un sentimiento positivo, los valores cercanos a -1 indican un sentimiento negativo y los valores cercanos a 0 indican un sentimiento neutral.

<h4>Fase 2:</h4> 
Localización Estratégica de Nuevos Establecimientos:<br>
Al incorporar el análisis de sentimiento, identificaremos las áreas geográficas ideales para establecer nuevos locales de restaurantes y negocios afines. Al comprender las preferencias y expectativas de los consumidores en diferentes ubicaciones, garantizaremos que nuestro cliente logre expandir su presencia en los mercados de manera inteligente.

<h4>Fase 3:</h4> 
Sistemas de Recomendación Inteligentes para Usuarios:<br>
Desarrollaremos un sistema de recomendación innovador para los usuarios de ambas plataformas. El mismo se basará en los resultados del análisis de sentimiento y en el perfíl del usuario, brindando a los mismos opciones a elección personalizadas que enriquecerán su experiencia al descubrir contenido relevante y emocionante que de otro modo podrían haber pasado por alto.

<h4>Fase 4:</h4> 
Recomendaciones Accionables e Informe Completo:<br>
Generaremos recomendaciones específicas y basadas en evidencia, respaldadas por nuestro análisis detallado. Completaremos nuestro proyecto con un informe exhaustivo que detalla cada fase del proceso, los resultados obtenidos y las recomendaciones propuestas, proporcionando un recurso invaluable para la toma de decisiones futuras.

<h2>Estados:</h2>
Hemos centrado nuestro análisis en los cinco estados con los valores más altos de PBI en los Estados Unidos. Estos datos fueron obtenidos utilizando técnicas de Web Scraping a través de la página de Wikipedia. Los estados elegidos son: <br><br>

[![states.jpg](https://i.postimg.cc/MZ0PVkZ4/states.jpg)](https://postimg.cc/Hjx91hy4)

California<br>
Texas<br>
New York<br>
Florida<br>
Illinois<br><br>
Cada uno de estos estados destaca por su alto PBI per cápita, lo que nos permite explorar patrones y tendencias económicas específicas.

<h2>KPIs</h2>
<h4>Tasa de Retención de Clientes:</h4>
Definición: Medir la proporción de clientes que han regresado a un negocio después de su primera visita.<br>
Fórmula: (Clientes que regresaron / Total de clientes) * 100<br>
Objetivo: Detectar tasas de retención de clientes superior al 70% para demostrar la capacidad del negocio en generar lealtad.<br><br>

<h4>Tasa de Crecimiento de Reseñas:</h4>
Definición: Medir el crecimiento porcentual de la cantidad de reseñas recibidas en un período de tiempo determinado. <br>
Fórmula: ((Cantidad de reseñas del periodo actual - Cantidad de reseñas del periodo anterior) / Cantidad de reseñas del periodo anterior) * 100. <br>
Objetivo: Identificar el crecimiento en la cantidad de reseñas recibidas, lo que puede indicar el nivel de participación y la satisfacción de los clientes con el negocio. Un aumento constante en las reseñas puede ser un indicador de una mayor visibilidad y reputación en línea. <br><br>

<h4>Variación Porcentual del Promedio del Puntaje:</h4>
Definición: Evaluar cómo varían los puntajes promedio de las categorías de servicio de un mes a otro.<br>
Fórmula: ((Puntaje promedio del periodo actual - Puntaje promedio del periodo anterior) / Puntaje promedio del periodo anterior) * 100.<br>
Objetivo: Identificar tendencias de mejora o declive en la calidad de los distintos tipos de servicios.<br><br>

<h4>Variación Porcentual del Promedio del Indice de Sentimiento:</h4>
Definición: Evalua la distribucion de la variación en el promedio del indice de sentimiento de las reseñas.<br>
Fórmula: ((Promedio del Indice de Sentimiento del periodo actual - Promedio del Indice de Sentimiento del periodo anterior) / Promedio del Indice de Sentimiento del periodo anterior) * 100.<br>
Objetivo: Identificar cambios en la percepción de los usuarios en diferentes categorías y estados.<br><br>


<h2>Recopilación y Fuentes de Datos</h2>
Datos Estáticos de Google Maps (Henry)<br>
Datos Estáticos de Yelp (Henry)<br>
Datos de Web Scraping (Wikipedia)

<h2>Stack tecnológico</h2>

[![stack-tecnologico.jpg](https://i.postimg.cc/ryRG7jyq/stack-tecnologico.jpg)](https://postimg.cc/5j1FCwFr)
Git: Sistema de control de versiones distribuido, para el seguimiento de cambios en el código fuente<br>
Github: Alojamiento de nuestro repositorio<br>
Visual Studio Code: Software para trabajar de forma local en el proyecto<br>
Google Drive: Servicio de Google para alma de forma provisoria nuestros archivos<br>
AWS: Plataforma de computación en la nube que ofrece una amplia gama de servicios de infraestructura y aplicaciones en la nube<br>
Airflow: Plataforma para automatización de flujos de trabajo<br>
Python: Lenguaje de programación usado para ciencia de datos<br>
Pandas: Librería escrita para el lenguaje Python para la manipulación y el análisis de datos<br>
Spark: Marco de procesamiento de datos en clúster de grandes volumenes de datos<br>
PySpark: Interfaz de programación en Python para Apache Spark<br>
Koalas: Librería que combina la simplicidad de Pandas con el poder de Spark<br>
Matplotlib: Librería en Python para crear visualizaciones de nuestros datos<br>
Seaborn: Librería de visualización de datos de Python basada en matplotlib<br>
Scikit-learn: Librería de aprendizaje automático de código abierto para el lenguaje de programación Python<br>
TensorFlow: Biblioteca de aprendizaje automático y redes neuronales<br>
NLTK: Librería para el procesamiento del lenguaje natural especializada en textos <br>

<h2>Aclaración:</h2>
Es fundamental comprender que éste proyecto tiene un enfoque educativo, simulando un ambiente laboral real para abordar diversas temáticas de manera didáctica. Los resultados y conclusiones obtenidos en el mismo no deben considerarse como base para tomar decisiones reales. 