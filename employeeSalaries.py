employees ={}
for i in range(5):
    name = input("Enter the name of employee : ")
    salary = float(input("Enter the salary  for {name}: "))
    employees[name] = salary

employee_list = list(employees.items())
n = len(employee_list)

for i in range(n):
    for j in range(0, n - i - 1):
        if employee_list[j][1] < employee_list[j + 1][1]:
            employee_list[j], employee_list[j + 1] = employee_list[j + 1], employee_list[j]

print("\nEmployees sorted by salary (Highest to Lowest):")
for rank, (name, salary) in enumerate(employee_list, start=1):
    print(f"Rank {rank}: {name} - Rs{salary:.2f}")
