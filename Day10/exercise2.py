#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
'''def sum_range(x):
    num = 0
    for i in range(x):
        num += i
    return num

print(sum_range(101))'''

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
'''def sum_range(x):
    num = 0
    odd_num = 0
    for i in range(0,x,2):
        num += i
    for i in range(x):
        if i % 2 != 0:
            odd_num += i
    return num and odd_num

print(sum_range(101))'''

   