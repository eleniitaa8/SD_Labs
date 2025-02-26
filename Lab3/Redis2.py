# Redis2.py
import redis

# Conectar al servidor Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Insertar elementos en la lista "fruits" usando LPUSH (los añade al inicio)
client.lpush("fruits", "apple", "banana", "cherry")

# Recuperar todos los elementos de la lista "fruits"
fruits = client.lrange("fruits", 0, -1)
print(f"Fruits list: {fruits}")

# Extraer un elemento de la lista (RPOP extrae desde el final)
popped_fruit = client.rpop("fruits")
print(f"Popped fruit: {popped_fruit}")

# Obtener la lista actualizada
updated_fruits = client.lrange("fruits", 0, -1)
print(f"Updated fruits list: {updated_fruits}")

# Eliminar la lista "fruits"
client.delete("fruits")
