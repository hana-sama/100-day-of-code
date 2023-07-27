import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Angela"]


student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {name: score for (name, score) in student_scores.items() if score >= 60}
print([passed_students])