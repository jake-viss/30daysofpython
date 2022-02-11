import random
import string

# Write a function which generates a six digit/character random_user_id.
'''def random_user_id():
    user_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range (6)])
    return user_id

print(random_user_id())'''

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    num_characters = int(input("Input how many characters for User ID: "))
    num_IDs = int(input("Input how many user IDs to create: "))
    # list_Ids = []
    for n in range(num_IDs):
        user_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(num_characters)])
        # list_Ids.append(user_id)
        print(user_id)
    # return list_Ids

print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    num1 = random.randint(0,255)
    num2 = random.randint(0,255)
    num3 = random.randint(0,255)
    rgb = "rgb(" + str(num1)+","+str(num2)+","+str(num3)+")"
    return rgb

print(rgb_color_gen())

