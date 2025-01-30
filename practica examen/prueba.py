#pip install torch transformers

from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Cargar el modelo y el tokenizador
model_name = "gpt2"  # Usaremos GPT-2 como ejemplo (puedes usar "distilgpt2" si tienes poca RAM)
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Crear un pipeline de generación de texto
generator = pipeline(
    "text-generation", 
    model=model, 
    tokenizer=tokenizer,
    device=0 if model.device.type == "cuda" else -1  # Usa GPU si está disponible
)

# Función para generar texto (parámetros actualizados)
def generar_texto(prompt, max_length=100, temperature=0.7, num_return_sequences=1):
    output = generator(
        prompt,
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=num_return_sequences
    )
    return [result["generated_text"] for result in output]

# Interacción con el usuario
if __name__ == "__main__":
    print("Escribe 'salir' para terminar.\n")
    
    while True:
        prompt = input("Tú: ")
        
        if prompt.lower() == "salir":
            print("¡Adiós!")
            break
            
        respuestas = generar_texto(
            prompt,
            max_length=1000,
            temperature=0.2,  # Controla la creatividad (0 = conservador, 1 = creativo)
            num_return_sequences=2  # Número de respuestas generadas
        )
        
        # Mostrar todas las respuestas
        for i, respuesta in enumerate(respuestas, 1):
            print(f"\nIA (Respuesta {i}): {respuesta}\n")




    #Explicación del código
#Modelo y Tokenizador: Se carga un modelo preentrenado (en este caso, gpt2) junto con su tokenizador.

#Pipeline: Se crea un pipeline de generación de texto utilizando el modelo y el tokenizador.

#Generación de texto: La función generar_texto toma un prompt y genera texto basado en él.

#Consideraciones
#Hardware: Los modelos grandes como GPT-2 o GPT-3 pueden requerir una GPU para funcionar eficientemente. Si no tienes una GPU potente, podrías experimentar con modelos más pequeños o usar servicios en la nube.

#Modelos más grandes: Si tienes acceso a modelos más grandes como GPT-3 o GPT-4, puedes cambiar el model_name a uno de esos modelos, pero ten en cuenta que pueden requerir más recursos.

#Alternativas
#Si prefieres no manejar el modelo directamente, también puedes usar la API de OpenAI (si tienes acceso) para interactuar con modelos como GPT-3 o GPT-4 desde tu entorno local.

#¡Espero que esto te ayude a implementar un modelo de lenguaje en tu entorno local! Si tienes más preguntas, no dudes en preguntar.