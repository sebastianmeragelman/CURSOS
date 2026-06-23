from flask import Flask, request, jsonify

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta de la API y el método (POST es ideal para enviar datos)
@app.route('/procesar', methods=['POST'])
def procesar_oracion():
    # Recibimos los datos en formato JSON
    datos = request.get_json()
    
    # Validamos que nos hayan enviado la oración
    if not datos or 'oracion' not in datos:
        return jsonify({'error': 'Por favor, proporciona una oración bajo la clave "oracion".'}), 400
    
    oracion_original = datos['oracion']
    
    # Procesamos la información
    en_mayusculas = oracion_original.upper()
    cantidad_palabras = len(oracion_original.split())
    
    # Armamos la respuesta en JSON
    respuesta = {
        'oracion_original': oracion_original,
        'oracion_mayuscula': en_mayusculas,
        'cantidad_palabras': cantidad_palabras
    }
    
    return jsonify(respuesta)

# Ejecutamos el servidor local
if __name__ == '__main__':
    app.run(debug=True)
