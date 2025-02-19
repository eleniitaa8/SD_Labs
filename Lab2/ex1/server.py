import Pyro4

# 1. Expose the class so that its methods can be called remotely.
@Pyro4.expose
class TheEchoServer:
    def echo(self, msg):
        print("Server received message:", msg)
        return msg

def main():
    # 2. Create a Pyro daemon. The daemon is responsible for handling remote calls.
    daemon = Pyro4.Daemon()  
    
    # 3. Locate the Name Server. The Name Server keeps track of objects by name.
    ns = Pyro4.locateNS()  
    
    # 4. Register the TheEchoServer class instance with the daemon.
    uri = daemon.register(TheEchoServer)
    
    # 5. Register the object with the Name Server using the name "echo.server".
    ns.register("echo.server", uri)
    
    print("Echo server is ready.")
    
    # 6. Enter the request loop to wait for incoming remote method calls.
    daemon.requestLoop()

if __name__ == '__main__':
    main()
