'''
exercise 4-9. Cube Comprehsion
use a list comprehension to generate a list of cubes from 1 to 10
'''
cubes = [number**3 for number in range(1,11)]
for number in cubes:
    print(number)
