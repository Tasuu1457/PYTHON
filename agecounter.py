def check_age():
    while True:
        try:
            age_input = input("Please enter your age: ")
            age = int(age_input)

            if age > 50:
                print("Error: Age seems unusually high.")
            else:
                print(f"You entered: {age}")
                if age % 2 == 0:
                    print("Your age is an even number.")
                else:
                    print("Your age is an odd number.")
                break
        except ValueError:
            print("Error!")
        except Exception as e:
            print(f"Error:{e}")

check_age()
