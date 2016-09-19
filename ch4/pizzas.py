'''
problem 4.1, problem 4.11
'''

pizzas = ['cheese', 'meat', 'veggie']
for pizza in pizzas:
    print("yummy " + pizza + " pizza!")
print("I really like " + pizza + " pizza.")
print("It is the best pizza.")
print("Yup.")
friend_pizzas = pizzas[:]
pizzas.append('anchovy')
friend_pizzas.append('hawaiian')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
