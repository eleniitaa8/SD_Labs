# InsultReceiver.py
import redis

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
channel_name = "insult_channel"

pubsub = client.pubsub()
pubsub.subscribe(channel_name)
print(f"InsultReceiver suscrito al canal {channel_name}, esperando insultos...")

for message in pubsub.listen():
    if message["type"] == "message":
        print(f"InsultReceiver received: {message['data']}")
