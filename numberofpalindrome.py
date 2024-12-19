sentence = input("Enter the word: ")

palindromes = [word for word in sentence.split() if word.lower() == word.lower()[::-1]]

print("no of palindrome words are: ", len(palindromes))