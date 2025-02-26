# InsultConsumer.py
import redis

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
queue_name = "insult_queue"
insults_list_key = "INSULTS"

print("InsultConsumer iniciado. Esperando insultos en la cola...")

while True:
    # BLPOP bloquea hasta que se recibe un insulto
    task = client.blpop(queue_name, timeout=0)
    if task:
        insult = task[1]
        # Recupera los insultos actuales de la lista "INSULTS"
        current_insults = client.lrange(insults_list_key, 0, -1)
        if insult not in current_insults:
            # Agrega el insulto a la lista si es nuevo (usando RPUSH para mantener el orden)
            client.rpush(insults_list_key, insult)
            print(f"InsultConsumer: Nuevo insulto agregado: {insult}")
        else:
            print(f"InsultConsumer: Insulto ya existente, ignorado: {insult}")
