import re
import pandas as pd
from PyPDF2 import PdfReader
import subprocess
import tempfile

def extraer_codigo_de_pdf(ruta_pdf):
    """
    Extrae bloques de código Python de un PDF.
    """
    with open(ruta_pdf, 'rb') as file:
        reader = PdfReader(file)
        texto = ""
        for pagina in reader.pages:
            texto += pagina.extract_text()
        
        # Busca bloques de código entre ```python ... ```
        bloques_codigo = re.findall(r'```python(.*?)```', texto, re.DOTALL)
        return [codigo.strip() for codigo in bloques_codigo if codigo.strip()]

def ejecutar_ejercicios(bloques_codigo):
    """
    Ejecuta cada bloque de código y captura los resultados.
    """
    for idx, codigo in enumerate(bloques_codigo, 1):
        print(f"\n--- Ejecutando Ejercicio {idx} ---")
        # Crear un archivo temporal para ejecutar el código
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode='w') as tmp:
            tmp.write(codigo)
            tmp_name = tmp.name
        
        # Ejecutar el código y capturar la salida
        try:
            result = subprocess.run(
                ['python', tmp_name],
                capture_output=True,
                text=True,
                check=True
            )
            print("✅ Ejecución exitosa:\n" + result.stdout)
        except subprocess.CalledProcessError as e:
            print("❌ Error durante la ejecución:\n" + e.stderr)
        finally:
            # Eliminar el archivo temporal
            subprocess.run(['rm', tmp_name])

if __name__ == "__main__":
    ruta_pdf = "tu_archivo.pdf"  # Cambia esto por tu PDF
    bloques_codigo = extraer_codigo_de_pdf(ruta_pdf)
    
    if not bloques_codigo:
        print("No se encontraron ejercicios de código en el PDF.")
    else:
        ejecutar_ejercicios(bloques_codigo)