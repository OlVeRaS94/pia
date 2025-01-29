from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar datos
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Entrenar modelo
modelo = LogisticRegression(max_iter=200)
modelo.fit(X_train, y_train)

# Evaluar
y_pred = modelo.predict(X_test)
print("Precisión:", accuracy_score(y_test, y_pred))
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))

# Respuesta conceptual: 
# SVM usa distancias entre puntos para calcular el hiperplano óptimo. Si las escalas de las características son diferentes, 
# las distancias estarán dominadas por las variables con mayor magnitud, lo que afecta el rendimiento del modelo.