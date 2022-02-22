# Filter only negative and zero in the list using list comprehension
from aem import con
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
tup_list = [tuple([i] + [i**j for j in range(6)]) for i in range(11)]
print(tup_list)


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
'''output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]'''
countries_flattened = [country for row in countries for tuple in row for country in tuple]
countries_flattened2 = [[country] + [country[0:4]] for sublist in countries for tuple in sublist for country in tuple]
countries_flattened3 = [[sublist[0]] + [sublist[0][0:3]] + [sublist[1]] for sublist in countries for sublist in sublist]
countries_flattened4 = [[sublist[0]] + [sublist[0][0:3]] + [sublist[1]] for sublist in countries for sublist in sublist]
# Need to find out how to capitalize
print(countries_flattened4)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
'''output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]'''
list_of_dicts = [{'country':sublist[0], 'city':sublist[1]} for sublist in countries for sublist in sublist]
print(list_of_dicts)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
'''output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']'''
conc_strings = [(sublist[0] + ' ' + sublist[1]) for sublist in names for sublist in sublist]
print(conc_strings)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
