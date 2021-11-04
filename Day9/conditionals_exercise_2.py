#1. Write a code which gives grade to students according to theirs scores:
'''90-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''
'''
def grade_student(score):
    if score >= 90 and score < 100:
        print("Congrats, you recieve an A.")
    elif score < 90 and score > 69:
        print("Congrats, you earned a B.")
    elif score < 70 and score > 59:
        print("You earned a C. There is some room for improvement.")
    elif score < 60 and score > 49:
        print("You received a D. You must work harder.")
    elif score < 50:
        print("You have failed. Here is your F.")
    else:
        print("Over 100%!? Impossible!")

grade_student(92)'''

#2. 
"""Check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn. 
December, January or February, the season is Winter. 
March, April or May, the season is Spring June, July or August, the season is Summer"""

Autumn = ["September","October","November"]
Winter = ["December",'January','February']
Spring = ['March','April','May']
Summer = ['June','July','August']

month=input("Let me tell you what the season is. Enter a month:")

if month in Autumn:
    print("The season is Autumn!")
elif month in Winter:
    print("It's cold out! Definitely winter!")
elif month in Spring:
    print("The flowers have started to bloom. It is Spring!")
elif month in Summer:
    print("Time to head to the beach. It's summer!")
else:
    print("Uhhh... I don't think that is a month.")


#. 3
"""If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')"""

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("What is your favorite fruit?")

if fruit in fruits:
    print("That fruit is already in that list.")
elif fruit not in fruits:
    fruits.append(fruit)
    print(fruits)

#4. 
'''Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:'''
person={
    'first_name': 'Jacob',
    'last_name': 'Vissering',
    'age': 123,
    'country': 'Croatia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Pythonn'],
    'address': {
        'street': 'Balloon Street',
        'zipcode': '02210'
    }
    }

if person["skills"]:
    index=int(len(person["skills"])/2)
    print(person["skills"][index])
else:
    print("Dude has no skills.")

if person["skills"]:
    if "Python" in person["skills"]:
        print("True")
    else:
        print("False")
else:
    print("Dude has no skills.")



