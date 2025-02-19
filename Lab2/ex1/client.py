import Pyro4

def main():
    # 1. (Optional) Configure the Name Server host and port if they are not the defaults.
    Pyro4.config.NS_HOST = "localhost"  # Change if your name server is running elsewhere.
    Pyro4.config.NS_PORT = 9090         # Change if using a different port.
    
    # 2. Retrieve the remote object using its name in the Name Server.
    echo_server = Pyro4.Proxy("PYRONAME:echo.server")
    
    # 3. Call the remote method 'echo' with the message "HOLA".
    response = echo_server.echo("HOLA")
    
    # 4. Print the response received from the server.
    print("Response from server:", response)

if __name__ == '__main__':
    main()
