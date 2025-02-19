import Pyro4

def main():
    # Locate the Name Server and look up the remote object by its registered name.
    ns = Pyro4.locateNS()
    uri = ns.lookup("example.remote.object")

    # Create a proxy for the remote object using its URI.
    remote_object = Pyro4.Proxy(uri)

    # Call the greet method and print its result.
    greeting = remote_object.greet("World")
    print("greet result:", greeting)

    # Call the add method and print its result.
    sum_result = remote_object.add(5, 7)
    print("add result:", sum_result)

    # Dynamic introspection: list the methods available on the remote object.
    # The _pyroMethods attribute is automatically provided by Pyro for exposed methods.
    methods = remote_object._pyroMethods
    print("Dynamic introspection (_pyroMethods):", methods)

if __name__ == "__main__":
    main()
