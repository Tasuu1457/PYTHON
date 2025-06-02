n = int(input("Enter a number: "))
res = ''
while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)