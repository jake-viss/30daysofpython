# Day three exercises below.
import numpy as np

age = 30
height = 6.33
cplex_num = 3j

# Area of a triangle script:
'''base = input("Base of triangle: ")
height = input("Height of triangle: ")
area_triangle = 0.5 * float(base) * float(height)
print(area_triangle)'''

# Perimeter of triangle script.
'''side_a = input("Enter trianlge side A: ")
side_b = input("Enter trianlge side B: ")
side_c = input("Enter trianlge side C: ")
triangle_perimeter = float(side_a) + float(side_b) + float(side_c)
print(triangle_perimeter)'''

# Rectangle scripts.
'''rectangle_length = input("Rectangle length? ")
rectangle_width = input("Rectangle width? ")
rectangle_perimeter = 2 * float(rectangle_length) + 2 * float(rectangle_width)
rectangle_area = float(rectangle_width) * float(rectangle_length)
print("The rectangle perimeter is:" , rectangle_perimeter)
print("The rectangle area is:", rectangle_area)'''

#Circle scripts
'''circle_radius = input("Input the radius of your circle: ")
pi = 3.14
area_of_circle = pi * float(circle_radius) ** 2
circumference_circle = 2 * pi * float(circle_radius)
print("The area of your circle is: ", area_of_circle)
print("The circumference of your circle is: ", circumference_circle)'''

# Calculate the slope, x-intercept and y-intercept of y= 2x - 2.
# x_intercept = 
# Confused.

# Calculate the slope and Euclidean distance of (2,2) and (6,10)
# Euclidean distance using numpy:
'''point_a = np.array((2,2))
point_b = np.array((6,10))
euclidean_distance = np.linalg.norm(point_a - point_b)
print("The euclidean distance of ", point_a, "and ", point_b, "is ", euclidean_distance)'''
# Slope w/o any libraries:
'''coordinate_one = [2,2]
coordinate_two = [6,10]
slope = (coordinate_two[1] - coordinate_one[1]) / (coordinate_two[0] - coordinate_one[0])
print(slope)
euclidean_distance = (((coordinate_two[0] - coordinate_one[0])**2) +((coordinate_two[1] - coordinate_one[1])**2)) ** 1/2
print(euclidean_distance)'''
# Slope w/ numpy.
# slope, intercept = np.polyfit(coordinate_one, coordinate_two,1)
# print(slope)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
'''x = -3
y = x ** 2 + 6*x +9
print(y)'''

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_len = len("python")
dragon_len = len("dragon")
print(python_len != dragon_len)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")

#There is no 'on' in both dragon and python
print("on" not in "python" and "on" not in "dragon")

# Find the length of the text python and convert the value to float and convert it to string.
length = len("Python")
length = float(length)
length = str(length)
print(type(length))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
'''num1 = input("Input a number ")
even_number = int(num1) % 2 == 0
print(even_number)'''

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
check = 7 // 3 == int(2.7)
print(check)

# Check if type of '10' is equal to type of 10
print(type("10") == type(10))

# Check if int('9.8') is equal to 10
print(type(int(9.8)) == type(10))

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""hours = input("How many hours did you work this week? ")
rate_per_hours = input("What is your rate per hour? ")

total_pay = float(hours) * float(rate_per_hours)
print(total_pay)"""

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years = input("Enter the number of years you have lived: ")
seconds_alive = float(number_of_years) * 365 * 24 * 60 * 60
print(seconds_alive)

#Write a Python script that displays the following table
list_1 = [1,1,1,1,1]
list_2 = [2,1,2,4,8]
list_3 = [3,1,3,9,27]
list_4 = [4,1,4,16,64]
list_5 = [5,1,5,25,125]

print(list_1)
print(list_2)
print(list_3)
print(list_2)
print(list_5)