def func(name, age):
    print("Name:", name)
    print("Age: ", age)
func("muhammad", 18)

print("------------------------")
# NOW CHANGING THE POSITION
def func(name, age):
    print("Name:", name)
    print("Age: ", age)
func(18, "Muhammad")

# THE COMPILER DON'T KNOW THAT NAME IS TAKING INTEGER CAUSE WE HAVEN'T SPECIFY IT YET
# SAME FOR THE AGE ARGUMENT
# FOR THIS PROBLEM WE WILL USE "EXPECTED TYPE" (name: str, age: int)