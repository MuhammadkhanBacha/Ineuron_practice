def show_result(func):
    def wrapper(*number):
        print("Calculation started")
        result = func(*number)
        print(result)
        print("Calculation ended")
        return result
    return wrapper


@show_result
def add_numbers(a, b, c):
    return a + b + c

@show_result
def multiply_numbers(a, b):
    return a * b

add_numbers(1,2,3)
multiply_numbers(5,5)