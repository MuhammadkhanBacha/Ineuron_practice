def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."
    
# number = int(input("Enter any number: "))
result = check_even_odd(number= 5)
print(result)