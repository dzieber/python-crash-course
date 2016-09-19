'''
exercise 4-8. Cubes:
make a list of the first 10 cubes and print them with a for loop
'''
cubes = []
for number in range(1,11):
    cubes.append(number**3)
for number in cubes:
    print(number)
