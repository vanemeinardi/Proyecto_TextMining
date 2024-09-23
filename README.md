# Explorando la Narrativa del Aborto: Análisis de Posturas a través de NLP

**Resumen**: 
En este trabajo, se propone utilizar la estructura de comunidades en redes sociales para asignar posturas a los tuits , desarrollando una solución automatizada para detectar posturas a favor y en contra de la Interrupción Voluntaria del Embarazo en Twitter. Este análisis se fundamenta en datos relacionados con el tratamiento del proyecto en las cámaras de Diputados y Senadores de Argentina durante 2018. Se empleará un dataset, obtenido y preprocesado por Pablo Celayes, que incluye tuits recogidos en torno a fechas clave del tratamiento, utilizando hashtags relevantes.

Para detectar comunidades, utilizaremos el algoritmo de Louvain para  la maximización de la modularidad (Gach y Hao 2013). Se esta apuntando a  las dos comunidades
más grandes que se encuentren , porque estamos asumiendo posiciones binarias (a
favor - en contra) en las instancias.  Se realizará una evaluación anecdótica mediante la anotación de tuits para verificar la correspondencia entre las comunidades detectadas y las posturas.

Se implementará el modelo LDA (Latent Dirichlet Allocation) para detectar tópicos y se analizará su alineación con las posturas identificadas. Finalmente, se desarrollarán dos clasificadores que utilizarán las comunidades como clases, considerando características textuales, estructurales y conversacionales, así como los tópicos identificados.

