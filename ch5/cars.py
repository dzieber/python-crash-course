'''
initial scratchpad for chapter 5
'''

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# True == non-zero, False == 0

requested_car = 'honda'
if requested_car != 'toyota':
    print("Hold the toyota!")

age_0 = 22
age_1 = 18
result = age_0 >= 21 and age_1 >= 21
print(result)
result = age_0 >= 21 or age_1 >= 21
print(result)
if 'audi' in cars:
    print("wowzer")
if 'audi' not in cars:
    print("bummer")
else:
    print("w00t")
