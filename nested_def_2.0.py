def shopping_bill(name: str, items: list):
    def calulate_total(items):
        total = 0
        for i in items:
            total += i
        return total 
    total = calulate_total(items)

    def apply_discount(total):
        if total >= 3000:
            amount = (total * 20) / 100
            return total - amount 
        
        elif total >= 2000:
            amount = (total * 10) / 100
            return total - amount  
        
        elif total >= 1000:
            amount = (total * 5) / 100
            return total - amount 
        
        else:
            return total
        
    discounted_amount = apply_discount(total)
            
    def adding_tax(amount):
        final_amount = (amount * 8) / 100
        return total + final_amount 
    
    final_bill = adding_tax(discounted_amount)

    def display_bill(name, original_total, discounted_amount, final_amount):
        print("Name: ", name)
        print("Orignial Total: ", original_total)
        print("Discounted Total: ", discounted_amount)
        print("Final Total: ", final_amount)

    display_bill(name, total, discounted_amount, final_bill)

list1 = [100,115,200]
shopping_bill("Muhammad", list1)