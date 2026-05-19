# passing a list to another list
marks = [1,2,3,4,5]
marks2 = []

def ret():
    for i in marks:
        marks2.append(i)

    return marks2

print(ret())