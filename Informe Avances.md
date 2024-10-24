#  Informe de Avances del Proyecto de Investigación 
 
Nuestro proyecto se centra en el análisis de una base de datos de tweets relacionados con el debate sobre la sanción de la ley del aborto en Argentina. La base fue recolectado por Pablo Celayes. Estos tweets fueron recolectados utilizando una serie de hashtags que inicialmente parecían reflejar las principales posturas sobre el tema. Los hashtags utilizados para la recolección incluyen:

- A favor del aborto legal:
  - `#abortolegal`, `#abortolegalya`, `#abortolegalesvida`, `#AbortoLegalEsSalud`, `#novotencontralasmujeres`, `#quesealey`, `#queelabortosealey`, `#AbortoSeraLey`

- En contra del aborto:
  - `#elijamoslas2vidas`, `#noalaborto`, `#noalabortolegal`, `#salvemoslasdosvidas`, `#SalvemosLas2Vidas`, `#ArgentinaEsProvida`, `#CuidemoslasDosVidas`, `#AbortoLegalEsMuerte`, `#NoAlAbortoEnArgentina`

Sin embargo, debido a la ambigüedad con la que los hashtags pueden ser usados (por ejemplo, de manera irónica o contradictoria), hemos decidido no emplearlos directamente para clasificar las posturas. En su lugar, aplicaremos técnicas avanzadas de detección de comunidades y análisis de tópicos para identificar de forma más precisa los grupos de usuarios y los temas que emergen en la discusión. Esto nos permitirá entender mejor las dinámicas y los principales enfoques presentes en el debate sin depender únicamente de los hashtags.

A continuación, se presentan los códigos utilizados en el proyecto, junto con una explicación detallada de su función:

## 0.1-crear-dataframes.ipynb
Leemos las bases de datos aborto_junio_tweets.csv, que contiene tweets comprendidos en el mes de junio.  
Filtramos la base por las  columnas de interés: retweet_count, full_text, user_name y user_id, posicion. 

1. **`retweet_count`:**  Esta columna indica el número de veces que un tweet ha sido retuiteado.  
2. **`full_text`:**   Contiene el texto completo del tweet.  
3. **`user_name`:**  Es el nombre de usuario del autor del tweet.  
4. **`user_id`:**  Es un identificador único que Twitter asigna a cada usuario.  
5. **`posicion`:**   Indica la postura o posición del tweet respecto al tema del aborto, con base a los hashtags.
6. Exportamos la base de taos como tweets_junio_procesado.csv para luego usarla en el siguiente código.

## 02.Deteccion_comunidades.ipynb
1. Leemos la base de datos tweets_junio_procesados.csv.
2. Generamos dos nuevas columnas: mención y retweet.
La primera columna, **mención**, extrae el `screen_name` de los usuarios que han sido mencionados en el tweet, ya sea de manera intencional o a través de un retweet. La segunda columna, **retweet**, es de tipo booleano y señala si el tweet es un retweet o no.
3. De la base de datos datos aborto_junio_users.csv vamos a extraer la identidad del screen_name, y así generar una nueva columna **user_name_mencion**.
4.  Cremamos un nuevo dataframe llamado df_pares_filtrados que incluye las columnas **user_name**, **user_name_mencion**, **full_text** y **posicion** y seleccionamos únicamente los tweets que han sido retuiteado más de 5 veces. 
5. Construimos un grafo a partir de las columnas de la tabla df_pares_filtrados, donde los nodos representan los nombres de los usuarios que aparecen en las columnas **user_name** y **user_name_mencion**
6. Los nodos estarán conectados si ha habido interacción entre ellos, ya sea a través de un retweet o una mención; en este caso, las aristas corresponden a las filas de la tabla
7. Aplicamos el algoritmo de Louvain con escalado progresivo de la resolución con valores Ninguna,  1, 2 y 3. La resolución óptima obtenida fue Ninguna.
8. Obtenemos 92 comunidades, donde las 5 primeras (0, 1, 2, 3 Y 19)  acumulan el 72% de las observaciones.
9. Volvemos a calcular las particiones por comunidades utilizando una resolución de `None` en el DataFrame `filtered_comunidades`, que incluye únicamente a los usuarios de las 5 comunidades más grandes. Además, incorporamos el grado de centralidad para identificar los nodos más conectados dentro de cada comunidad.
10. Observamos que muchos presentaban valores bajos en este indicador. Para optimizar el análisis, probamos reducir el número de nodos con los grados de centralidad más altos, evaluando reducciones del 50%, 25% y 15%. Al notar que la disminución de observaciones no era significativa en las distintas pruebas realizadas, decidimos quedarnos con la reducción del 15%.
12.  De las comunidades obtenidas, queremos determinar las posturas. Para ello, construimos la tabla  comunidades_completo.csv (filtrando las observaciones que quedaron del punto anterior).
13.  Como una primera medida de las comunidades hacemos la matriz de confusion entre posturas obtenemos que la comunidad 0,1, 3 y 19, podría asociarse a la posición ‘si’; la comunidad 2 a la posición ‘no’.
14. Extraemos aleatoriamente 20 tweets de cada comunidad. Este proceso nos permitirá evaluarlos de manera anecdótica y, posteriormente, elaborar la matriz de confusión que compare nuestras evaluaciones con las comunidades.
15. Hacemos la matriz de confusion entre la evaluacion anecdotica, y obtenemos que la comunidad 0,1, 3 y 19, podría asociarse a la posición ‘si’; la comunidad 2 a la posición ‘no’. 
16. Definimos una nueva variable llamada postura que asignamos la categoría si a los tweets que estan en las comunidades 0,1, 3 y 19 y no a los tweets que estan en la comunidad 2. Exportamos la base como 'comunidades.csv'.

## 0.2.1 obtencion_caractesticas_comunidades.ipynb
Extraemos características de los tweets que puedan ser utilizadas como variables explicativas en modelos de clasificación, donde la variable dependiente a predecir son las comunidades a las que pertenecen los usuarios. Para ello
1. Leemos la base de datos 'comunidades.csv'.  
2. Obtenemos las características estructurales de los tweets:   
   **`Question Mark`:** Indica si el tweet contiene al menos un signo de interrogación (¿ o ?).  
   **`Question Mark Count`:** Cuenta el número total de signos de interrogación.  
   **`Starts with Question Mark`:** Indica si el tweet comienza con un signo de interrogación.  
   **`Ends with Mark Count`:** Indica si el tweet termina con un signo de interrogación.  
   **`Upper Ratio`:** Proporción de letras en mayúsculas sobre el total de letras en el tweet.  
   **`Exclamation Mark`:** Indica si el tweet contiene al menos un signo de admiración (¡ o !).  
   **`Exclamation Mark Count`:**  Cuenta el número total de signos de admiración en el tweet.  
   **`Ellipsis Occurrence`:**  Indica si el tweet contiene tres o más puntos seguidos ("...").  
   **`Hashtag Presence`:** Indica si el tweet incluye hashtags.  
   **`Text Length`:** Largo del texto del tweet después de eliminar menciones, URLs y hashtags.  
   **`URL Count`:** Cuenta el número de URLs incluidas en el tweet.  
   **`Quotes`:** Indica si el tweet contiene palabras entre comillas.  
3. Exportamos la base con las caracteristicas como 'Caracteristicas_comunidades.csv'.  
4. Identificamos los unigramas más distintivos de cada comunidad para usarlas como características:  
   4.1. Pre-Procesamos todos los tweets del dataset con un stemmer (de scikit-learn) en español quitando hashtags, nombres de usuario y urls. Obteniendo el DataFrame 'df_preproces'.   
   4.2. Convertimos los tweets en vectores usando tfidf vectorizer y los utilizamos para entrenar una regresión logística, alcanzando un accuracy de 0.89.  
   4.3. Una vez entrenado el modelo, tomamos las 20 palabras con coeficientes de mayor peso en valor absoluto y cramos un nuevo vectorizador solo con esas palabras.  
   4.4.  Ajustamos el vectorizador personalizado a los tweets originales para crear nuevas características con estas palabras, y lo añadimos al DataFrame df_preproces. Lo exportamos como 'df_unigramas.csv'.    
     
## 0.3 LDA.ipynb   
Vamos a aplicar el modelo LDA (Latent Dirichlet Allocation) para detectar tópicos presentes en los tweets, con el objetivo de utilizarlos como posibles posturas.
1. Leemeos la base de datos 'tweets_junio_procesado.csv'.
2. Limpiamos la base:  
   2.1.  Eliminamos aquellos tweets que estaban recortados, ya que durante los experimentos con LDA introducían ruido y afectaban negativamente los resultados. Exportamos la nueva tabla como 'tweets_junio_recortados.csv'.   
   2.2. Eliminamos URLs, menciones de usuarios y el símbolo de numeral (#) en los hashtags, manteniendo únicamente el texto. La eliminacion completa de los hashtags empeoraban la deteccion de tópicos, por lo tanto fueron conservados.  
   2.3. Eliminamos de puntuación, RT (retweets) y stopwords.
   2.4. Convertimos todo el texto  de los tweets a minúsculas.  
3. Para mejorar la detección de tópicos en los tweets, balanceamos los datos mediante un submuestreo de la clase mayoritaria. Esto permitió una mejor identificación de tópicos, ya que inicialmente, al aplicar LDA, predominaban palabras relacionadas con la postura 'sí'.
4. Aplicamos CountVectorizer, donde el min_df=10000 (solo se consideraron palabras que aparecían al menos 10.000 veces) y max_df=0.99 (se excluyeron palabras que aparecían en más del 99% de los tweets).
5. Ajuste del modelo LDA:  
   5.1. Entrenamos el modelo LDA sobre el conjunto balanceado con 2 tópicos. Este número fue elegido tras realizar varias pruebas con distintos valores de tópicos.
   5.2. Utilizamos el modelo entrenado para predecir los tópicos en el conjunto completo de tweets_junio_recortados.  
   5.3. Realizamos la matriz de confusión La matriz entre los tópicos identificados por LDA y las posturas, obteniendo que el tópico 0 se correspondía en un 79% con la postura 'si' y el tópico 1 se correspondía en un 80% con la postura 'no'.
   
## Cronograma de trabajo
- Construcción de  características textuales, estructurales y conversacionales (semana del 28/10).  
- Aprender dos clasificadores de stance usando comunidades como clases y usando tópicos como clases (Todo el mes de noviembre).  

