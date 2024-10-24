#  Informe de Avances del Proyecto de Investigación 
 
Nuestro proyecto se centra en el análisis de una base de datos de tweets relacionados con el debate sobre el aborto en Argentina. La base fue recolectado por Pablo Celayes. Estos tweets fueron recolectados utilizando una serie de hashtags que inicialmente parecían reflejar las principales posturas sobre el tema. Los hashtags utilizados para la recolección incluyen:

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
2. Generamos dos nuevas columnas: "mención" y "retweet".
La primera columna, "mención", extrae el `screen_name` de los usuarios que han sido mencionados en el tweet, ya sea de manera intencional o a través de un retweet. La segunda columna, "retweet", es de tipo booleano y señala si el tweet es un retweet o no.
3. Leemos la base de datos aborto_junio_users.csv para extraer la identidad del screen_name, y así generar una nueva columna ‘user_name_mencion’. Filtramos los tweets y seleccionamos aquellos que han sido retuiteado más de 5 veces. La columna ‘user_name’ contiene quien lo retuitió y la columna ‘user_name_mencion’ tiene el nombre del usuario que escribió el tweet original o quien fue mencionado.
Construimos el grafo donde los nodos son los nombres de los usuarios que aparecen tanto en columnas user_name como en user_name_mencion. Los nodos van estar conectados si ha habido interaccion entre ellos,ya sea un retweet o una mención.

Aplicamos el algoritmo de Louvain con escalado progresivo de la resolución con valores Ninguna, 0, 1, 2 y 3. La resolución óptima obtenida fue Ninguna.
Obtenemos 77 comunidades, donde las 5 primeras (0, 1, 2, 3 Y 19)  acumulan el 73% de las observaciones (por qué cambian las comunidades cada vez que lo corremos)
Analizamos la distribucion de los grado de centralidad de cada usuario en cada comunidad. Observamos que muchos de los usuarios tenían muy bajos grados de centralidad, por lo tanto reducimos a la mitad cantidad de nodos, quedándonos con aquellos que tenían mayor grado de centralidad
Exportamos la base de datos con las comunidades para luego hacer una selección aleatoria de 20 tweets dentro de las 5 comunidades para hacer una evaluación anecdótica. 
Al hacer lla matriz de confusión comunidad vs. posición, obtenemos que la comunidad 0,1, 3 y 19, corresponden a la posición ‘si’; la comunidad 2 a la posición ‘no’. Asumiendo que esta asociación entre posiciones y comunidades es correcta, agrupamos las primeras comunidades mencionadas para formar una única (comunidad 2).La comunidad 2 fue llamada comunidad 0 
De todos los usuarios mas influyentes que hemos seleccionado, la comunidad 0 representa el 65% de los usuarios, por lo tanto la comunidad 1 el 35%.


   

