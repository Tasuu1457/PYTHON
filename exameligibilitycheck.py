reason = input("Do you have medical reason? (Yes/No): ").lower()
if reason == "yes":
    attendence = int(input("Enter your attendence percentage: "))
    if attendence >= 60:
        print("You are eligible for the exam!")
    else:
        print("You are not eligible for the exam!")
elif reason == "no":
    attendence = int(input("Enter your attendence percentage: "))
    if attendence >= 75:
        print("You are eligible for the exam!")
    else:
        print("You are not eligible for the exam!")
else:
    print("Invalid input!")