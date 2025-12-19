def outer():
    print("Hello World")
    def inner():
        print("Welcome!")
    inner()


outer()


