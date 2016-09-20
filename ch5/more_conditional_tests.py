'''
exercise 5-2. More Conditional Tests:
    create more tests, have one True and one False for:
        equality and inequality with strings
        using lower()
        numerical, using equality and inequality, < and >, >= and <=
        using and, or
        whether an item is in a list
        whether an item is not in a list
'''

print("moose" == 'moose')
print("moose" == "meese")
print("MOOSE".lower() == "moose")
print("MOOSE".lower() == "MOOSE")
print(4 == 2**2)
print(4 == 2**3)
print(4 != 2*3)
print(4 != 2 + 2)
print(4 > 3)
print(4 < 4)
print(4 >= 4)
print(4 >= 5)
print(4 == 4 and 4 >= 4)
print(4 == 4 and 4 > 4)
print(4 == 4 or 4 < 4)
print(4 <= 3 or 3 == 2)
print("mouse" in ['mouse', 'squid'])
print("moose" in ['mouse', 'squid'])
print("yak" not in ['mouse', 'squid'])
print("squid" not in ['mouse', 'squid'])
