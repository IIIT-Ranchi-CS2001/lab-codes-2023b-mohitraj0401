names =["Akash", "Vikas", "Prakash"]
rollNos =[7,34,25]
Marks =[98,85,74]

student_details = list(zip(names,rollNos,Marks))
sorted_students = sorted(student_details, key=lambda x: x[2])
print(sorted_students)





