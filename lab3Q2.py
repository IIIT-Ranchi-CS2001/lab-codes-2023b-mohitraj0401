number = int(input("Enter a number: "))
original_number = number
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("Number:", original_number)
print("Sum of digits:", sum_of_digits)
