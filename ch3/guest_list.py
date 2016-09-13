'''
the program for exercies 3.4 - 3.7
'''

guest_list = ['ME', 'myself', 'i']
message = "I would love to invite to dinner " + guest_list[0].title() + ", " \
    + guest_list[1].title() + ", and " + guest_list[-1].upper() + "."
print(message)
print("I am inviting " + str(len(guest_list)) + " people to dinner.")
no_show = 'i'
print("Oh noes, " + no_show.upper() + " can't make it!")
new_guest = 'yo'
guest_list.append(new_guest)
guest_list.remove(no_show)
message = "I would love to invite to dinner " + guest_list[0].title() + ", " \
    + guest_list[1].title() + ", and " + guest_list[-1].upper() + "."
print(message)
print("I done found me a bigger table!")
guest_list.insert(0,"god_king")
guest_list.insert(2,"master")
guest_list.append("lord")
print("I am inviting " + str(len(guest_list)) + " people to dinner.")
message = "I would love to invite to dinner " + guest_list[0].title() + ", " \
    + guest_list[1].title() + ", " + guest_list[-1].upper() + ", " +\
    guest_list[-2] + ", " + guest_list[-3] + ", and " + guest_list[-4] + "."
print(message)
print("Oh noes!  My table shrunk!")
print("Sorry " + guest_list.pop() + ", you outta here!")
print("Sorry " + guest_list.pop() + ", you outta here!")
print("Sorry " + guest_list.pop() + ", you outta here!")
print("Sorry " + guest_list.pop() + ", you outta here!")
print("I am inviting " + str(len(guest_list)) + " people to dinner.")
print("Hey "+ guest_list[0].title() + " and " + guest_list[-1].title() + \
    ", c'mon bye!")
del guest_list[0]
del guest_list[0]
print(guest_list)
