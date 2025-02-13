#Cargamos librerías
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score
from sklearn.metrics import f1_score
import warnings
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import make_scorer, recall_score, confusion_matrix, accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
import time  # Importar la librería para medir el tiempo
# Desactivar todos los warnings temporalmente
warnings.filterwarnings("ignore")

tabla=pd.read_csv('/home/vmeinardi/Proyecto_NLP/Analisis_sentimiento_LDA.csv')
print(tabla.columns)

# Separar las características y la variable objetivo
X = tabla.drop(columns=['topico'])
y = tabla['topico']

# Seleccionar columnas numéricas, booleanas y categóricas
numericas = X.select_dtypes(include=[np.number])
booleanas = X.select_dtypes(include=[bool])
categoricas = X.select_dtypes(include=['object'])

# Crear un preprocesador para escalar y codificar las variables
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numericas.columns),
        ('bool', 'passthrough', booleanas.columns),
        ('cat', OneHotEncoder(), categoricas.columns)
    ]
)

# Función personalizada para calcular especificidad
def specificity_score(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    return tn / (tn + fp)

# Crear los scorers
scorers = {
    'sensitivity': make_scorer(recall_score),
    'specificity': make_scorer(specificity_score),
    'accuracy': make_scorer(accuracy_score),
    'f1_score': make_scorer(f1_score),
    'roc_auc': make_scorer(roc_auc_score)
}

# Crear el pipeline que combine el preprocesamiento y el modelo
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Definir el modelo y los parámetros a probar
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_leaf_nodes': [None, 2, 5, 7],
    'classifier__max_depth': [None, 10, 20, 30],
    'classifier__criterion': ["gini", "entropy"]
}

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Configurar la búsqueda en malla con múltiples métricas de scoring
grid_search = GridSearchCV(
    estimator=pipeline, param_grid=param_grid, cv=5,
    scoring=scorers, refit='f1_score', return_train_score=True, n_jobs=-1
)
# Añadir un callback para medir el tiempo de cada combinación de parámetros
start_time = time.time()  # Tiempo de inicio
# Ajustar el modelo
grid_search.fit(X_train, y_train)
end_time = time.time()  # Tiempo de fin
execution_time = end_time - start_time
# Guardar los resultados finales
results = grid_search.cv_results_
data = {
    'Parámetros': [f"n_estimators={params['classifier__n_estimators']}, "
                   f"max_leaf_nodes={params['classifier__max_leaf_nodes']}, "
                   f"max_depth={params['classifier__max_depth']}, "
                   f"criterion={params['classifier__criterion']}" for params in results['params']],
    'Mean Sensitivity': results['mean_test_sensitivity'],
    'Mean Specificity': results['mean_test_specificity'],
    'Mean Accuracy': results['mean_test_accuracy'],
    'Mean F1 Score': results['mean_test_f1_score'],
    'Mean AUC': results['mean_test_roc_auc']
}
results_df = pd.DataFrame(data)
# Redondear las métricas de la búsqueda en malla
results_df = pd.DataFrame(data)
results_df['Mean Sensitivity'] = results_df['Mean Sensitivity'].round(3)
results_df['Mean Specificity'] = results_df['Mean Specificity'].round(3)
results_df['Mean Accuracy'] = results_df['Mean Accuracy'].round(3)
results_df['Mean F1 Score'] = results_df['Mean F1 Score'].round(3)
results_df['Mean AUC'] = results_df['Mean AUC'].round(3)
results_df.to_csv("random_forest_results_analisis_sentimiento.csv", index=False)

# Ordenar el DataFrame por las métricas de interés
sorted_results = results_df.sort_values(by=['Mean Accuracy', 'Mean AUC', 'Mean Sensitivity'], ascending=False)

# Obtener la mejor combinación de hiperparámetros
best_params = grid_search.best_params_

# Reentrenar el modelo con los mejores hiperparámetros en los datos de entrenamiento
best_model = grid_search.best_estimator_

# Evaluar el modelo en los datos de prueba
y_pred_train = best_model.predict(X_train)
y_pred_test = best_model.predict(X_test)

# Redondear las métricas de entrenamiento y prueba
metrics_train = {
    'Accuracy': round(accuracy_score(y_train, y_pred_train), 4),
    'Sensitivity': round(recall_score(y_train, y_pred_train), 4),
    'Specificity': round(specificity_score(y_train, y_pred_train), 4),
    'F1 Score': round(f1_score(y_train, y_pred_train), 4),
    'ROC AUC': round(roc_auc_score(y_train, best_model.predict_proba(X_train)[:, 1]), 4)
}

metrics_test = {
    'Accuracy': round(accuracy_score(y_test, y_pred_test), 4),
    'Sensitivity': round(recall_score(y_test, y_pred_test), 4),
    'Specificity': round(specificity_score(y_test, y_pred_test), 4),
    'F1 Score': round(f1_score(y_test, y_pred_test), 4),
    'ROC AUC': round(roc_auc_score(y_test, best_model.predict_proba(X_test)[:, 1]), 4)
}
# Mostrar las métricas
print("Métricas de entrenamiento:", metrics_train)
print("Métricas de prueba:", metrics_test)
# Crear un DataFrame con las métricas
metrics_df = pd.DataFrame([metrics_train, metrics_test], index=['Entrenamiento', 'Prueba'])
metrics_df.to_csv("RF_best_parametros_analisis_sentimiento_LDA.csv")
# Mostrar tiempo total de ejecución
print(f"Tiempo total de ejecución para la búsqueda en malla: {execution_time:.2f} segundos")