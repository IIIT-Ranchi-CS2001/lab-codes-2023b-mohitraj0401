
string = "Extraordinary"
letter_count = {}  

for letter in string:
    if letter.isalpha(): 
        letter = letter.lower()  
        if letter in letter_count:
            letter_count[letter] += 1  
        else:
            letter_count[letter] = 1  

print(letter_count)
