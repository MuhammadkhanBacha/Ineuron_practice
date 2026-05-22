def decorate_Average_marks(func):
    def wrapper(marks):
        print("Marks is processing")
        result = func(marks)
        print("Marks completed")

        return result

    return wrapper

@decorate_Average_marks
def average_Marks(marks):
    total = 0

    for i in marks:
        total += i

    return total / len(marks)
    
marks = [10,20,30,40,50]
print(average_Marks(marks))
