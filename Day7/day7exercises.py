# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

"""Exercises: Level 1
1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard"""

print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
new_it_companies = ["Tableau","Salesforce","SnowFlake"]
it_companies.update(new_it_companies)
print(it_companies)
it_companies.remove("IBM")
print(it_companies)
it_companies.discard("Oracle")
print(it_companies)

"""Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely"""

AB = A.union(B)
print(AB)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
AB = A.union(B)
BA = B.union(A)
print(AB)
print(BA)
print(A.symmetric_difference(B))
del A
del B

"""
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set"""

age_set = set(age)
print(len(age))
print(len(age_set))
# The list is bigger because it contains duplicates. 

# A string is made up of letters and numbers, like a sentence.
# A list is an un-ordered collection of datatypes. It can contain strings, integers, floats, lists.
# A tuple is an immutable list of objects. It cannot be changed.
# A set is an immutable collection of objects, however, it cannot contain duplicate values. 
# 
