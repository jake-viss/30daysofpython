# Add two numbers function
from audioop import reverse
from hashlib import new


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

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(nums):
    new_list = []
    for i in range(len(nums)):
        new_list.insert(i,nums[-1])
        nums.pop(-1)
    return print(new_list)
   

nums = [1,2,3,4,5]
reverse_list(nums)

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(items):
    capitalized_items = []
    for i in range(len(items)):
        capitalized_items.append(items[i].capitalize())
    return print(capitalized_items)

words = ["jake","liz","lilly"]
capitalize_list_items(words)
print(words[1].capitalize())

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(xlist, item):
    xlist.append(item)
    return xlist

test_list = ["ski", 2022, "pow"]
add_item(test_list, "steep")
print(test_list)

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(xlist, item):
    xlist.remove(item)
    return xlist


remove_item(test_list, "ski")
print(test_list)  

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    total = 0
    for i in range(num+1):
        total += i
    return print(total)

sum_of_numbers(10)

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def sum_of_odds():

