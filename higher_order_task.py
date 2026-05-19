def process_marks(marks, func):
    return func(marks)

def passed_Marks(marks):
    for i in marks:
        result =  i
        if(result >= 50):
            return result
    else:
        print("Marks is less than 50. ->", result)

def addBonus(marks):
    result = []
    for i in marks:
        sum = i + 5
        if (sum > 100):
            sum = 100
        result.append(sum)
    return result
    


def average_Marks(marks):
    total = 0
    for i in marks:
        total += i
    return total / len(marks)

marks = [45, 78, 90, 32, 67, 88, 55, 100, 29]

# output for passing marks
passingResult=process_marks(marks, passed_Marks)
print(passingResult)

# output for average marks
AverageResult = process_marks(marks, average_Marks)
print(AverageResult)

# output for adding bonus 
BonusResult = process_marks(marks, addBonus)
print(BonusResult)