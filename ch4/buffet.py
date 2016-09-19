'''
exercise 4-13. Buffet:
    store five foods in a tuple
    try to modify one of the items, watch the errors
    add a block of code to change the items, print each item with a for loop
'''

foods = ('crab', 'chicken', 'beef', 'pork', 'duck')
for food in foods:
    print(food)
print("\n")

# this line breaks things because tuples are immutable
# foods[4] = 'moose'

temp_foods = list(foods)
temp_foods[3:] = ["bok choy", "tofu"]
foods = tuple(temp_foods)
for food in foods:
    print(food)
print("\n")
