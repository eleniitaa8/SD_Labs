import Pyro4

@Pyro4.expose # Makes all methods accessible remotely
@Pyro4.behavior(instance_mode="single") # Ensures only one instance is used
class TheObservable(object):
    def __init__(self):
        # List to hold observer URIs
        self.observers = []

    def register_observer(self, observer_uri):
        """Register an observer by its remote URI."""
        print("Registering observer:", observer_uri)
        self.observers.append(observer_uri)

    def unregister_observer(self, observer_uri):
        """Unregister an observer by its remote URI."""
        print("Unregistering observer:", observer_uri)
        try:
            self.observers.remove(observer_uri)
        except ValueError:
            print("Observer not found:", observer_uri)

    def notify_observers(self, message):
        """Notify all registered observers with the given message."""
        print("Notifying observers with message:", message)
        for observer_uri in self.observers: # Iterates
            try:
                # Create a proxy for each observer using its URI
                observer = Pyro4.Proxy(observer_uri)
                observer.update(message)
            except Exception as e:
                print("Error notifying observer", observer_uri, ":", e)

def main():
    # Create a Pyro daemon to expose objects
    daemon = Pyro4.Daemon()

    # Locate the running Name Server (ensure it's running with "python -m Pyro4.naming")
    ns = Pyro4.locateNS()

    # Create an instance of TheObservable
    observable = TheObservable()

    # Register the observable with the daemon, which returns its unique URI
    uri = daemon.register(observable)

    # Register the object with the Name Server under the name "example.observable"
    ns.register("example.observable", uri)

    print("Observable server is ready. Object URI:", uri)
    # Enter the request loop waiting for remote calls
    daemon.requestLoop()

if __name__ == "__main__":
    main()
