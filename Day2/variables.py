# Day 2: 30 Days of python programming
# Create variables.
first_name = "Jacob"
last_name = "Vissering"
full_name = "Jacob Vissering"
country = "United States of America"
city = "Seattle"
age = 30
year = 2021
is_married = False
is_true = True
is_light_on = True
state, county, neighborhood = "Washington", "King", "Crown Hill"

# Check variable types.
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))

# Check length of name.
print(len(first_name))
print(len(last_name))

# Arithmatic.
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Circle problem. Radius of circle is 30 meters
pi = 3.14159265359
radius = input("What is the radius of the circle?")
area_of_circle = pi * int(radius) ** 2
print(area_of_circle)

circum_of_circle = 2 * pi * int(radius)
print(circum_of_circle)

# Use input to collect information.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
country = input("What country are you from? ")
age = input("what is your age? ")

