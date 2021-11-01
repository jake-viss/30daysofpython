'''Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries'''

# 1. Create an empty dictionary called dog
dog = {}
#2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Raider', 'color':'black','breed':'mutt','legs':4,'age':10}
#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'','last_name':'','gender':'','age':'','marital_status':'','skills':'','country':'','city':'','address':''}
#4. Get the length of the student dictionary
print(len(student))
print(student)
#5. Get the value of skills and check the data type, it should be a list
student = {'first_name':'Jacob','last_name':'Vissering','gender':'Male','age':'30','marital_status':'Single','skills':['accounting','finance','python','pandas','skiing','rock climbing'],'country':'USA','city':'Seattle'}
print(student['first_name']+student['last_name'])
print(student['skills'])

#6. Modify the skills values by adding one or two skills
student['skills'] = ['accounting', 'finance', 'python', 'pandas', 'skiing', 'rock climbing','mountain biking']
print(student['skills'])

# 7. Get the dictionary keys as a list
print(student.keys())

#8. Get the dictionary values as a list
print(student.values())

#9. Change the dictionary to a list of tuples using items() method
student_tuples = student.items()
print(student_tuples)

#10. Delete one of the items in the dictionary
del student['skills']
print(student)

#11. Delete one of the dictionaries
del student_tuples