import math
def calculate_circumference(x):
    circumference = 2 * 3.141 * x
    return circumference
x = int(input("Enter the radius: "))
circumference = calculate_circumference(x)
print(f"The circumference of a circle is: {circumference}")