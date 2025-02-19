import Pyro4

@Pyro4.expose
class MyRemoteObject(object):
    def greet(self, name):
        """Return a greeting for the given name."""
        return f"Hello, {name}!"

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

def main():
    # Create a Pyro daemon
    daemon = Pyro4.Daemon()

    # Locate the Name Server (must be running separately via: python -m Pyro4.naming)
    ns = Pyro4.locateNS()

    # Register the MyRemoteObject class with the daemon and obtain its URI.
    uri = daemon.register(MyRemoteObject)

    # Register the object with the Name Server under the name "example.remote.object"
    ns.register("example.remote.object", uri)

    # Print the URI so that you know the object is available.
    print("MyRemoteObject is ready. Object URI:", uri)

    # Enter the request loop to wait for incoming remote calls.
    daemon.requestLoop()

if __name__ == "__main__":
    main()
