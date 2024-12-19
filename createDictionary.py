students={}
for i in range(5):
    name = input("Enter the name of student : ")
    marks = float(input("Enter the marks (in percentage) for {name}: "))
    students[name] = marks

high_performers = []
average_performers = []
low_performers = []

highest_marks = -1
top_student = ""

for name, marks in students.items():
    if marks >= 85:
        high_performers.append(name)
    elif 60 <= marks < 85:
        average_performers.append(name)
    else:
        low_performers.append(name)
    
    if marks > highest_marks:
        highest_marks = marks
        top_student = name

print("\nClassification of Students:")
print(f"High Performers (marks ≥ 85): {len(high_performers)}")
print(", ".join(high_performers))

print(f"Average Performers (60 ≤ marks < 85): {len(average_performers)}")
print(", ".join(average_performers))

print(f"Low Performers (marks < 60): {len(low_performers)}")
print(", ".join(low_performers))

print(f"\nThe student with the highest marks is: {top_student} with {highest_marks}%")
