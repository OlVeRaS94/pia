from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/saludo/<nombre>', methods=['GET'])
def saludar(nombre):
    return jsonify({"mensaje": f"Hola, {nombre}"})

if __name__ == '__main__':
    app.run(debug=True)

# Consumir la API (en otro script):
import requests
response = requests.get('http://localhost:5000/saludo/Mundo')
print(response.json())