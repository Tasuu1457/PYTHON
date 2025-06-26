def valid_age():
    try:
        age = int(input("Enter the age: "))
        if 0 <= age <= 50:
            return True, age
        else:
            return False, "Age must be between 0 and 50."
    except ValueError:
        return False, "Invalid input. Please enter a whole number for age."
    
while True:
    age = input("Please enter your age: ")
    correct, message = valid_age(age)

    if correct:
        print(f"Age entered: {message}. This is a valid age.")
        break
    else:
        print(f"Error: {message}")
        print("Please try again.")

while True:
    try:
        n = int(input("Enter a number: "))
        if n%2 == 0:
            print("Even!")
        else:
            print("Odd!")
    except ValueError:
        print("Error!")