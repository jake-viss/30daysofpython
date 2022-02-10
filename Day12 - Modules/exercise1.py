import random
import string
def random_user_id():
    user_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range (6)])
    return user_id

print(random_user_id())

