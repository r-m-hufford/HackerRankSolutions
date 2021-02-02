# if the difference in the grade and the next multiple of 5 is less than three round up.
# if under 38 no rounding.
# output given sample is 75 67 40 33
import math

grades = [73, 67, 38, 33]


def grading_students(grades):
    final_grades = []
    for grade in grades:
        if grade <= 37:
            final_grades.append(grade)
        elif (grade + 2) % 5 == 0:
            final_grades.append(round(grade / 5) * 5)
        elif (grade + 1) % 5 == 0:
            final_grades.append(round(grade / 5) * 5)
        else:
            final_grades.append(grade)
    return final_grades


print(grading_students(grades))
