
input_string = input("Enter a string: ")
target_char = input("Enter the character to count: ")


count = 0

for char in input_string:
  
    if char == target_char:
        count += 1


print(f"The character '{target_char}' occurs {count} times in the string.")
