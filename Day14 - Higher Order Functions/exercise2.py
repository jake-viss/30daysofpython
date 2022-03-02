from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map to create a new list by changing each country to uppercase in the countries list
def uppercase(x):
    return x.upper()

upper_case_countries = map(lambda x: x.upper(), countries)
print(list(upper_case_countries))

# Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = map(lambda x:x**2, numbers)
print(list(squared_numbers))

# Use map to change each name to uppercase in the names list
upper_case_names = map(lambda x: x.upper(), names)
print(list(upper_case_names))

# Use filter to filter out countries containing 'land'.
def landless(x):
    if "land" not in x:
        return True
    else:
        return False

landless_countries = filter(landless, countries)
print(list(landless_countries))

# Use filter to filter out countries having exactly six characters.

def six_exact(x):
    if len(x) == 6:
        return False
    else:
        return True

countries_not_six = filter(six_exact, countries)
print(list(countries_not_six))