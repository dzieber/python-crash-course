'''
Working on adding and removing elements from lists
'''
squids = ['humbolt', 'fried', 'calamari', 'poke']
print(squids)
squids[0] = 'tasty'
print(squids)
squids.append('buttered')
print(squids)
del squids[3]
print(squids)
squids.insert(2,squids.pop())
print(squids)
squids.insert(1,'yucky')
print(squids)
message = "I don't like " + squids.pop(1) + " squids."
print(message)
not_prep = 'tasty'
squids.remove(not_prep)
print(squids)
message = "I think that squid is " + not_prep + " when it is " + squids[0] + \
        " and " + squids[1] + "."
print(message)
