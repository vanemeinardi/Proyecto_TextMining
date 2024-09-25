# Explorando la Narrativa del Aborto: Análisis de Posturas a través de NLP

**Resumen**: 
En este trabajo, se propone utilizar la estructura de comunidades en redes sociales para asignar posturas a los tuits , desarrollando una solución automatizada para detectar posturas a favor y en contra de la Interrupción Voluntaria del Embarazo en Twitter. Este análisis se fundamenta en datos relacionados con el tratamiento del proyecto en las cámaras de Diputados y Senadores de Argentina durante 2018. Se empleará un dataset, obtenido y preprocesado por Pablo Celayes, que incluye tuits recogidos en torno a fechas claves del tratamiento, utilizando hashtags relevantes.

**Objetivos Preliminares**
- Procesar la base de datos (Semana 25/09)
- Detectar comunidades y analizar si se corresponden con stances (Semanas 30/09 y 07/10)
- Detectar tópicos y analizar si se corresponden con stances (Semana 14-10)
- Construcción de  características textuales, estructurales y conversacionales (Semanas 21/10-28/10)
- Aprender dos clasificadores de stance usando comunidades como clases y usando tópicos como clases (Todo el mes de noviembre) 

**Técnicas que vamos a usar**

- Para detectar comunidades, utilizaremos el algoritmo de Louvain para la maximización de la modularidad.
- Se implementará el modelo LDA (Latent Dirichlet Allocation) para detectar tópicos.
- Pre-Procesar los ejemplos del dataset con un stemmer (de scikit-learn) en español quitando hashtags, nombres de usuario y urls.
- Convertir los tweets en vectores usando tfidf vectorizer
- Entrenar una regresión logística multi-clase para encontrar los unigramas más distintivos para cada clase.
- Entrenar con clasificadores XGBoosT y Regresion Logistica
- Búsqueda de hiperparámetros con Grid Search sobre los parámetros de interés con K-Fold Cross Validation (k=10)

**Referencias**
 - Furman et al. "You can simply rely on communities for a robust characterization of stances". 2021 (https://hal.science/hal-03260142)
 - Tesis de Grado Mariano Schmidt: " Explotando características contextuales para la detección de posturas en Twitter en el marco de la vacunación del COVID-19 en Argentina
 - Pamungkas et al. "Exploiting Affective Information and Conversation Structure, 2nd International Workshop on Rumours and Deception in Social Media (RDSM)". 2018 (https://arxiv.org/pdf/1901.01911.pdf)
 - Addawood et al. "Stance Classification of Twitter Debates: The Encryption Debate as A Use Case". 2017 ( http://hdl.handle.net/2142/96250)
 - Gach et al. "Improving the Louvain Algorithm for Community Detection with Modularity Maximization". 2014 (https://doi.org/10.1007/978-3-319-11683-9_12)

 **Evaluación**
 - Anécdotica para comparar comunidades y tópicos con stances
 - Precisión, Recall, F1-Score, Macro Avg para evaluar la performance de los clasificadores

  
  



