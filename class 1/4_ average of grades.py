import locale

# Setting up locale lo allow user put commas or dots on decimals
locale.setlocale(locale.LC_ALL, 'es_PE.UTF-8')

def compute_average(grades):
    total = sum(grades)
    average = total / len(grades)
    rounded_average = round(average, 2)
    return average

grades = []
while True:
    grade = input("Enter a grade an enter 'done' when you're finished: ")
    if grade.lower() == 'done':
        break
    grade = locale.atof(grade)
    grades.append(float(grade))

average = compute_average(grades)
print("The average grade is: ", average)