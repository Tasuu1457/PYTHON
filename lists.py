fruits = ["Apple", "banana", "cherry"]
print(fruits)

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

colours = ["Red,", "yellow,"]
colours.extend(["blue", "black"])
print(colours)

animals = ["Cat,", "dog,", "rabbit"]
animals.insert(2, "hamster,")
print(animals)

cities = ["London,", "Paris,", "New York"]
cities.remove("Paris,")
print(cities)

languages = ["Python, ", "Java, ", "C++"]
removed = languages.pop()
print(languages)

scores = [88, 75, 92, 60]
scores.sort()
print(scores)

letters = ["a", "b", "c", "d"]
letters.reverse()
print(letters)

numbers = [1, 2, 3, 4, 5, 5, 4, 3, 3, 2, 1, 0]
count_2 = numbers.count(2)
print(2)