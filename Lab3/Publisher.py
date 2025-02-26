# Publisher.py
import redis
import time

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
channel_name = "news_channel"

messages = [
    "Breaking News: Market hits new high!",
    "Weather Update: Heavy rain expected",
    "Sports: Local team wins championship"
]

for message in messages:
    client.publish(channel_name, message)
    print(f"Published: {message}")
    time.sleep(2)  # Simula un retardo entre mensajes
