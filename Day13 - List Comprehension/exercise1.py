# Filter only negative and zero in the list using list comprehension
from numpy import number


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

e1 = [i for i in numbers if i >= 0]

print(e1)

name = "Jacob Vissering"
n1 = [i for i in name]
print(n1)

numbers = [i for i in range(10)]
print(numbers)

squared_nums = [i for i in range(101) if i % 2 ==0]
print(squared_nums)

squared_nums = [i for i in range(101) if i % 2 ==0 and i > 50]
print(squared_nums)

math_list = [i * 3 for i in range (6)]
print(math_list)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [number for row in list_of_lists for row in row for number in row]

print(flattened_list)

# Using list comprehension create the following list of tuples:

