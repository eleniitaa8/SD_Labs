# Redis1.py
import redis

# Conectar al servidor Redis en localhost:6379, usando la base de datos 0
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Establecer un par clave-valor ("name": "Alice")
client.set("name", "Alice")

# Obtener el valor asociado a la clave "name"
name = client.get("name")
print(f"Retrieved value: {name}")

# Borrar la clave "name"
client.delete("name")

# Verificar si la clave "name" sigue existiendo
exists = client.exists("name")
print(f"Does 'name' exist? {'Yes' if exists else 'No'}")
