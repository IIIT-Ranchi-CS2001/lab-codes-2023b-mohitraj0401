names = ["Akash", "Vikas", "Prakash"]
rollNos = [7, 34, 25]
Marks = [98, 85, 74]

student_details = [("Akash", 7, 98), ("Vikas", 34, 85), ("Prakash", 25, 74)]

for i in range(len(student_details)):
    for j in range(0, len(student_details) - i - 1):
        if student_details[j][2] > student_details[j + 1][2]:
            student_details[j], student_details[j + 1] = student_details[j + 1], student_details[j]

print(student_details)
