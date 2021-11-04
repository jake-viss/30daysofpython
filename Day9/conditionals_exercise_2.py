#1. Write a code which gives grade to students according to theirs scores:
'''90-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''

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

grade_student(92)

#2. 

