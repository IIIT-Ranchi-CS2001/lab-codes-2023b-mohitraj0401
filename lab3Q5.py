
input_string = input("Enter a string: ")

all_alphanumeric = True


for char in input_string:
    if not char.isalnum():
        all_alphanumeric = False
        break

print(all_alphanumeric)
