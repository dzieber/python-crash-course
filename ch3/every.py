'''
exercise 3.8
'''

things = ['one', 'fish', 'two', 'fish']
print(things)
print(things[0])
print(things[-1])
things[0] = 'moose'
print(things)
things.append('squid')
print(things)
things.insert(2,'fish')
print(things)
print(things.pop(2))
print(things)
del things[1]
print(things)
bad = 'fish'
things.remove(bad)
print(things)
print(sorted(things))
print(sorted(things,reverse=True))
things.reverse()
print(things)
things.reverse()
print(things)
things.sort()
print(things)
things.sort(reverse=True)
print(things)
print(len(things))
