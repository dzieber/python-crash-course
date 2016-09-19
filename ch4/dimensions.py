'''
chapter 4, Tuples
'''
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# to copy a tuple into a list you have to cast it
temp_dimensions = list(dimensions[:])
print(temp_dimensions)
temp_dimensions[0] = 250
print(temp_dimensions)
# and it works the other way as well.  Note that you don't need to make it
#   a slice when copying with the type cast
dimensions = tuple(temp_dimensions)
print(dimensions)
temp_dimensions.append(1000)
print(temp_dimensions)
print(dimensions)
