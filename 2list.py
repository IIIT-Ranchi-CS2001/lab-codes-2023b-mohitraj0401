

course_codes = ["CS1001", "CS1002", "CS1003"]
course_names = ["Python", "Data Structures", "Algorithms"]

combined_courses = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]

print(combined_courses)
