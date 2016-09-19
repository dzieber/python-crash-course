magicians = ['billy', 'bob', 'alice']
for magician in magicians:
    print(magician.title() + ", you are nifty!")
    print("I like your socks, " + magician.title() + "!\n")
print("All done!")
magicians.append('muffy')
for magician in magicians:
    print(magician)

