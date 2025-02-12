# insult_client.py
import xmlrpc.client
import time

def run_client():
    # Conecta con el Insult Server (en este ejemplo, en localhost:8000)
    server_url = "http://localhost:8000"
    insult_server = xmlrpc.client.ServerProxy(server_url, allow_none=True)
    
    # Lista de insultos a enviar
    insults_to_send = [
        "You're as bright as a black hole!",
        "Your mind is on vacation but your mouth is working overtime.",
        "If I wanted to hear from an idiot, I'd ask you to speak.",
        "You are proof that evolution can go in reverse."
    ]
    
    index = 0
    while True:
        insult = insults_to_send[index % len(insults_to_send)]
        print(f"Enviando insulto: {insult}")
        response = insult_server.add_insult(insult)
        print(response)
        index += 1
        time.sleep(3)

if __name__ == '__main__':
    run_client()
