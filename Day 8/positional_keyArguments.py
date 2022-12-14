# Positional Arguments.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Where do you live, {location}")


# greet_with("Keval", "Bharuch")
greet_with("Bharuch", "Keval")  # This is called as Positional arguments.


# Keywords Arguments.
def greet_with_(name, location):
    print(f"Hello {name}")
    print(f"Where do you live, {location}")


# greet_with_(name="keval", location="Bharuch")
greet_with_(location="Bharuch", name="Keval")

