# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
from numpy import var


def evens_and_odds(num):
    evens = []
    odds = []
    for i in range(num+1):
        if i % 2 != 0:
            odds.append(i)
        else:
            evens.append(i)
    evens_count = len(evens)
    odds_count = len(odds)
    return print(f"The number of odds are {odds_count}. The number of evens are {evens_count}.")


evens_and_odds(100)

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    total = 1
    for i in range(1,num+1):
        total = total * i
    return total

print(factorial(10))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param == {}:
        print("The parameter is empty")
    else:
        print("The parameter is not empty")

variable = ["Moose","Elk"]
is_empty(variable)

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(_list):
    list_len = len(_list)
    total = 0
    for i in _list:
        total += i
    mean = total / list_len
    return mean

ex = [10,5,5,7]
print(calculate_mean(ex))


    