import Pyro4

def main():
    # Create a proxy to the observable object using the name server lookup shortcut
    observable = Pyro4.Proxy("PYRONAME:example.observable")

    # Call notify_observers() on the observable to send a notification to all observers
    observable.notify_observers("Hello, Observers!")
    print("Notification sent.")

if __name__ == "__main__":
    main()
