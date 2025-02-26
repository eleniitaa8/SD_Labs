# AngryPublisher.py
import redis
import time

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
queue_name = "text_queue"

texts_with_insults = [
    "Eres tan tonto como un zapato, y la vida es una broma.",
    "Tu inteligencia ilumina la habitación, pero no ilumina tu futuro.",
    "No solo fallas en todo, sino que además eres un desastre."
]

print("AngryPublisher iniciado. Enviando textos con insultos cada 3 segundos...")

while True:
    for text in texts_with_insults:
        client.rpush(queue_name, text)
        print(f"AngryPublisher produced: {text}")
        time.sleep(3)
