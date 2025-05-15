C = int(input("Enter C.P: "))
S = int(input("Enter S.P: "))
if S>C:
    profit = S - C
    print(f"You made a profit of {profit}Tk.")
elif S==C:
    print("No profit or no loss!")
else:
    loss = C - S
    print(f"You made a loss of {loss}Tk.")