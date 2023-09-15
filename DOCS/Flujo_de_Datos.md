<h1 style="color:red"><center>Flujo de Datos</center></h1>

[![programador-de-tareas-ico.png](https://i.postimg.cc/JnsbhGj6/programador-de-tareas-ico.png)](https://postimg.cc/7GyCsPs0)



## Procesos de Almacenamiento, Transformación y Análisis de Datos

<h4>Datos en Archivo JSON:</h4> 
El proceso comienza con la adquisición de datos desde archivos JSON. Estos archivos contienen información cruda y desestructurada que requiere ser procesada y transformada en una forma más útil.

<h4>Optimización a Parquet:</h4> 
Para mejorar la velocidad de procesamiento y optimizar el espacio requerido de almacenamiento, los datos son convertidos al formato Parquet. Parquet es un formato de almacenamiento columnar que facilita el acceso y la consulta de datos de manera rápida y eficiente.

<h4>Almacenamiento en 'Data Lake' en AWS Amazon S3:</h4> 
Los datos optimizados se almacenan en un "Data Lake" en Amazon S3. Este es un repositorio escalable y seguro para el almacenamiento de datos en la nube. Permite la flexibilidad de acceso a los datos y su uso en diversas aplicaciones y procesos.

<h4>Scripts de Limpieza y Procesamiento con Spark y Python:</h4> 
Se aplican scripts y procesos de limpieza y procesamiento utilizando tecnologías como Spark y Python. Esto implica la transformación de datos, la eliminación de valores atípicos y la preparación de los datos para su análisis posterior.

<h4>'Data Warehouse' en AWS Amazon S3:</h4> 
Los datos procesados se almacenan en un "Data Warehouse" en Amazon S3. Este almacén centralizado permite un acceso rápido y estructurado a los datos para su análisis y generación de informes.

<h4>Ingeniería de Características con Spark y Python:</h4> 
Se lleva a cabo la ingeniería de características para crear variables relevantes y significativas que mejorarán el análisis y el rendimiento de los modelos.

<h4>Análisis, Reportes de KPIs y Dashboards con Power BI:</h4> 
Se utilizan herramientas como Power BI para el análisis exploratorio de datos, la generación de reportes de indicadores clave de rendimiento (KPIs) y la creación de dashboards interactivos que proporcionan información valiosa.

<h4>Modelos de Machine Learning:</h4> 
Se desarrollan modelos de aprendizaje automático utilizando los datos preparados. Estos modelos incluyen algoritmos de clasificación, regresión, agrupación y otros.

<h4>Pruebas y Comparaciones, Ajustes de Hiperparámetros, Modelos de Machine Learning y Predicciones:</h4> 
Esta etapa involucra la evaluación de modelos, la comparación de su rendimiento, la optimización de hiperparámetros y la realización de predicciones. Esta información alimenta tanto el análisis exploratorio como la ingeniería de características para un ciclo iterativo de mejora.

<h4>API y Renderizado con FastAPI y Render:</h4> 
Se desarrolla una API utilizando FastAPI para proporcionar acceso a los resultados del análisis y los modelos de machine learning. La API se conecta con la visualización y el renderizado de datos, lo que permite a los usuarios interactuar con los resultados a través de interfaces web amigables.


https://github.com/BrianMasat/PG_Google_Yelp/assets/129197307/1a640df5-2a53-4fc7-91e3-fe55bf376f3e