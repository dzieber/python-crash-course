message = "I am a big fan of moose"
print(message)
print("\tMoose!")
print("Moose:\n\tLarge\n\tAntlered\n\tShaggy")
largest_base = 'moose '
print("unstripped" + " " + largest_base + "!")
print("stripped" + " " + largest_base.rstrip() + "!")
largest_base = largest_base.rstrip()
print largest_base
largest_base = '    big   moose     '
print "unstripped" + " " + largest_base + "!"
print "lstripped" + " " + largest_base.lstrip() + "!"
print "stripped" + " " + largest_base.strip() + "!"
