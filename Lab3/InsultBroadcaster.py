# InsultBroadcaster.py
import redis
import time

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
channel_name = "insult_channel"
insults_list_key = "INSULTS"

print("InsultBroadcaster iniciado. Publicando insultos en el canal pubsub...")

last_count = 0  # Lleva la cuenta de cuántos insultos ya se han publicado

while True:
    # Obtener todos los insultos de la lista "INSULTS"
    insults = client.lrange(insults_list_key, 0, -1)
    # Si hay nuevos insultos (más que la cuenta anterior)
    if len(insults) > last_count:
        new_insults = insults[last_count:]
        for insult in new_insults:
            client.publish(channel_name, insult)
            print(f"InsultBroadcaster published: {insult}")
        last_count = len(insults)
    time.sleep(5)
