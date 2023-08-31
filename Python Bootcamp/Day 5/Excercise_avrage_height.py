student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
#amount_of_Students = len(student_heights)
amount_of_Students = 0
for student in student_heights:
    amount_of_Students += 1

#total_height = sum(student_heights)
total_height = 0
for height in student_heights:
    total_height += height

avrage_student_height = total_height / amount_of_Students
print(f"The avrage height of the students is {avrage_student_height}cm tall")
