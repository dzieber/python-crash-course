for value in range(1,5):
    print(value)
for value in range(1,6):
    print(value)
print(range(1,5))
numbers = list(range(1,5))
for number in numbers:
    print(number)
numbers = list(range(2,11,2))
for number in numbers:
    print(number)
squares = []
for number in range(1,11):
    squares.append(number**2)
print(squares)
digits = list(range(1,10))
digits.append(0)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
digits.append(11)
print(min(digits))
print(max(digits))
print(sum(digits))
squares = [values**2 for values in range(1,11)]
print squares
