# Iterate 0 to 10 using for loop, do the same using while loop.
'''for i in range(11):
    print(i)

count = 0
while count < 11:
    print(count)
    count = count + 1
else:
    print("done")'''

#2. Iterate 10 to 0 using for loop, do the same using while loop.
'''for i in reversed(range(11)):
    print(i)

count = 10
while count >= 0:
    print(count)
    count = count -1'''

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""call = "#"
while len(call) < 8:
    print(call)
    x = "#"
    call = call + x"""


#. 4 Use nested loops to create the following:
num_rows = 8
num_cols = 8

for i in range(num_rows):
    for j in range(num_cols):
        print("#", end=" ")
    print()
    