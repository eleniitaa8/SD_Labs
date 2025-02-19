import Pyro4

@Pyro4.expose # Update() method is available for remote calls
class TheObserver(object):
    def update(self, message):
        """Called by the observable to deliver a message."""
        print("Observer received message:", message)

def main():
    # Create a Pyro daemon for this observer to receive remote calls
    daemon = Pyro4.Daemon()

    # Create an observer instance and register it with the daemon
    observer = TheObserver()
    observer_uri = daemon.register(observer)
    print("Observer is ready with URI:", observer_uri)

    # Locate the Name Server and look up the observable object
    ns = Pyro4.locateNS()
    observable_uri = ns.lookup("example.observable")
    observable = Pyro4.Proxy(observable_uri)

    # Register this observer with the observable using its remote URI
    observable.register_observer(observer_uri)
    print("Observer registered with the observable.")

    # Enter the daemon's request loop to wait for update notifications
    daemon.requestLoop()

if __name__ == "__main__":
    main()
