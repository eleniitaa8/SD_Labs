# InsultProducer.py
import redis
import time

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
queue_name = "insult_queue"

# Lista de insultos de ejemplo
insults = [
    "Eres tan tonto como un zapato.",
    "Tu inteligencia ilumina la habitación... cuando se apaga la luz.",
    "Si la estupidez doliera, tú estarías en coma.",
    "No eres la persona más brillante del barrio."
]

print("InsultProducer iniciado. Enviando insultos cada 5 segundos...")

while True:
    for insult in insults:
        client.rpush(queue_name, insult)
        print(f"InsultProducer produced: {insult}")
        time.sleep(5)
