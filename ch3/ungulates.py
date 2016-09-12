'''
Playing with lists
'''
ungulates = ['moose', 'deer', 'goat', 'giraffe']
print(ungulates[0].upper())
print(ungulates[-1].upper()) # index -1 starts at the end of the list
print(ungulates[-4].upper()) # counting them backwards goes all the way to the front
print(ungulates[-2])         # so, weird off-by one errors going backwards

# accessing list elements inside a string
message = "My first ungulate was a" + " " + ungulates[0].title() + "."
print(message)

# exercise 3.1
friends = ["Aaron", "Scott", "Jude", "Garrett"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

# exercise 3.2
message_part1 = "Some of my friends are:" + "  " + friends[0].title() + ", "
message_part2 = friends[1].title() + ", " + friends[2].title() + ", "
message_part3 = friends[3].title() + "."
print(message_part1 + message_part2 + message_part3)

# exercise 3.3
pogo_sticks = ['nifty', 'shiny', 'working', 'springy']
message = "I would like to own a" + " " + pogo_sticks[-1] + " " + "pogo stick."
print(message)
message = "I would like to own a" + " " + pogo_sticks[-3] + " " + "pogo stick."
print(message)
message = "I would like to own a" + " " + pogo_sticks[-2] + " " + "pogo stick."
print(message)
message = "I would like to own a" + " " + pogo_sticks[-4] + " " + "pogo stick."
print(message)

