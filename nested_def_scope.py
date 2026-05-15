def outer():
    def inner():
        x = 10
        return x

    result = inner()
    print("Inside outer:", result)

outer()

# without storing it in a variable
# def outer():
#     def inner():
#         x = 10
#         return x

#     print("Inside outer:", inner())

# outer()