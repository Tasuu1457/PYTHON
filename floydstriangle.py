rows = int(input("Enter the total number of rows: "))
number = 1
print("Floy's triangle: ")
for i in range (1, rows + 1):
    for j in range(1, i+1):
        print(number, end = " ")
        number += 1
    print()