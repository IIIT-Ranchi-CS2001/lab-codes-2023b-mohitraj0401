Name = input("Enter the Name: ")
Roll_Number = int(input("Enter the Roll Number: "))
Marks_secured = int(input("Enter the Marks: "))


print("Name: ", Name)
print("Roll_Number: ", Roll_Number)
if Marks_secured >= 90:
    Remark = "OUTSTANDING"
    GRADE = 10
elif Marks_secured >=80 &Marks_secured < 90 :
        Remark = "VERY GOOD"
        GRADE = 9
elif Marks_secured >=70 &Marks_secured < 80 :
        Remark = "GOOD"
        GRADE = 8
elif Marks_secured >=60 &Marks_secured < 70 :
        Remark = "AVERAGE"
        GRADE = 7
elif Marks_secured >=50 &Marks_secured < 60 :
        Remark = "PASS"
        GRADE = 6
elif Marks_secured < 50 :
        Remark = "FAIL"
print("Grade Points: ", GRADE)
print("Remark: ", Remark)

