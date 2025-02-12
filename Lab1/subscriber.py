# subscriber.py
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import time

def notify(new_insult):
    # Notificar nuevo insulto.
    print(f"Recibido nuevo insulto: {new_insult}")
    return f"Notificación recibida: {new_insult}"

def run_subscriber_server(port):
    server = SimpleXMLRPCServer(('localhost', port), allow_none=True)
    print(f"Suscriptor corriendo en el puerto {port}...")
    server.register_function(notify, 'notify')
    server.serve_forever()

def register_self_with_insult_server(port, insult_server_url="http://localhost:8000"):
    # Se conecta al Insult Server y se registra a sí mismo como suscriptor
    subscriber_url = f"http://localhost:{port}"
    time.sleep(1)
    try:
        proxy = xmlrpc.client.ServerProxy(insult_server_url, allow_none=True)
        response = proxy.add_subscriber(subscriber_url)
        print(f"Registro exitoso: {response}")
    except Exception as e:
        print(f"Error registrando el suscriptor: {e}")

def main():
    port = 8001  # Único puerto para suscriptor
    # Arrancamos el servidor del suscriptor en un hilo separado
    server_thread = threading.Thread(target=run_subscriber_server, args=(port,), daemon=True)
    server_thread.start()
    
    # Auto-registro en el Insult Server
    register_self_with_insult_server(port)
    
    # Mantenemos el hilo principal activo
    server_thread.join()

if __name__ == '__main__':
    main()
