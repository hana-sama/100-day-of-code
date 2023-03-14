student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for student in student_heights:
    total_height += student

print(total_height)

number_of_student = 0
for student in student_heights:
    number_of_student += 1

print(number_of_student)
average_height = total_height / number_of_student

print(round(average_height, 1))