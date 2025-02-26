# Producer.py
import redis
import time

client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
queue_name = "task_queue"

# Lista de tareas a enviar
tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6"]

for task in tasks:
    client.rpush(queue_name, task)
    print(f"Produced: {task}")
    time.sleep(1)  # Simula un retardo en la producción de tareas
