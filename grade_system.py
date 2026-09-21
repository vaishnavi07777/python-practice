def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Needs Improvement"


def main():
    name = input("Enter student name: ")

    subjects = ["Python", "Maths", "Physics"]
    marks = []

    for subject in subjects:
        mark = float(input(f"Enter {subject} mark: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(marks)

    print("\n----- STUDENT REPORT -----")
    print(f"Name    : {name}")
    print(f"Total   : {total:.2f}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")
