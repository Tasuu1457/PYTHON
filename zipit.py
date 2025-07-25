fruits = ["Apples", "Orange", "Mango", "Dragon fruit"]
prices = [350, 300, 120, 200]
data = {fruits: prices for fruits, prices in zip(fruits, prices)}
print(data)