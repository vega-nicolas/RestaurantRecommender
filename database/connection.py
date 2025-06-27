from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError

try:
    client = MongoClient(
        "mongodb://localhost:27017/",
        serverSelectionTimeoutMS=5000
    )
    client.server_info()
    print("Conexión a MongoDB establecida exitosamente")

except ConnectionFailure as e:
    print(f"Error: No se pudo conectar a MongoDB. Detalle: {e}")
    raise Exception("No se pudo conectar a MongoDB. Verifica que el servidor esté corriendo.")
except ConfigurationError as e:
    print(f"Error: Configuración de MongoDB incorrecta. Detalle: {e}")
    raise Exception("Configuración de MongoDB inválida. Revisa la URI o las credenciales.")
except Exception as e:
    print(f"Error inesperado al conectar a MongoDB: {e}")
    raise Exception("Error inesperado al conectar a MongoDB.")

def close_connection():
    try:
        client.close()
        print("Conexión a MongoDB cerrada")
    except Exception as e:
        print(f"Error al cerrar la conexión a MongoDB: {e}")