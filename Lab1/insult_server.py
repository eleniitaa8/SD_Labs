# insult_server.py
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import random

# Lista de insultos inicial
insults = [
    "Tonto",
    "Feo",
    "You're the reason they put directions on shampoo bottles.",
    "Tolai"
]

# Lista de suscriptores (se almacenan sus URLs, por ejemplo "http://localhost:8001")
subscribers = []

def add_insult(insult):
    # Agrega un insulto y notifica a todos suscriptores
    insults.append(insult)
    notify_subscribers(insult)
    return f'Insulto agregado: {insult}'

def get_insults():
    # Devuelve la lista de insultos
    return insults

def insult_me():
    # Devuelve un insulto aleatorio
    return random.choice(insults)

def add_subscriber(subscriber_url):
    # Registra un suscriptor (observer)
    # Se debe pasar la URL del servidor suscriptor
    subscribers.append(subscriber_url)
    return f'Suscriptor agregado: {subscriber_url}'

def notify_subscribers(new_insult):
    # Notifica a cada suscriptor que se le pasó la URL del servidor observador.
    # Llama al método notify del suscriptor para pasarle el nuevo insulto.
    for sub_url in subscribers:
        try:
            print(f'Notificando a {sub_url} sobre el insulto: {new_insult}')
            proxy = xmlrpc.client.ServerProxy(sub_url, allow_none=True)
            proxy.notify(new_insult)
        except Exception as e:
            print(f"Error al notificar al suscriptor {sub_url}: {e}")

def run_server():
    # Configuramos el servidor en localhost en el puerto 8000.
    # Si el servidor debe ser accesible desde otras máquinas, cambia 'localhost' por la IP adecuada o '0.0.0.0'.
    server = SimpleXMLRPCServer(('localhost', 8000), allow_none=True)
    print("Servidor de Insultos ejecutándose en el puerto 8000...")
    
    # Registramos las funciones disponibles vía XML-RPC.
    server.register_function(add_insult, 'add_insult')
    server.register_function(get_insults, 'get_insults')
    server.register_function(insult_me, 'insult_me')
    server.register_function(add_subscriber, 'add_subscriber')
    
    # Ejecuta el servidor de forma indefinida.
    server.serve_forever()

if __name__ == '__main__':
    run_server()
