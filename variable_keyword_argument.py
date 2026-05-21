def student_info(**kwargs):
    print(kwargs)

student_info(name="Ali", age=18, city="Lahore")


print("-----------------------------------------------")

# example with access the values
def student_info(**kwargs):
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])

student_info(name="Ali", age=18)
