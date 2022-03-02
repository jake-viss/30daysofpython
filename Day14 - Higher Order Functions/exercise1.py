# Define a call function before map, filter or reduce, see examples.
from tkinter import Y
from numpy import square
from functools import reduce


numbers = [12, 24, 36, 48, 60]
def square_rt(x):
    return x // 2

square_root_nums = map(lambda x: x//2, numbers)
print(list(square_root_nums))

def bigs(x):
    if x > 40:
        return True
    else:
        return False

big_nums = filter(bigs, numbers)

print(list(big_nums))

other_numbers = [2, 5, 8]
def multip(x,y):
    return x * y

huge_num = reduce(multip, other_numbers)
print(huge_num)

# Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for i in countries:
    print(i)

# Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for i in names:
    print(i)

# Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i)


