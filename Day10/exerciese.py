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
for i in reversed(range(11)):
    print(i)

count = 10
while count >= 0:
    print(count)
    count = count -1
