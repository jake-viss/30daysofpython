# Create an empty tuple
empty_tuple = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother_tuple = ("Sage", "Blake", "Devin")
sister_tuple = ("AJ", "Kelsea")
# Join brothers and sisters tuples and assign it to siblings
siblings = brother_tuple + sister_tuple
# How many siblings do you have?
print(len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
print(type(siblings))
parents = ["jim", "Heidi"]
family_members = tuple(siblings + parents)
print(type(family_members))


# Unpack siblings and parents from family_members
print(family_members)
siblings = family_members[0:4]
parents = family_members[5:]
print(siblings)
print(parents)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("orange","peach","lemon","plum")