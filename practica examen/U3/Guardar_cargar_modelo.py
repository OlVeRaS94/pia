# Guardar modelo
modelo.save('modelo_mnist.h5')

# Cargar modelo
modelo_cargado = tf.keras.models.load_model('modelo_mnist.h5')

# Ejemplo de predicción
imagen_ejemplo = X_test[0].reshape(1, -1)
prediccion = modelo_cargado.predict(imagen_ejemplo)
print("Clase predicha:", np.argmax(prediccion))