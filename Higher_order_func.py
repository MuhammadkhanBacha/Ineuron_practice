def square(num):
    return num * num

def operate(num, operate):
    return operate(num)

result = operate(5, square)
print(result)
