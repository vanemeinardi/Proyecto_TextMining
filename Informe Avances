#  Informe de Avances del Proyecto de Investigación 
 
Nuestro proyecto se centra en el análisis de una base de datos de tweets relacionados con el debate sobre el aborto en Argentina. Estos tweets fueron recolectados utilizando una serie de hashtags que inicialmente parecían reflejar las principales posturas sobre el tema. Los hashtags utilizados para la recolección incluyen:

- A favor del aborto legal:
  - `#abortolegal`, `#abortolegalya`, `#abortolegalesvida`, `#AbortoLegalEsSalud`, `#novotencontralasmujeres`, `#quesealey`, `#queelabortosealey`, `#AbortoSeraLey`

- En contra del aborto:
  - `#elijamoslas2vidas`, `#noalaborto`, `#noalabortolegal`, `#salvemoslasdosvidas`, `#SalvemosLas2Vidas`, `#ArgentinaEsProvida`, `#CuidemoslasDosVidas`, `#AbortoLegalEsMuerte`, `#NoAlAbortoEnArgentina`

Sin embargo, debido a la ambigüedad con la que los hashtags pueden ser usados (por ejemplo, de manera irónica o contradictoria), hemos decidido no emplearlos directamente para clasificar las posturas. En su lugar, aplicaremos técnicas avanzadas de detección de comunidades y análisis de tópicos para identificar de forma más precisa los grupos de usuarios y los temas que emergen en la discusión. Esto nos permitirá entender mejor las dinámicas y los principales enfoques presentes en el debate sin depender únicamente de los hashtags.

A continuación, se presentan los códigos utilizados en el proyecto, junto con una explicación detallada de su función:
0.1-crear-dataframes.ipynb
En este código leemos las bases de datos aborto_junio_tweets.csv, que contiene tweets comprendidos en el  
Una vez leídos ambos archivos, generamos nuevas bases para cada archivo con columnas de interés: retweet_count, full_text, user_name y user_id. Para la base de junio seleccionamos la columna posicion, ya que la de agosto no contaba con la misma.
Las nuevas bases las llamos tweets_junio_procesado.csv y tweets_agosto_procesado.csv.

