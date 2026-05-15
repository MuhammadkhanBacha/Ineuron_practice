def outer():
    def inner():
        x = 10
        return x

    print("Inside outer:", inner())

outer()