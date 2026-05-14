def calculate_total(price):
    def calculate_tax():
        return price * 0.10
    
    tax = calculate_tax()
    total = price + tax
    return total

print(calculate_total(1000))



# without nested def

# def calculate_tax(price):
#     return price * 0.10

# def calculate_total(price):
#     tax = calculate_tax(price)
#     total  = price + tax
#     return total

# print(calculate_total(1000))
