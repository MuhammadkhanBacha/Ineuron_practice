def square(num):
    return num * num

def operation(values, operate):
    for i in values:
        result = operate(i)
        print(result, sep="-")

values = [4,5,6,7]
operation(values, square)