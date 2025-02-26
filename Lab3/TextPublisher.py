# TextPublisher.py
import redis
import time

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
queue_name = "text_queue"

texts = [
    "Este es un texto sin insultos. Todo está bien.",
    "La vida es hermosa cuando no hay palabras hirientes.",
    "Disfruta de cada momento y mantén la calma."
]

print("TextPublisher iniciado. Enviando textos sin insultos cada 5 segundos...")

while True:
    for text in texts:
        client.rpush(queue_name, text)
        print(f"TextPublisher produced: {text}")
        time.sleep(5)
