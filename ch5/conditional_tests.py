'''
exercise 5-1. Conditional Tests:
    write a series of condtions tests
    Print a statement describing each test and your prediction for the 
    results of each test
    create at least 10 tests
'''

car = 'beetle'
print("Is the little thing a beetle?  I think True.")
print(car == 'beetle')
print("Is it a moose?  I think False.")
print(car == 'moose')
beasties = ['moose', 'kitty', 'squid', 'yak', 'llama']
print("Is a moose a beastie?  I think True.")
print('moose' in beasties)
print("Is a car a beastie?  I think False.")
print('car' in beasties)
print("Is a toe not a beastie?  I think True.")
print('toe' not in beasties)
print("Is a yak not a beastie?  I think False.")
print("yak" not in beasties)
print("Is a Squid in beasties?  I think True, if properly capitalized.")
print("Squid".lower() in beasties)
print("Are a kitty and a llama both beasties?  I think True.")
print("kitty" in beasties and "llama" in beasties)
print("Are a bottle and a moose beasties?  I think False.")
print("bottle" in beasties and "moose" in beasties)
print("Are a bottle or a moose beasties?  I think True.")
print("bottle" in beasties or "moose" in beasties)
print("kitty is in beasties, is KITTY?  I think False.")
print("KITTY" in beasties)
print("how about a fuzzy-wuzzy-muffin?  I think False.")
print("fuzzy-wuzzy-muffin" in beasties)
