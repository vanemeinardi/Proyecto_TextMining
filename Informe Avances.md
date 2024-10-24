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
   - 
3. **`user_name`:**  Es el nombre de usuario del autor del tweet.  
   

4. **`user_id`:**  Es un identificador único que Twitter asigna a cada usuario.  
   -

5. **`posicion`:**   Indica la postura o posición del tweet respecto al tema del aborto, con base a los hashtags. 
   

