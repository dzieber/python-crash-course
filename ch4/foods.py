'''
general work in chapter four
also, exercise 4-10. Slices:
    print the first three items from a list
    print three items from the middle of the list
    print the last three items from a list
also, exercise 4-11. More Loops:
    use for loops to print two of the food lists
'''
my_foods = ['mice', 'voles', 'grasshoppers', 'sparrows']
print(my_foods)
your_foods = my_foods[:]
print(your_foods)
my_foods.append('squid')
print(my_foods)
print(your_foods)
your_foods = my_foods
print(my_foods)
print(your_foods)
my_foods.append('chihuahuas')
print(my_foods)
print(your_foods)
print("The first three items from my_foods are:")
for food in my_foods[:3]:
    print(food)
print("Three middle items from my_foods are:")
for food in my_foods[1:4]:
    print(food)
print("The last three items from my_foods are:")
for food in my_foods[-3:]:
    print(food)
for food in my_foods:
    print(food)
for food in your_foods:
    print(food)
