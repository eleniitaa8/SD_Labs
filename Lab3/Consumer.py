# Consumer.py
import redis

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
queue_name = "task_queue"

print("Consumer is waiting for tasks...")

while True:
    # BLPOP bloquea hasta que hay un elemento en la cola
    task = client.blpop(queue_name, timeout=0)
    if task:
        print(f"Consumed: {task[1]}")
