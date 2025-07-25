a = {'apple', 'banana', 'orange'}
b = {'banana', 'date', 'orange'}
print("1. Union",a.union(b))
print("2. Intersection", a.intersection(b))
print("3. Difference (A - B)", a.difference(b))
print("3. Difference (B - A)", b.difference(a))
print("5. Symmetric Difference",a.symmetric_difference(b))