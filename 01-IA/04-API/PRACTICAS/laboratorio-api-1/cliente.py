import requests

def consultar_api():
    # URL donde está corriendo tu API de Flask
    url = "http://127.0.0.1:5000/procesar"
    
    print("--- Cliente de la API de Procesamiento ---")
    # Pedimos el texto al usuario por consola
    oracion_usuario = input("Ingresa una oración para analizar: ")
    
    # Validamos que no esté vacía
    if not oracion_usuario.strip():
        print("No ingresaste ningún texto.")
        return

    # Armamos el paquete de datos (el diccionario que se convertirá en JSON)
    datos = {"oracion": oracion_usuario}
    
    print("\nEnviando datos a la API...")
    
    try:
        # Hacemos la petición POST enviando los datos como JSON
        respuesta = requests.post(url, json=datos)
        
        # Si la API responde con un código de éxito (200)
        if respuesta.status_code == 200:
            # Convertimos la respuesta JSON en un diccionario de Python
            resultado = respuesta.json()
            
            # Mostramos los datos bien formateados y limpios
            print("\n========================================")
            print("         RESULTADO DE LA API            ")
            print("========================================")
            print(f"Texto original:   {resultado['oracion_original']}")
            print(f"Texto en MAYUS:   {resultado['oracion_mayuscula']}")
            print(f"Total palabras:   {resultado['cantidad_palabras']}")
            print("========================================")
        else:
            print(f"\nError en la API. Código de estado: {respuesta.status_code}")
            print(respuesta.json())
            
    except requests.exceptions.ConnectionError:
        print("\n[ERROR] No se pudo conectar con la API.")
        print("¿Asegúrate de que 'app.py' se está ejecutando en otra terminal?")

if __name__ == "__main__":
    consultar_api()
