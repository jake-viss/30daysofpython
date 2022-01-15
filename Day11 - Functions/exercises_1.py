# Add two numbers function
def add_two_numbers(num1,num2):
    _sum = num1 + num2
    return _sum
print(add_two_numbers(8,7))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14159265359
    area = pi * r * r
    return area
print(area_of_circle(8))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    for num in nums:
        if type(num) != int:
            return "You have invalid arguments"
    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(5,5,"5"))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def celsius_to_fahrenheit(c):
    fahrenheit = (c *9/5) +32
    return fahrenheit
print(celsius_to_fahrenheit(50))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    winter = ["December","January","February"]
    spring = ["March","April","May"]
    summer = ["June","July","August"]
    fall = ["September","October","November"]
    if month in winter:
        return "This is a winter month."
    elif month in spring:
        return "This is a spring month."
    elif month in summer:
        return "This is a summer month."
    else:
        return "This is a fall month."
print(check_season("May"))

# Write a function called calculate_slope which return the slope of a linear equation
def slope(x1,y1,x2,y2):
    m = (y2-y1) / (x2 - x1)
    return m
print(slope(4,5,8,10))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(your_list):
    for item in your_list:
        print(item)
my_list = ["boom","snap","clap",2007]
print_list(my_list)
    