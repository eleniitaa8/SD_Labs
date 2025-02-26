# InsultFilter.py
import redis
import re

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
queue_name = "text_queue"
results_list_key = "RESULTS"
insults_list_key = "INSULTS"

print("InsultFilter iniciado. Procesando textos de la cola...")

while True:
    task = client.blpop(queue_name, timeout=0)
    if task:
        text = task[1]
        # Recuperar la lista de insultos actual
        insults = client.lrange(insults_list_key, 0, -1)
        filtered_text = text
        # Reemplazar cada insulto encontrado por "CENSORED"
        for insult in insults:
            filtered_text = re.sub(re.escape(insult), "CENSORED", filtered_text, flags=re.IGNORECASE)
        # Almacenar el texto filtrado en la lista "RESULTS"
        client.rpush(results_list_key, filtered_text)
        print(f"InsultFilter processed text: {filtered_text}")
