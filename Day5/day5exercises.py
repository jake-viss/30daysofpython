# Day 5 Exercises
# Exercises: Level 1

#1. Declare an empty list.
empty_list=[]

#2. Declare a list with more than 5 items.
camp_items = ["hiking boots", "tent", "backpack", "sleeping bag", "sleeping pad", "jet boil"]

# 3. Find the length of your list
print(len(camp_items))

#Get the first item, the middle item and the last item of the list
print(camp_items[0],camp_items[3], camp_items[-1])

#5, Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["Jacob",30,"6'4", "single", "Seattle"]
print(mixed_data_types)

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[-1])
print(it_companies[-1::-3])

#10. Print the list after modifying one of the companies
it_companies[5] = "SalesForce"
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append("Tableau")

#12. Insert an IT company in the middle of the companies list
it_companies.insert(4, "Snowflake")

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0]="FACEBOOK"
print(it_companies)

#14. Join the it_companies with a string '#;  '
joined_list = "#; ".join(it_companies)
print(joined_list)

#15. Check if a certain company exists in the it_companies list.
exists = "Tableau" in it_companies
print(exists)

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#18. Slice out the first 3 companies from the list
print(it_companies[0:3])

#19. Slice out the last 3 companies from the list
print(it_companies[-3:])

#20. Slice out the middle IT company or companies from the list.
print(it_companies[1:-1])

#21. Remove the first IT company from the list
it_companies.remove("Tableau")
print(it_companies)

#22. Remove the middle IT company or companies from the list
del it_companies[1:-1]
print(it_companies)

#23. Remove the last IT company from the list.
it_companies.pop()
print(it_companies)

#24, Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_list.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)
print(joined_list)