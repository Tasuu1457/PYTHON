word = input("Enter a string to check the occurance: ")
letter = input("Enter a letter to find the count: ")
count = 0
for i in word:
    if i == letter:
        count += 1
print(f"The letter '{letter}' occurs {count} in the string.")